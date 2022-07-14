import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from Pages.Base import Base

from Config.config import TestData
from selenium.webdriver.common.by import By
class SearchPage(Base):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.baseUrl)

    def get_search_page_title(self,title):
        return self.get_title(title)

    def search_Product(self):


        self.Iphone=self.driver.find_element(By.ID,"twotabsearchtextbox")
        self.Iphone.send_keys("Iphone")

        Search_key=self.Iphone.get_attribute('value')
        time.sleep(5)
        self.driver.find_element(By.ID,"twotabsearchtextbox").send_keys(Keys.ENTER)

        self.mobiles=self.driver.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")


        MobileDetails=""

        for x in range(len(self.mobiles)):
            print(self.mobiles[0].text)
            MobileDetails=self.mobiles[0].text
            break

        Info=MobileDetails.split(",")
        value1=Info[0]
        value2=Info[1:3]

        list_data={'name':value1,'specifications':value2}
        Items={Search_key:list_data}
        print(Items)

















