import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner


class Granos_test_tenant(unittest.TestCase):


    def    setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")


    def test_login_user(self):
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


        select_tenant = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[8]/div/div/img')
        select_tenant.click()

        select_granos = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span')
        select_granos.click()



        select_fijaciones = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[1]/a')
        select_fijaciones.click()


        ## validar que estamos en la solapa fijaciones habilitadas 
        elemento = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/ul/li[1]/a')
        valor = elemento.text 
        valor_esperado = "Fijaciones Habilitadas"
        if valor == valor_esperado:
           print("Nos encontramos en la solapa Fijaciones Habilitadas")
        else:
           print("no estamos ubicados en la solapa Fijaciones Habilitadas") 

        input_cuenta = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/div/div[1]/app-bindings-enabled-list/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/div/div/div[2]/input")  
        input_cuenta.send_keys("484")

        wait = WebDriverWait(driver, 10)  
        account = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/div/div[1]/app-bindings-enabled-list/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[5]/span"))) 
        account.click()
        time.sleep(5)

       

        select_rublo1 = driver.find_element_by_xpath('/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[1]/div/div')
        select_rublo1.click()
        time.sleep(2)

        select_rublo2 = driver.find_element_by_xpath('/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[2]/div/img')
        select_rublo2.click()
        time.sleep(2)

        select_campaña = driver.find_element_by_xpath('/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[3]/div/div')
        select_campaña.click()
        time.sleep(2)

        select_button = driver.find_element_by_xpath('/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button')
        select_button.click()
        time.sleep(3)
    
    
    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'reporte_inicio'))
        