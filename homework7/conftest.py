import os
import time

import pytest
import requests
from requests.exceptions import ConnectionError

import settings
from application.client import HttpClient
from mock import flask_mock


def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 15:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError(f'{host}:{port} did not started in 5s!')


def start_mock():
    flask_mock.run_mock()
    wait_ready(host=settings.MOCK_HOST, port=settings.MOCK_PORT)


def stop_mock():
    requests.get(f'https://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        start_mock()


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        stop_mock()


@pytest.fixture(scope='function')
def mock_client():
    return HttpClient(settings.MOCK_HOST, int(settings.MOCK_PORT))


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))

