APP_PACKAGE = "ru.auroraos.CallApiDBus"
APPIUM_SERVER_URL = "http://localhost:4723"

CAPABILITIES = {
    "automationName": "Aurora",
    "platformName": "Aurora",
    "platformVersion": "2.2",
    "newCommandTimeout": 86400,
    "appPackage": APP_PACKAGE,
    "deviceName": "host.docker.internal",
    "autoLaunch": True,
    "appiumInspector": False,
}
