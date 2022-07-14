import pytest
import unittest
from TestCases.test_Base import Basetest
from Pages.SearchPage import SearchPage
from Config.config import TestData
class Test_001_Search(Basetest):

    def test_get_search_page_title(self):
        self.searchPage = SearchPage(self.driver)
        title=self.searchPage.get_search_page_title(TestData.search_page_title)
        assert title==TestData.search_page_title

    def test_search_Product(self):
        self.searchPage = SearchPage(self.driver)
        self.searchPage.search_Product()

if __name__=='__main__':
    unittest.main()












