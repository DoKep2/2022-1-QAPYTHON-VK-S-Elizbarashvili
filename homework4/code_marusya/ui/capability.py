import os


def capability_select(get_apk_name):
    capability = {"platformName": "Android",
                  "platformVersion": "8.1",
                  "automationName": "Appium",
                  "autoGrantPermissions": True,
                  "appPackage": "ru.mail.search.electroscope",
                  "app": os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                      f'..{os.sep}stuff{os.sep}{get_apk_name}')
                                         ),
                  "orientation": "PORTRAIT"
                  }
    return capability
