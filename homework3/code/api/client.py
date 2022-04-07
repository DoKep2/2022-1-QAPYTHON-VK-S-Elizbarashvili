import json
import random
import faker
import requests

from input_data_generator import fake_name
from data.campaign_create_data import *

f = faker.Faker()
SEGMENTS_LIMIT = 100


class RespondErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:
    def __init__(self, base_url, login, password):
        self.base_url = base_url
        self.login = login
        self.password = password
        self.session = requests.Session()

    def _request(self, method, location, headers=None, data=None, expected_status=200, jsonify=True, params=None,
                 json=None):
        url = location
        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params, json=json)
        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"')

        if jsonify:
            json_response = response.json()
            if json_response.get('bStateError', False):
                error = json_response['sErrorMsg'] or 'Unknown'
                raise RespondErrorException(f'Request {url} returned error {error}!')

            return json_response

        return response

    def get_token(self):
        location = 'https://target.my.com/csrf/'
        res = self._request('GET', location, jsonify=False)
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

        result = self._request('POST', url, headers=headers, data=data, jsonify=False)
        self.csrf_token = self.get_token()
        return result

    def add_segment(self):
        headers = {
            "X-CSRFToken": f'{self.csrf_token}',
        }

        data = {
            "name": fake_name(f),
            "logicType": "or",
            "pass_condition": "1",
            "relations": [
                {
                    "object_type": "remarketing_player",
                    "params": {
                        "type": "positive",
                        "left": "365",
                        "right": "0"
                    },
                }
            ]
        }
        url = f"https://target.my.com/api/v2/remarketing/segments.json?limit={SEGMENTS_LIMIT}"

        resp = self.session.post(url=url, headers=headers, json=data)
        segment_id = json.loads(resp.content.decode('utf-8'))['id']
        self.find_segment(segment_id, segment_exists=True)

    def get_segments(self):
        url = f"https://target.my.com/api/v2/remarketing/segments.json?limit={SEGMENTS_LIMIT}"
        return self.session.get(url).json()

    def get_campaigns(self):
        url = f"https://target.my.com/api/v2/campaigns.json?limit={SEGMENTS_LIMIT}"
        return self.session.get(url).json()

    def get_segments_id(self):
        resp = self.get_segments()
        return [i['id'] for i in resp['items']]

    def get_campaigns_id(self):
        resp = self.get_campaigns()
        return [i['id'] for i in resp['items']]

    def find_segment(self, segment_id, segment_exists=True):
        resp = self.get_segments_id()
        segments = [i for i in resp if segment_id == i]
        assert (len(segments) != 0) == segment_exists

    def find_campaign(self, campaign_id, campaign_exists=True):
        resp = self.get_campaigns_id()
        campaigns = [i for i in resp if campaign_id == i]
        assert (len(campaigns) != 0) == campaign_exists

    def get_random_existing_segment_id(self):
        all_segments_id = self.get_segments_id()
        if len(all_segments_id) == 0:
            print("Nothing to delete")
            return
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
        resp = self.session.delete(url, headers=headers)
        assert resp.status_code == 204
        print(f"Campaign with id: {campaign_id} was deleted")

    def create_campaign(self, name=fake_name(f)):
        url = "https://target.my.com/api/v2/campaigns.json"
        headers = {
            "Referer": 'https://target.my.com/campaign/new',
            "X-CSRFToken": self.csrf_token
        }

        data = {
            "banners": [{"content": {"image_240x400": {"id": image_id}}, "urls": {"primary": {"id": url_id}}}],
            "name": name,
            "objective": objective,
            "package_id": package_id,
        }
        resp = self.session.post(url=url, headers=headers, json=data)
        campaign_id = resp.json()['id']
        self.find_campaign(campaign_id, campaign_exists=True)
        self.delete_campaign(campaign_id)
