import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC





class comprobantes_contratos(unittest.TestCase):
    
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

        select_menu_Account = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        )
        select_menu_Account.click()

        select_menu_vouchers = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[5]/a")
        select_menu_vouchers.click()
        time.sleep(2)

        # validar el título de la pagina 

        title_vouchers = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span")
        title_vouchers_obtained = title_vouchers.text
        title_vouchers_expected = "COMPROBANTES"

        if title_vouchers_expected == title_vouchers_obtained:
            print("El título de la pagina es: ",title_vouchers_obtained)

        else: 
             print("El título de la pagina no es el correcto: ")


       ## seleccionar filtro de contrato

        select_filter_button1 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/span")
        select_filter_button1.click()


        wait = WebDriverWait(driver, 10)
        select_contract_filter1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Contratos"]')))
        select_contract_filter1.click()


        insert_date_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]")
        insert_date_filter.click()
        time.sleep(2)

        select_arrow_filter1 = driver.find_element_by_xpath("/html/body/div/div[1]/span[1]")
        select_arrow_filter1.click()
        time.sleep(2)

         ##Espera hasta que el checkbox esté visible y activo
        wait = WebDriverWait(driver, 10)
        select_date_filter1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='flatpickr-day' and text()='2']")))
        select_date_filter1.click()

        select_arrow_filter2 = driver.find_element_by_xpath("/html/body/div/div[1]/span[2]")
        select_arrow_filter2.click()
        time.sleep(2)

        wait = WebDriverWait(driver, 10)
        select_date_filter2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='flatpickr-day' and text()='13']")))
        select_date_filter2.click()


        apply_filter_button = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button")
        apply_filter_button.click()
        time.sleep(3)


        ## validar titulo de la pantalla 
        title_page_vouchers = driver.find_element_by_xpath("//span[@class='fw-bold' and text()='Mis Comprobantes']")
        title_page_vouchers_obtained = title_page_vouchers.text
        title_page_vouchers_expected = "Mis Comprobantes"

        if title_page_vouchers_expected == title_page_vouchers_obtained:
            print("El título de la pagina es: ",title_page_vouchers_obtained)

        else: 
             print("El título de la pagina no es el correcto: ")

        ## seleccionar contrato 


        select_contract_list1 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-responsive-table-multiple-items/div/table/tbody/tr[1]/th/input")
        select_contract_list1.click()

        ## validar numero de contrato

        contract_number1 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td/div/div[2]/div[2]/div[3]/span")
        contract_number1_obtained = contract_number1.text
        contract_number1_expected = "VT 0001 00121040"
        if contract_number1_expected == contract_number1_obtained:
            print("El numero del contrato seleccionado es: ", contract_number1_obtained)

        else:
            print("El numero de contrato no es correcto")

        select_contract_list2 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-responsive-table-multiple-items/div/table/tbody/tr[2]/th/input")
        select_contract_list2.click()

        ## validar numero de contrato

        contract_number2 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-responsive-table-multiple-items/div/table/tbody/tr[2]/td/div/div[2]/div[2]/div[3]/span")
        contract_number2_obtained = contract_number2.text
        contract_number2_expected = "VT 0001 00121041"
        if contract_number2_expected == contract_number2_obtained:
            print("El numero del contrato seleccionado es: ", contract_number2_obtained)

        else:
            print("El numero de contrato no es correcto")


        ## seleccionar boton descargar 

        download_button1 = driver.find_element_by_xpath("//button[@type='button'and @class='btn dropdown-toggle dropdown-toggle-split shadow-none btn-primary']")
        download_button1.click()

        select_type_document1 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a")
        select_type_document1.click()

        ## aceptar popup

        select_popup1 = driver.find_element_by_xpath("/html/body/div/div/div[6]/button[1]")
        select_popup1.click()

        ## validar respuesta del pop up 
        messager_popup = driver.find_element_by_xpath("/html/body/div/div/h2")
        messager_popup_obtained =  messager_popup.text
        messager_popup_expected = "El comprobante seleccionado no se encuentra para su descarga"

        if  messager_popup_expected ==  messager_popup_obtained:
            print("El mensaje de la descarga  es: ", messager_popup_obtained)

        else: 
             print("El sistema no esta arrojando mensaje de la descarga: ")


        ## salir de la pantalla  
        
        select_header_arrow = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a")
        select_header_arrow.click()


        








    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'comprobantes'))
