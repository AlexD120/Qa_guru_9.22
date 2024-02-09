import os

from qa_guru_922 import utils

# context = os.getenv('context', 'bstack')
# run_on_bstack = os.getenv('run_on_bstack', 'false').lower() == 'true'
remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723/wd/hub')
deviceName = os.getenv('deviceName')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
app = os.getenv('app', './org.wikipedia-50466.apk')
runs_on_bstack = app.startswith('bs://')
if runs_on_bstack:
    remote_url = 'http://hub.browserstack.com/wd/hub'
bstack_userName = os.getenv('bstack_userName', 'bsuser_1EpbYw')
bstack_accessKey = os.getenv('bstack_accessKey', 'LapqcrC4yPBU7sUkaxys')


def to_driver_options():
    from appium.options.android import UiAutomator2Options

    options = UiAutomator2Options()

    if deviceName:
        options.set_capability('deviceName', deviceName)

    if appWaitActivity:
        options.set_capability('appWaitActivity', appWaitActivity)

    options.set_capability(
        'app',
        (
            app
            if (app.startswith('/') or runs_on_bstack)
            else utils.file.abs_path_from_project(app)
        ),
    )

    if runs_on_bstack:
        options.set_capability('platformVersion', '9.0')
        options.set_capability(
            'bstack:options',
            {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',
                'userName': bstack_userName,
                'accessKey': bstack_accessKey,
            },
        )

    return options
