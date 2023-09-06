import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC





class insumos_productos(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")

    def test_cuenta_entregas(self):
        driver = self.driver
        usermane = driver.find_element_by_id("email")
        usermane.send_keys("comercialgd@silohub.ag")
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

        ## seleccionar menú de insumos 

        select_supplies = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[4]/a/span")
        select_supplies.click()

        select_menu_product = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[4]/div/ul/li[1]/a")
        select_menu_product.click()


        ## validar titulo de la pagina 

        title_page_product = driver.find_element_by_xpath("//span[text()='PRODUCTOS']")
        title_page_product_expected = title_page_product.text
        title_page_product_obtained = "PRODUCTOS"

        if title_page_product_expected == title_page_product_obtained:
            print("El titulo de la pagina es: ", title_page_product_obtained)

        else:
            print("El titulo de la pagina no es correcto")

        ## agregar producto

        add_product = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[1]/input")
        add_product.send_keys("aceite")
        add_product.send_keys(Keys.ENTER)

        ## seleccionar condicion 

        select_condition = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[2]/app-supplies-price-list-selector/button")
        select_condition.click()

        ## ingresar fecha en busqueda

        insert_cleam = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[2]/app-supplies-price-list-selector/ul/input")
        insert_cleam.clear()
        time.sleep(3)
 

        insert_date = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[2]/app-supplies-price-list-selector/ul/input")))
        insert_date.send_keys("60 días")
        insert_date.send_keys(Keys.ENTER)

        ## seleccionar condición 

        type_condition_1 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[2]/app-supplies-price-list-selector/ul/div/div[89]/input")
        type_condition_1.click()

        type_condition_2 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[2]/app-supplies-price-list-selector/ul/div/div[162]/input")
        type_condition_2.click()

        

        button_search = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[3]/button/div")
        button_search.click()
        time.sleep(3)

        ## seleccionar producto del listado 
        
        select_price_product = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-product-price-list/div/app-supplies-product-price-list-item[1]/div/div/div/div[2]/button[2]/strong")
        select_price_product.click()
        time.sleep(3)

        ## agregar producto al carro 

        select_product_list = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-product-price-list/div/app-supplies-product-price-list-item[1]/div/div/app-supplies-product-price-list-item-price/div[2]/app-supplies-product-price-list-item-price-item/div/div[1]/input")
        select_product_list.click()
        time.sleep(3)

        add_button = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-product-price-list/div/app-supplies-product-price-list-item[1]/div/div/app-supplies-product-price-list-item-price/app-supplies-product-price-list-item-price-add-share-buttons/div/button[2]")
        add_button.click()
        time.sleep(3)

        ## ingresar al carrito 

        select_car = driver.find_element_by_id("shipment")
        select_car.click()
        time.sleep(3)

        ## validar titulo pantalla 






    def tearDown(self):
        self.driver.close()




if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'reporte_insumosProductos'))
   