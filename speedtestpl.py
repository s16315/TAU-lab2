import time


class SpeedTestPl:
    """
    Klasa testująca działanie strony www.speedtest.pl
    """
    def __init__(self, driver, logger):
        self.driver = driver
        self.driver.get('https://www.speedtest.pl/')
        # poprawić - self.driver.title nie działa
        self.browser = "?"
        self.logger = logger
        self.logger.info("www.speedtest.pl {} otwarcie strony".format(self.browser))

    def rodo_click(self):
        """
        Metoda umożliwiająca przejście popup-u z rodo blokującego dalszą aktywność.
        """
        self.driver.find_element_by_id('rodoClick').click()
        self.logger.info("{} www.speedtest.pl przejście popup-u RODO".format(self.browser))

    def main_menu_test(self):
        """
        Przejście w głównym menu do pozycji Moje konto
        :return:
        """
        step1 = self.driver.find_element_by_id('topmenu')
        step2 = step1.find_elements_by_tag_name('li')
        step2[2].click()
        self.logger.info(
            "{} www.speedtest.pl przejście w głównym menu do pozycji \"Moje konto\" https://www.speedtest.pl/account".format(
                self.browser))

    def main_menu_wycena(self):
        step1 = self.driver.find_element_by_id('topmenu')
        step2 = step1.find_elements_by_tag_name('li')
        step2[3].click()
        self.logger.info(
            "{} www.speedtest.pl przejście w głównym menu do pozycji \"Wycena stron\" https://www.speedtest.pl/wycena".format(
                self.browser))
        step3 = self.driver.find_element_by_id('domain')
        step3.send_keys('rykoszet.info')
        self.logger.info(
            "{} www.speedtest.pl/wycena wstawienie do formularza strony \"rykoszet.info\"".format(
                self.browser))
        step4 = self.driver.find_element_by_id('swa')
        step4.click()
        self.logger.info(
            "{} www.speedtest.pl/wycena kliknięcie w przycisk \"Rozpocznij wycenę\"".format(
                self.browser))
        time.sleep(2)

    def end_test(self):
        """
        Metoda kończąca test.
        :return:
        """
        time.sleep(1)
        self.driver.close()
        self.logger.info("{} www.speedtest.pl zamknięcie przeglądarki".format(self.browser))

    def scenario_1(self):
        self.rodo_click()
        self.main_menu_test()
        self.end_test()

    def scenario_2(self):
        self.rodo_click()
        self.main_menu_wycena()
        self.end_test()