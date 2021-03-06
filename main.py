from kangurkrakowpl import Kangurkrakowpl
from logger import Logger
from speedtestpl import SpeedTestPl
from webdrivers import WebDrivers

logger = Logger()
webDrivers = WebDrivers()

speedTest = SpeedTestPl(webDrivers.get_edge(), logger)
speedTest.scenario_1()

speedTest = SpeedTestPl(webDrivers.get_firefox(), logger)
speedTest.scenario_1()

speedTest = SpeedTestPl(webDrivers.get_chrome(), logger)
speedTest.scenario_1()

speedTest = SpeedTestPl(webDrivers.get_edge(), logger)
speedTest.scenario_2()

speedTest = SpeedTestPl(webDrivers.get_firefox(), logger)
speedTest.scenario_2()

speedTest = SpeedTestPl(webDrivers.get_chrome(), logger)
speedTest.scenario_2()

kangur = Kangurkrakowpl(webDrivers.get_edge(), logger)
kangur.scenario_1()

kangur = Kangurkrakowpl(webDrivers.get_firefox(), logger)
kangur.scenario_1()

kangur = Kangurkrakowpl(webDrivers.get_chrome(), logger)
kangur.scenario_1()

kangur = Kangurkrakowpl(webDrivers.get_edge(), logger)
kangur.scenario_2()

kangur = Kangurkrakowpl(webDrivers.get_firefox(), logger)
kangur.scenario_2()

kangur = Kangurkrakowpl(webDrivers.get_chrome(), logger)
kangur.scenario_2()