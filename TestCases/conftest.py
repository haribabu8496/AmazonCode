import pytest
from selenium import webdriver
from Config.config import TestData

@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    if request.param=="chrome":
        driver=webdriver.Chrome(executable_path=TestData.chrome_path)
        driver.set_window_size(1920, 1080)
    request.cls.driver=driver
    yield
    driver.close()





