

from speedtestpl import SpeedTestPl
from webdrivers import WebDrivers

webDrivers = WebDrivers()
speedTest = SpeedTestPl(webDrivers.get_chrome())
speedTest.rodo_click()
speedTest.main_menu_test()
speedTest.end_test()

speedTest = SpeedTestPl(webDrivers.get_edge())
speedTest.rodo_click()
speedTest.main_menu_test()
speedTest.end_test()

speedTest = SpeedTestPl(webDrivers.get_firefox())
speedTest.rodo_click()
speedTest.main_menu_test()
speedTest.end_test()
