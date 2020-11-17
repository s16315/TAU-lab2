import time

from selenium import webdriver


class MenuTest:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.speedtest.pl/')

    def rodo_click(self):
        self.driver.find_element_by_id('rodoClick').click()

    def main_menu_test(self):
        step1 = self.driver.find_element_by_id('topmenu')
        step2 = step1.find_elements_by_tag_name('li')
        step2[2].click()

    def end_test(self):
        time.sleep(4)
        self.driver.close()


speedTest = MenuTest(webdriver.Chrome(executable_path='./../chromedriver.exe'))
speedTest.rodo_click()
speedTest.main_menu_test()
speedTest.end_test()
