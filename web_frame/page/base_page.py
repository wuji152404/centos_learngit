# -*- coding:utf-8 -*-
# Author : zhuke
# Data : 2019/12/11 16:04

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage():
    BaseURL='http://192.168.1.162/crm/index.php?m=user&a=login'
    OUTTIME=30

    def __init__(self, driver, url=BaseURL, outtime=OUTTIME):
        self.driver=driver
        #self.driver=webdriver.Chrome()
        self.url=url
        self.outtime=outtime

    def open(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.outtime)

    def find_ele(self, location):
        return self.driver.find_element(*location)
if __name__ == '__main__':
    driver=webdriver.Chrome()
    #driver.get('http://192.168.1.162/crm/index.php?m=user&a=login')
    lp=BasePage(driver)
    lp.open()
    lp.find_ele((By.NAME,'name')).send_keys('admin')