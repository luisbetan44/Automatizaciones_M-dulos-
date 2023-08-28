from selenium  import webdriver
import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class precio_granos(unittest.TestCase):

    def     setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")


    def test_precio_granos(self):
        driver = self.driver
        username = driver.find_element_by_id("email")
        username.send_keys("admingd@silohub.ag")
        username.send_keys(Keys.ENTER)
        time.sleep(3)
        
        passwordUser = driver.find_element_by_id("password")
        passwordUser.send_keys("G@viglio123")
        passwordUser.send_keys(Keys.ENTER)
        time.sleep(3)

        insertButton = driver.find_element_by_xpath("/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button")
        insertButton.send_keys(Keys.ENTER) 
        time.sleep(3)

      ## seleccionar el tenant 
        selectTenant = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[8]/div/div/img")
        selectTenant.click()
        time.sleep(3)

     # localiza el input y envia el número de la cuenta 
        input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-options")))
        input_element.send_keys('1023')
      
       #selecciona el elemento oculto y crea un botón para hacer click sobre el 
        element_to_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search-dropdown > app-accounts-list > ngx-simplebar > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div.dropdown-sub-item.accounts-numbers")))
        driver.execute_script("arguments[0].style.display = 'block';", element_to_click)
        element_to_click.click()
        time.sleep(3)
    
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= 'reportes', report_name='reporte_precioGranos'))
        


