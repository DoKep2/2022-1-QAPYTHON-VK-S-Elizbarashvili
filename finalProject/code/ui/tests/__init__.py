from config.creds import APP_SERVICE, APP_PORT

REGISTER_PAGE_URL = f"http://{APP_SERVICE}:{APP_PORT}/reg"
MAIN_PAGE_URL = f"http://{APP_SERVICE}:{APP_PORT}/welcome/"
LOGIN_PAGE_URL = f"http://{APP_SERVICE}:{APP_PORT}/login"
