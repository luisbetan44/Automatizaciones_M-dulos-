import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
import xmlrunner
from selenium.webdriver.support import expected_conditions as EC
import re





class cuenta_ctacte_aplicada(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver.exe")
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
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        )
        select_menu_contrat.click()

        ## seleccionar cuenta corriente

        select_account = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[4]/a"
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

        select_arrow_3 = driver.find_element_by_xpath(
            "/html/body/div/div[1]/span[1]"
        )
        select_arrow_3.click()
        time.sleep(2)

        select_date_1 = driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[2]/div/span[8]"
        )
        select_date_1.click()
        time.sleep(2)

        select_arrow_3 = driver.find_element_by_xpath(
            "/html/body/div/div[1]/span[2]"
        )
        select_arrow_3.click()
        time.sleep(2)

        select_date_2 = driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[2]/div/span[33]"
        )
        select_date_2.click()
        time.sleep(2)

        apply_button_filter = driver.find_element_by_xpath(
            "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        )
        apply_button_filter.click()
        time.sleep(2)

        ## validar titulo de pantalla cuenta corriente aplicada 

        title_account = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        )

        title_account_expected = title_account.text
        title_account_obtained = "CUENTA CORRIENTE APLICADA"
        self.assertEqual(title_account_obtained,title_account_expected)
        print("El titulo de la pantalla es: ",title_account_obtained)

        ## validar totalizadores 


        

        total_to_pay = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[1]/div/div[1]/app-totalizer/div/div[1]/div[2]/div[2]')
        valor_1 = total_to_pay.text 
        if re.search(r'\d', valor_1):  
          print('El total a pagar  es un carácter numérico.', valor_1)
        else:
          print('El total a pagar no es un carácter numérico.')
   

        ## validar saldos

        balance_ars = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[1]/div/div[2]/app-totalizer/div/div/div[2]/div[2]/span[1]"
        )
        valor_2 = balance_ars.text 
        if re.search(r'\d', valor_2):  
          print('El saldo ARS  es un carácter numérico.', valor_2)
        else:
          print('El saldo ARS no es un carácter numérico.')
   


        balance_usd = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[1]/div/div[3]/app-totalizer/div/div/div[2]/div[2]/span[1]"
        )

        valor_3 = balance_usd.text 
        if re.search(r'\d', valor_3):  
          print('El saldo USD  es un carácter numérico.', valor_3)
        else:
          print('El saldo USD no es un carácter numérico.')
   

        ## seleccionar movimientos del lisatos 

        movements_list_1 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-responsive-table/div/table/tbody/tr[2]/th/input"
        )
        movements_list_1.click()

        

        
      
       ## seleccionar botón descargar  

        select_button = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        )
        select_button.click()

        ## descargar Excel 

        download_Excel = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a"
        )

        download_Excel.click()
        time.sleep(3)

        ## descargar PDF 

        select_button = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        )
        select_button.click()

        ## descargar Excel 

        download_PDF = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        )

        download_PDF.click()
        time.sleep(3)


        ## ingresar al detalle 

        detail_movements = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-responsive-table/div/table/tbody/tr[2]/td[2]/span/span"
        )
        detail_movements.click()
        time.sleep(3)

        ## validar titulo pantalla 
        title_detail = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        )

        title_detail_expected = title_detail.text
        title_detail_obtained = "CUENTA CORRIENTE"
        self.assertEqual(title_detail_expected,title_detail_obtained)   
        print("El titulo de la pantalla es: ", title_detail_obtained)

        ## validar datos del detalle 

        number_movements = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[1]/div") 

        number_movements_obtained = number_movements.text

        if isinstance(number_movements_obtained, str):
            print("El numero del  comprobante es un string: ",number_movements_obtained)

        else: 
            print("El numero del  comprobante no es un string: ")



        balance_movements = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[2]/div/div[2]/div[1]"
        )
        balance_movements_ebtained = balance_movements.text
        if isinstance(balance_movements_ebtained, str):
            print("El monto total en el detalle es un string: ",balance_movements_ebtained)

        else: 
            print("El monto total en el detalle no es un string: ")

        settlement = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/div/div/div/div[2]/div[2]/div[2]"
        )

        settlement_obtained = settlement.text
        if isinstance(settlement_obtained, str):
            print("El tipo de cambio en el detalle es un string: ",settlement_obtained)

        else: 
            print("El tipo de cambio en el detalle no es un string: ")

        ## Seleccionar salida al listado 

        go_out_list = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        )
        go_out_list.click()
        time.sleep(3)



        

















    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(cuenta_ctacte_aplicada)
  runner = xmlrunner.XMLTestRunner(output='reportCtacteAplicada')
  runner.run(test_suite)