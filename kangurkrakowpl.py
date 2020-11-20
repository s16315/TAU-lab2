import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Kangurkrakowpl:
    def __init__(self, driver, logger):
        self.driver = driver
        self.driver.get('http://kangur-krakow.pl')
        # poprawić - self.driver.title nie działa
        self.browser = "?"
        self.logger = logger
        self.logger.info("kangur-krakow.pl {} otwarcie strony".format(self.browser))

    def end_test(self):
        """
        Metoda kończąca test.
        :return:
        """
        time.sleep(3)
        self.driver.close()
        self.driver.quit()
        self.logger.info("kangur-krakow.pl {} zamknięcie przeglądarki".format(self.browser))

    def photo_gallery_test(self):
        step1 = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/a[9]')
        step1.click()
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[4]/div/h2'))
            WebDriverWait(self.driver, 3).until(element_present)
        except TimeoutException:
            self.logger.error("kangur-krakow.pl {} galeria zdjęć nie została wczytana w ciagu 3 sekund".format(self.browser))
            return
        self.logger.info("kangur-krakow.pl {} wczytano galerię zdjeć".format(self.browser))
        step2 = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[4]/div/div/table/tbody/tr[1]/td[1]/a')
        step2.click()
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[4]/div/div[2]/table[2]/tbody/tr[1]/td[1]/a'))
            WebDriverWait(self.driver, 3).until(element_present)
        except TimeoutException:
            self.logger.error("kangur-krakow.pl {} album zdjęć nie został wczytany w ciagu 3 sekund".format(self.browser))
            return
        self.logger.info("kangur-krakow.pl {} poprawnie wczytano album zdjeć".format(self.browser))
        step3 = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[4]/div/div[2]/table[2]/tbody/tr[1]/td[1]/a')
        step3.click()
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[4]/div/div/div[1]/a'))
            WebDriverWait(self.driver, 3).until(element_present)
        except TimeoutException:
            self.logger.error("kangur-krakow.pl {} zdjęcie nie zostało wczytane w ciagu 3 sekund".format(self.browser))
            return
        self.logger.info("kangur-krakow.pl {} poprawnie wczytano zdjecie".format(self.browser))
        step4 = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[4]/div/div/div[1]/a')
        step4.click()
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/div[1]'))
            WebDriverWait(self.driver, 3).until(element_present)
        except TimeoutException:
            self.logger.error("kangur-krakow.pl {} powiększenie zdjęcie nie zostało wczytane w ciagu 3 sekund".format(self.browser))
            return
        self.logger.info("kangur-krakow.pl {} testowanie galerii zdjęć zakończylo się sukcesem".format(self.browser))

    def results_finding_test(self):
        step1 = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/a[7]')
        step1.click()
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[4]/div/h2'))
            WebDriverWait(self.driver, 3).until(element_present)
        except TimeoutException:
            self.logger.error("kangur-krakow.pl {} podstrona z wynikami nie została wczyta w ciagu 3 sekund".format(self.browser))
            return
        self.logger.info("kangur-krakow.pl {} wczytano podstronę z wynikami".format(self.browser))
        step2 = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[4]/div/div/p[3]/strong[3]/a')
        step2.click()
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[4]/div/h2'))
            WebDriverWait(self.driver, 3).until(element_present)
        except TimeoutException:
            self.logger.error("kangur-krakow.pl {} nie wczytano podstrony z wynikami z 2019 roku w ciagu 3 sekund".format(self.browser))
            return
        self.logger.info("kangur-krakow.pl {} wczytano podstronę z wynikami z 2019 roku".format(self.browser))
        step3 = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[4]/div/div/p[11]/a[3]')
        step3.click()
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[4]/div/h2'))
            WebDriverWait(self.driver, 3).until(element_present)
        except TimeoutException:
            self.logger.error("kangur-krakow.pl {} nie wczytano podstrony z wynikami \"Beniamin\" z 2019 roku w ciagu 3 sekund".format(self.browser))
            return
        self.logger.info("kangur-krakow.pl {} test wczytywania wyników zakończył się sukcesem".format(self.browser))

    def scenario_1(self):
        self.logger.info(" *** ".format(self.browser))
        self.logger.info("kangur-krakow.pl {} scenario_1".format(self.browser))
        self.end_test()

    def scenario_2(self):
        self.logger.info(" *** ".format(self.browser))
        self.logger.info("kangur-krakow.pl {} scenario_2".format(self.browser))
        self.end_test()
