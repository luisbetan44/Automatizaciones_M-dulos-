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

        select_menu_Account = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        )
        select_menu_Account.click()

        select_deliveries = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[3]/a"
        )
        select_deliveries.click()
        time.sleep(3)



        #   Validar titulo de la pantalla 

        title_menu = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/div/span")
        title_obtained = title_menu.text
        tille_expected = "Mis Ventas"
        self.assertEqual(title_obtained, tille_expected)

        if title_obtained:
            print("El titulo de la pagina es:", title_menu.text)


        else:
              print("el titulo de la pagina no se enconto ")  


        # selecionar botón del filtro
        selct_filter = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/span")
        selct_filter.click()
        time.sleep(2)
 


        # limpiar  filtro 

        clean_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[1]/button")
        clean_filter.click()
        time.sleep(2)

        # aplicar filtro

        apply_product_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[1]/div/img")
        apply_product_filter.click()
        time.sleep(2)

        apply_Campaign_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[3]/div/div")
        apply_Campaign_filter.click()
        time.sleep(2)

        apply_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button")
        apply_filter.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'reporte_ventas'))
