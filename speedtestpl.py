import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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
        self.logger.info("www.speedtest.pl {} przejście popup-u RODO".format(self.browser))

    def main_menu_test(self):
        """
        Przejście w głównym menu do pozycji Moje konto
        :return:
        """
        step1 = self.driver.find_element_by_id('topmenu')
        step2 = step1.find_elements_by_tag_name('li')
        step2[2].click()
        self.logger.info(
            "www.speedtest.pl {} przejście w głównym menu do pozycji \"Moje konto\" https://www.speedtest.pl/account".format(
                self.browser))

    def main_menu_wycena(self):
        step1 = self.driver.find_element_by_id('topmenu')
        step2 = step1.find_elements_by_tag_name('li')
        step2[3].click()
        self.logger.info(
            "www.speedtest.pl {} przejście w głównym menu do pozycji \"Wycena stron\" https://www.speedtest.pl/wycena".format(
                self.browser))
        #time.sleep(1)
        try:
            element_present = EC.presence_of_element_located((By.ID, 'domain'))
            WebDriverWait(self.driver, 3).until(element_present)
        except TimeoutException:
            self.logger.error("www.speedtest.pl/wycena {} nie można odnaleźć elementu o id {}".format(
                self.browser, 'domain'))
            return

        step3 = self.driver.find_element_by_id('domain')
        self.logger.error("www.speedtest.pl/wycena {} znaleziono element o id {}".format(
            self.browser, 'domain'))
        step3.send_keys('rykoszet.info')
        self.logger.info(
            "www.speedtest.pl/wycena {} wstawienie do formularza strony \"rykoszet.info\"".format(
                self.browser))
        step4 = self.driver.find_element_by_id('swa')
        step4.click()
        self.logger.info(
            "www.speedtest.pl/wycena {} kliknięcie w przycisk \"Rozpocznij wycenę\"".format(
                self.browser))
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[1]/div[2]/div[5]/div[1]/div[1]'))
            WebDriverWait(self.driver, 3).until(element_present)
        except TimeoutException:
            self.logger.error("www.speedtest.pl/wycena {} wycena nie została wczytana".format(
                self.browser, 'domain'))
            return
        self.logger.info(
            "www.speedtest.pl/wycena {} wycena została poprawnie wczytana".format(
                self.browser))

    def end_test(self):
        """
        Metoda kończąca test.
        :return:
        """
        time.sleep(1)
        self.driver.close()
        self.driver.quit()
        self.logger.info("www.speedtest.pl {} zamknięcie przeglądarki".format(self.browser))

    def scenario_1(self):
        self.rodo_click()
        self.main_menu_test()
        self.end_test()

    def scenario_2(self):
        self.rodo_click()
        self.main_menu_wycena()
        self.end_test()

    def scenario_2_test(self):
        self.rodo_click()
        self.main_menu_wycena()
