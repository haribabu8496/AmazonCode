from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    def __init__(self, driver):
        self.driver=driver


    def get_title(self,title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title