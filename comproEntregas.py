import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC





class comprobantes_Entregas(unittest.TestCase):
    
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
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        )
        select_menu_Account.click()

        select_menu_vouchers = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[5]/a")
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

        ## seleccionar boton de filtro

        select_button_filter = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div")
        select_button_filter.click()

        ## seleccionar checkbox de entregas dentro del filtro y aplicar filtro

        wait = WebDriverWait(driver, 10)
        select_filter_deliveries = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Entregas"]')))
        select_filter_deliveries.click()

        apply_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button")
        apply_filter.click()
        time.sleep(2)

        ## seleccionar movimientos 

        movenments_list1 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-responsive-table-multiple-items/div/table/tbody/tr[1]/th/input")
        movenments_list1.click()

        movenments_list2 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-responsive-table-multiple-items/div/table/tbody/tr[2]/th/input")
        movenments_list2.click()

        movenments_list3 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-responsive-table-multiple-items/div/table/tbody/tr[3]/th/input")
        movenments_list3.click()


        ## VALIDAR NÚMEROS DE COMPROBANTES A DESCARGAR 

             
        number_vouchers1_expected = "TK 0001 00102949"
 
# Utiliza XPath para encontrar el elemento <span> por su texto
        xpath = f'//span[text()="{number_vouchers1_expected}"]'
        number_vouchers1 = driver.find_element(By.XPATH, xpath)

# Obtén el texto del elemento <span>
        number_vouchers1_obtained = number_vouchers1.text

        if number_vouchers1_expected == number_vouchers1_obtained:
           print("El número del primer comprobante es:", number_vouchers1_obtained)
        else:
            print("El comprobante no fue encontrado:")
        
        number_vouchers2 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-responsive-table-multiple-items/div/table/tbody/tr[2]/td/div/div[2]/div[2]/div[3]/span")
        number_vouchers2_obtained = number_vouchers2.text
        number_vouchers2_expected = "TK 0001 00102884"

        if number_vouchers2_expected == number_vouchers2_obtained:
            print("El número del segundo comprobante es: ",number_vouchers2_obtained)

        else: 
             print("El comprobante no fue encontrado: ")

        number_vouchers3 = driver.find_element_by_css_selector('span.f-size-14.fw-semibold')
        number_vouchers3_obtained = number_vouchers3.text
        number_vouchers3_expected = "TK 0001 00102791"

        if number_vouchers3_expected == number_vouchers3_obtained:
            print("El número del tercer comprobante es: ",number_vouchers3_obtained)

        else: 
             print("El comprobante no fue encontrado: ")




        ## seleccionar boton de descarga 

        download_movenments = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]")
        download_movenments.click()

        select_type_download = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-receipts/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a")
        select_type_download.click()




    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'comproEntregas'))

 