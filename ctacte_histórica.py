import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC





class cuenta_ctacte_historica(unittest.TestCase):
    
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
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        )
        select_menu_contrat.click()

        ## seleccionar cuenta corriente

        select_account = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[4]/a"
        )
        select_account.click()
        time.sleep(3)

        ## seleccionar solapa cta cte historica 

        select_account_history = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/ul/li[2]/a")
        select_account_history.click()

        ## selecionar botón del filtro

        select_filter = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/span"
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

        ## seleccionar filtro ordenado por 

        older_by_expiration = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-radio-button-list[1]/div/app-radio[2]/div/input")
        older_by_expiration.click()

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
            "/html/body/div/div[2]/div/div[2]/div/span[26]"
        )
        select_date_2.click()
        time.sleep(2)

        apply_button_filter = driver.find_element_by_xpath(
            "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        )
        apply_button_filter.click()
        time.sleep(3)

        ## validar titulo de pantalla cuenta corriente aplicada 

        title_account = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        )

        title_account_expected = title_account.text
        title_account_obtained = "CUENTA CORRIENTE"
        self.assertEqual(title_account_obtained,title_account_expected)
        print("El titulo de la pantalla es: ",title_account_obtained)

        ## validar totalizadores 



        balance_ars = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[1]/div/div[1]/app-totalizer/div/div/div[2]/div[2]/span[1]"
        )

        balance_ars_expected = balance_ars.text
        balance_ars_obtained = "93.514.277,69"
        self.assertEqual(balance_ars_expected,balance_ars_obtained)
        print("El saldo en pesos es: ", balance_ars_obtained)


        balance_usd = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[1]/div/div[2]/app-totalizer/div/div/div[2]/div[2]/span[1]"
        )

        balance_usd_expected = balance_usd.text
        balance_usd_obtained = "-247.538,76"
        self.assertEqual(balance_usd_expected,balance_usd_obtained)
        print("El saldo en dólares es: ", balance_usd_obtained)

        ## seleccionar movimientos del lisatos 

        movements_list_1 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-responsive-table/div/table/tbody/tr[2]/th/input"
        )
        movements_list_1.click()

        movements_list_2 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-responsive-table/div/table/tbody/tr[3]/th/input"
        )
        movements_list_2.click()

        movements_list_3 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-responsive-table/div/table/tbody/tr[4]/th/input"
        )
        movements_list_3.click()

        movements_list_4 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-responsive-table/div/table/tbody/tr[5]/th/input"
        )
        movements_list_4.click()
      
       ## seleccionar botón descargar  

        select_button = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        )
        select_button.click()

        ## descargar Excel 

        download_Excel = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a"
        )

        download_Excel.click()
        time.sleep(3)

        ## descargar PDF 

        select_button = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        )
        select_button.click()

        ## descargar Excel 

        download_PDF = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        )

        download_PDF.click()
        time.sleep(3)


        ## ingresar al detalle 

        detail_movements = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-responsive-table/div/table/tbody/tr[2]/td[2]/span/span"
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

        number_movements = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[1]/div"
        )

        number_movements_expected = number_movements.text
        number_movements_obtained = "Movimiento LC 3302 11350799"
        self.assertEqual(number_movements_expected,number_movements_obtained)
        print("El numero del movimiento es: ", number_movements_obtained)


        balance_movements = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[2]/div/div[2]/div[1]"
        )

        balance_movements_expected = balance_movements.text
        balance_movements_obtained = "+ ARS 17.701.650,00"
        self.assertEqual(balance_movements_expected,balance_movements_obtained)
        print("El saldo del movimiento es: ", balance_movements_obtained)

        settlement = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[2]/div/div[2]/div[2]"
        )

        settlement_expected = settlement.text
        settlement_obtained = "Liq.1116C SOJA 2122 30000 Kgs. 100,00%"
        self.assertEqual(settlement_expected,settlement_obtained)
        print("El numero de liquidación es: ", settlement_obtained)

        ## Seleccionar salida al listado 

        go_out_list = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        )
        go_out_list.click()
        time.sleep(3)



        

















    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'reporte_ctacte_histórica'))
