import os
import random

import requests

from api_exceptions import ResponseStatusCodeException, RespondErrorException
from data.segment_create_data import SegmentCreateData
from homework3.input_data_generator import MyFaker


class ApiClient:
    def __init__(self, base_url, login, password):
        self.base_url = base_url
        self.login = login
        self.password = password
        self.session = requests.Session()

    def _request(self, method, location, headers=None, data=None, expected_status=200, params=None, json=None):
        url = location
        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params, json=json)
        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"')

        return response

    def get_token(self):
        location = self.base_url
        res = self._request('GET', location)
        headers = res.headers['Set-Cookie'].split(';')
        token_header = [c for c in headers if 'csrftoken' in c]
        if not token_header: raise Exception('csrf_token not found')
        token_header = token_header[0]
        csrf_token = token_header.split('=')[-1]

        return csrf_token

    def post_login(self):
        url = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'

        headers = {
            'Referer': 'https://target.my.com/',
        }

        data = {
            'email': self.login,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        result = self._request('POST', url, headers=headers, data=data)
        self.csrf_token = self.get_token()
        return result

    def add_segment(self):
        headers = {
            "X-CSRFToken": f'{self.csrf_token}',
        }

        data = SegmentCreateData.data
        url = f"https://target.my.com/api/v2/remarketing/segments.json"

        resp = self.session.post(url=url, headers=headers, json=data)
        segment_id = resp.json()['id']
        self.find_segment(segment_id, segment_exists=True)

    def get_segments(self):
        url = f"https://target.my.com/api/v2/remarketing/segments.json"
        return self.session.get(url).json()

    def get_campaigns(self):
        url = f"https://target.my.com/api/v2/campaigns.json"
        return self.session.get(url).json()

    def get_segments_id(self):
        resp = self.get_segments()
        return [i['id'] for i in resp['items']]

    def get_campaigns_id(self):
        resp = self.get_campaigns()
        return [i['id'] for i in resp['items']]

    def find_segment(self, segment_id, segment_exists=True):
        url = f"https://target.my.com/api/v2/remarketing/segments/{segment_id}.json"
        resp: dict = self.session.get(url).json()
        assert ((resp.get('id') == segment_id) == segment_exists)

    def find_campaign(self, campaign_id, campaign_exists=True):
        url = f"https://target.my.com/api/v2/campaigns/{campaign_id}.json?fields=status"
        resp = self.session.get(url).json()
        assert ((resp.get('status') == "active") == campaign_exists)

    def get_random_existing_segment_id(self):
        all_segments_id = self.get_segments_id()
        assert len(all_segments_id) != 0, "No segments to delete"
        index = random.randint(0, len(all_segments_id) - 1)
        return all_segments_id[index]

    def delete_segment(self, segment_id):
        url = f"https://target.my.com/api/v2/remarketing/segments/{segment_id}.json"
        headers = {
            "X-CSRFToken": f'{self.csrf_token}',
        }
        self.session.delete(url, headers=headers)
        self.find_segment(segment_id, segment_exists=False)
        print(f"Segment with id: {segment_id} was deleted")

    def delete_campaign(self, campaign_id):
        url = f"https://target.my.com/api/v2/campaigns/{campaign_id}.json"
        headers = {
            "X-CSRFToken": f'{self.csrf_token}',
        }
        self.session.delete(url, headers=headers)
        self.find_campaign(campaign_id, campaign_exists=False)
        print(f"Campaign with id: {campaign_id} was deleted")

    def create_picture(self):
        location = "https://target.my.com/api/v2/content/static.json"
        headers = {
            "X-CSRFToken": self.csrf_token,
        }
        file = {
            "file": open(f"..{os.sep}data{os.sep}picture.png", "rb"),
        }
        return self.session.post(url=location, headers=headers, files=file)

    def get_picture_url_id(self, image_id):
        url = "https://target.my.com/api/v2/mediateka.json"
        headers = {
            "X-CSRFToken": self.csrf_token,
        }
        data = {
            "content": {
                "id": image_id
            },
            "description": "picture.png"
        }
        resp = self.session.post(url=url, headers=headers, json=data)
        return resp.json()['id']

    def create_campaign(self, objective='traffic', package_id=961):
        url = "https://target.my.com/api/v2/campaigns.json"
        headers = {
            "X-CSRFToken": self.csrf_token,
        }
        picture_data = self.create_picture().json()
        image_id = picture_data['id']
        url_id = self.get_picture_url_id(image_id)
        data = {
            "banners": [{"content": {"image_240x400": {"id": image_id}}, "urls": {"primary": {"id": url_id}}}],
            "name": MyFaker.fake_name(),
            "objective": objective,
            "package_id": package_id,
        }
        resp = self.session.post(url=url, headers=headers, json=data)
        campaign_id = resp.json()['id']
        return campaign_id
