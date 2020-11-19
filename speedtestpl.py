import time


class SpeedTestPl:
    """
    Klasa testująca działanie strony www.speedtest.pl
    """
    def __init__(self, driver, logger):
        self.driver = driver
        self.driver.get('https://www.speedtest.pl/')
        self.browser = "?"
        self.logger = logger
        self.logger.info("{} www.speedtest.pl otwarcie strony".format(self.browser))

    def rodo_click(self):
        """
        Metoda umożliwiająca przejście popup-u z rodo blokującego dalszą aktywność.
        """
        self.driver.find_element_by_id('rodoClick').click()
        self.logger.info("{} www.speedtest.pl przejście popup-u RODO".format(self.browser))

    def main_menu_test(self):
        step1 = self.driver.find_element_by_id('topmenu')
        step2 = step1.find_elements_by_tag_name('li')
        self.logger.info("{} www.speedtest.pl przejście w głównym menu do pozycji logowanie".format(self.browser))
        step2[2].click()

    def end_test(self):
        """
        Metoda kończąca test.
        :return:
        """
        time.sleep(1)
        self.driver.close()
        self.logger.info("{} www.speedtest.pl zamknięcie przeglądarki".format(self.browser))