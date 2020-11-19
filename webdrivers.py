from selenium import webdriver


class WebDrivers:
    """
    Klasa dostarczająca i konfigurująca webdrivery do przeglądarek
    """

    @staticmethod
    def get_chrome():
        driver = webdriver.Chrome(executable_path='./Drivers/chromedriver.exe')
        return driver

    @staticmethod
    def get_edge():
        driver = webdriver.Edge(executable_path='./Drivers/msedgedriver.exe')
        return driver

    @staticmethod
    def get_firefox():
        driver = webdriver.Firefox(executable_path='./Drivers/geckodriver.exe')
        return driver

