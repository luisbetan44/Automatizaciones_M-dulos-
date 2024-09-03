import time
from findElements import find_element_by_css_selector, find_element_by_xpath, find_element_by_id

class LoginHelper:
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

    def search_and_select_account(self, account_number):
        input_element = find_element_by_id(self.driver, "search-options")
        input_element.send_keys(account_number)

        element_to_click = find_element_by_css_selector(self.driver, "#search-dropdown > app-accounts-list > ngx-simplebar > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div.dropdown-sub-item.accounts-numbers")
        self.driver.execute_script("arguments[0].style.display = 'block';", element_to_click)
        element_to_click.click()
        time.sleep(5)