import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC
import re
import xmlrunner



class reporteIsumoPendRetirar(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")

    def test_reports_entregas_ventas(self):
        driver = self.driver
        username = driver.find_element_by_id("email")
        username.send_keys("admingd@silohub.ag")
        username.send_keys(Keys.ENTER)
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
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        )
        select_menu_Account.click()


        # ingresar al submenú de reportes 

        select_menu_reports = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[6]/a")
        select_menu_reports.click()
        time.sleep(3)

        ## aplicar filtro 

        select_filter_button = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-reports/div/app-header-for-responsive-table/div/div/div[2]/div/div/app-filter-button/button/div/span")
        select_filter_button.click()
        time.sleep(2)

        select_option_supplies = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-radio-button-list/div/app-radio[3]/div/input")
        select_option_supplies.click()
        time.sleep(2)

        apply_filter_supplies = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button")
        apply_filter_supplies.click()
        time.sleep(3)

        # validar titulo de la pantalla 

        title_page_supplies = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/div/div/div[1]")
        title_page_supplies_obtained = title_page_supplies.text
        title_page_supplies_expected = "Insumos Pendientes de Retirar"
        if title_page_supplies_expected == title_page_supplies_obtained:
            print("El título de la pantalla es : ", title_page_supplies_obtained)

        else:
            print("No se encontro el título se la pantalla ")

        # validar numero de comprobante de primer  movimiento 

        list_movements1 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/table/tbody/tr[1]/td[1]/span/span") 

        list_movements1_obtained = list_movements1.text

        if isinstance(list_movements1_obtained, str):
            print("El numero del  primer comprobante es un string: ",list_movements1_obtained)

        else: 
            print("El numero del  primer comprobante no es un string: ",list_movements1_obtained)

        # validar descripcion del articulo del primer movimiento

        description_article1 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/table/tbody/tr[1]/td[2]/span/span") 

        description_article1_obtained = description_article1.text

        if isinstance(description_article1_obtained, str):
            print("La  descripción del primer  artículo  es un string: ",description_article1_obtained)

        else: 
            print("La  descripción del artículo primer  no es un string: ", description_article1_obtained)

        # validar monto del primer movimiento pemdiente 

        pending_amount1 = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/table/tbody/tr[1]/td[3]/span/span")
        pending_amount1_obtained = pending_amount1.text 
        if re.search(r'\d', pending_amount1_obtained):  
          print('El saldo pemdiente del primer movimiento  es un carácter numérico.', pending_amount1_obtained)
        else:
          print('El saldo pemdiente del primer movimiento no es un carácter numérico.')


        # validar numero de comprobante de segundo movimiento 

        list_movements2 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/table/tbody/tr[2]/td[1]/span/span") 

        list_movements2_obtained = list_movements2.text

        if isinstance(list_movements2_obtained, str):
            print("El numero del segundo comprobante es un string: ",list_movements2_obtained)

        else: 
            print("El numero del segundo  comprobante no es un string: ",list_movements2_obtained)

        # validar descripcion del articulo del segundo  movimiento
        
        description_article2 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/table/tbody/tr[2]/td[2]/span/span") 

        description_article2_obtained = description_article2.text

        if isinstance(description_article2_obtained, str):
            print("La  descripción del segundo  artículo  es un string: ",description_article2_obtained)

        else: 
            print("La  descripción del artículo primer  no es un string: ", description_article2_obtained)

         # validar monto del segundo movimiento pemdiente 

        pending_amount2 = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/table/tbody/tr[2]/td[3]/span/span")
        pending_amount2_obtained = pending_amount2.text 
        if re.search(r'\d', pending_amount2_obtained):  
          print('El saldo pemdiente del segundo movimiento  es un carácter numérico.', pending_amount2_obtained)
        else:
          print('El saldo pemdiente del segundo movimiento no es un carácter numérico.')



        # seleccionar movimientos del listado y descargar 

        select_first_movements = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/table/tbody/tr[1]/th/input")
        select_first_movements.click()

        select_second_movements = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/table/tbody/tr[2]/th/input")
        select_second_movements.click()

        # descargar movimientos seleccionados 

        select_button_download1 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]")
        select_button_download1.click()
        time.sleep(2)

        download_option_Excel = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a")
        download_option_Excel.click()
        time.sleep(3)

        select_button_download2 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]")
        select_button_download2.click()
        time.sleep(2)

        download_option_PDF = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a")
        download_option_PDF.click()
        time.sleep(3)




    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(reporteIsumoPendRetirar)
  runner = xmlrunner.XMLTestRunner(output='reportInsuPendRetirar')
  runner.run(test_suite)
        