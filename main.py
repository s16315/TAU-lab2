

from selenium import webdriver
from speedtestpl import SpeedTestPl

speedTest = SpeedTestPl(webdriver.Chrome(executable_path='./Drivers/chromedriver.exe'))
speedTest.rodo_click()
speedTest.main_menu_test()
speedTest.end_test()
