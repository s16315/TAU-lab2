import time


class SpeedTestPl:
    """
    Klasa testująca działanie strony www.speedtest.pl
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.speedtest.pl/')

    def rodo_click(self):
        """
        Metoda umożliwiająca przejście popup-u z rodo blokującego dalszą aktywność.
        """
        self.driver.find_element_by_id('rodoClick').click()

    def main_menu_test(self):
        step1 = self.driver.find_element_by_id('topmenu')
        step2 = step1.find_elements_by_tag_name('li')
        step2[2].click()

    def end_test(self):
        """
        Metoda kończąca test.
        :return:
        """
        time.sleep(1)
        self.driver.close()