import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC





class cuenta_entregas(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")

    def test_cuenta_entregas(self):
        driver = self.driver
        usermane = driver.find_element_by_id("email")
        usermane.send_keys("admingd@silohub.ag")
        usermane.send_keys(Keys.ENTER)
        time.sleep(3)


        passworUser = driver.find_element_by_id("password")
        passworUser.send_keys("G@viglio123")
        passworUser.send_keys(Keys.ENTER)
        time.sleep(3)

        insertButton = driver.find_element_by_xpath("/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button")
        insertButton.click()
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

        # ingresar al menú de cuentas 

        select_menu_contrat = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        )
        select_menu_contrat.click()

        ## seleccionar cuenta corriente

        select_account = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[4]/a"
        )
        select_account.click()
        time.sleep(3)

        ## selecionar botón del filtro

        select_filter = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/span"
        )
        select_filter.click()
        time.sleep(2)

          ## aplicar filtro de rubros 

        apply_filter_1 = driver.find_element_by_xpath(
            "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-agricultural-category-container/div/app-agricultural-category-button[1]/div/img"
        )
        apply_filter_1.click()
        time.sleep(2)

        apply_filter_2 = driver.find_element_by_xpath(
            "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-agricultural-category-container/div/app-agricultural-category-button[2]/div/img"
        )
        apply_filter_2.click()
        time.sleep(2)

        apply_filter_3 = driver.find_element_by_xpath(
            "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-agricultural-category-container/div/app-agricultural-category-button[3]/div/img"
        )
        apply_filter_3.click()
        time.sleep(2)

        ## seleccionar rango de fecha

        select_field_date = driver.find_element_by_xpath(
            "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        )
        select_field_date.click()
        time.sleep(2)

        select_arrow_1 = driver.find_element_by_xpath(
            "/html/body/div/div[1]/span[1]"
        )
        select_arrow_1.click()
        time.sleep(2)

        select_arrow_2 = driver.find_element_by_xpath(
            "/html/body/div/div[1]/span[1]"
        )
        select_arrow_2.click()
        time.sleep(2)

        select_date_1 = driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[2]/div/span[4]"
        )
        select_date_1.click()
        time.sleep(2)

        select_arrow_3 = driver.find_element_by_xpath(
            "/html/body/div/div[1]/span[2]"
        )
        select_arrow_3.click()
        time.sleep(2)

        select_date_2 = driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[2]/div/span[26]"
        )
        select_date_2.click()
        time.sleep(2)

        apply_button_filter = driver.find_element_by_xpath(
            "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        )
        apply_button_filter.click()
        time.sleep(2)

        ## validar titulo de pantalla cuenta corriente aplicada 








    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'reporte_ctacte_aplicada'))
