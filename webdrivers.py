from selenium import webdriver


class WebDrivers:
    """

    """

#    def __init__(self):
#        self.driver = webdriver.Chrome(executable_path='./Drivers/chromedriver.exe.exe')

    def get_chrome(self):
        self.driver = webdriver.Chrome(executable_path='./Drivers/chromedriver.exe')
        return self.driver

    def get_edge(self):
        self.driver = webdriver.Edge(executable_path='./Drivers/msedgedriver.exe')
        return self.driver

    def get_firefox(self):
        self.driver = webdriver.Firefox(executable_path='./Drivers/geckodriver.exe')
        return self.driver
