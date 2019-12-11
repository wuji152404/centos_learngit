# -*- coding:utf-8 -*-
# Author : zhuke
# Data : 2019/12/11 16:41
import ddt

from case.basecase import BaseCase
from page.login_page import LoginPage
from selenium.webdriver.common.by import By
from data import users
from model import driver
import ddt


@ddt.ddt
class LoginCase(BaseCase):
    # @ddt.data(*[{'username':'admin','password':'admin'}])
    # @ddt.data(*users.users)
    @ddt.data(*driver.get_table('user', 'Sheet1'))
    @ddt.unpack
    def test_login_case(self, username, password):
        lp=LoginPage(self.driver)
        lp.open()
        lp.login_submit(username, password)
        a=self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a').text
        self.assertIn('admin', a)
