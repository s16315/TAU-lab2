from logger import Logger
from speedtestpl import SpeedTestPl
from webdrivers import WebDrivers

logger = Logger()
webDrivers = WebDrivers()
speedTest = SpeedTestPl(webDrivers.get_chrome(), logger)
speedTest.rodo_click()
speedTest.main_menu_test()
speedTest.end_test()

speedTest = SpeedTestPl(webDrivers.get_edge(), logger)
speedTest.rodo_click()
speedTest.main_menu_test()
speedTest.end_test()

speedTest = SpeedTestPl(webDrivers.get_firefox(), logger)
speedTest.rodo_click()
speedTest.main_menu_test()
speedTest.end_test()
