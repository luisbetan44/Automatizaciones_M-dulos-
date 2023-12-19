from  selenium.webdriver.common.keys import Keys
import time
from findElements import  find_element_by_xpath, find_element_by_id

class LoginSample:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user = find_element_by_id(self.driver, "email")  # asegúrate de pasar self.driver
        user.send_keys(username)
        passuser = find_element_by_id(self.driver, "password")  # también aquí
        passuser.send_keys(password)
        button = find_element_by_xpath(self.driver, "/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button")
        button.click()
        time.sleep(3)

    def select_tenant(self):
        select_tenant = find_element_by_xpath(self.driver, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[8]/div/div/img")
        select_tenant.click()

        time.sleep(3)