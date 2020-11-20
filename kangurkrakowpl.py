import time

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

    def scenario_1(self):
        self.end_test()

    def scenario_2(self):
        self.end_test()