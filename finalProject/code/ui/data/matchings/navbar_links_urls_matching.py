from config.creds import APP_PORT, APP_SERVICE
from ui.data.enums.navbar_links_names import NavbarLinksNames as Names

NavbarLinksUrlsMatching = {
    f"http://{APP_SERVICE}:{APP_PORT}/welcome/": Names.HOME,
    "https://www.python.org/": Names.PYTHON,
    "https://en.wikipedia.org/wiki/History_of_Python": Names.PYTHON_HISTORY,
    "https://flask.palletsprojects.com/en/1.1.x/#": Names.FLASK,
    "https://getfedora.org/ru/workstation/download/": Names.CENTOS,
    "https://www.wireshark.org/news/": Names.WIRESHARK_NEWS,
    "https://www.wireshark.org/#download": Names.WIRESHARK_DOWNLOAD,
    "https://hackertarget.com/tcpdump-examples/": Names.TCPDUMP_EXAMPLES
}
