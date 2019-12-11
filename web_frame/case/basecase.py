# -*- coding:utf-8 -*-
# Author : zhuke
# Data : 2019/12/11 14:46

import unittest
from selenium import webdriver
from model import driver
class BaseCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=driver.getchrome()
        self.driver.maximize_window()


    def tearDown(self) -> None:
        self.driver.quit()