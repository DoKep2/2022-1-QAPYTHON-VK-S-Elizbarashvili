import os

from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--appium', default='http://127.0.0.1:4723/wd/hub')


@pytest.fixture(scope='session')
def config(request):
    appium = request.config.getoption('--appium')
    return {'appium': appium}


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))


@pytest.fixture(scope='session')
def get_apk_name(repo_root):
    from os import listdir
    from os.path import isfile, join
    apk_path = os.path.join(repo_root, "stuff")
    files_names = [f for f in listdir(apk_path) if isfile(join(apk_path, f))]
    apk_file_name = files_names[0]
    return apk_file_name


@pytest.fixture(scope='session')
def get_apk_version(repo_root, get_apk_name):
    apk_file_name = get_apk_name
    apk_version = apk_file_name.split(' ')[0].split('_')[1][1:]
    return apk_version
