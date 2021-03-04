from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            return webdriver.Chrome(ChromeDriverManager().install())
        elif browser == "opera":
            return webdriver.Opera(executable_path=OperaDriverManager().install())
        elif browser == "firefox":
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == "edge":
            return webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())