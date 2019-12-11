# -*- coding:utf-8 -*-
# Author : zhuke
# Data : 2019/12/11 16:17
from page.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    username_locator=(By.NAME, 'name')
    password_locator=(By.NAME, 'password')
    button_locator=(By.NAME, 'submit')

    def username(self, username):
        self.find_ele(self.username_locator).clear()
        self.find_ele(self.username_locator).send_keys(username)

    def password(self, password):
        password_input=self.find_ele(self.password_locator)
        password_input.clear()
        password_input.send_keys(password)

    def login_submit(self, username, password):
        self.username(username)
        self.password(password)
        self.find_ele(self.button_locator).click()
