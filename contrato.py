import time
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class incio_tenat(unittest.TestCase):

    def    setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")

    

    def test_login_user_1(self):
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

        # ingresar al menú de uentas 

        select_menu_Account = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        )
        select_menu_Account.click()

        select_contract = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[1]/a"
        )
        select_contract.click()
        time.sleep(5)

        # Limpiar filtro que viene por default 
        
        select_filter = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-contracts/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/span"
        )
        select_filter.click()
        time.sleep(3)

        uncheck_filter = driver.find_element_by_xpath(
            "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-tag-container/div/div/div[7]/app-tag/div/div/i"
        )
        uncheck_filter.click()
        time.sleep(3)

        # aplicar un nuevo filtro

        select_new_filter = driver.find_element_by_xpath(
            "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[1]/div/div"
        )
        select_new_filter.click()
        time.sleep(3)

        select_campaign = driver.find_element_by_xpath(
            "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[2]/div/div"
        )
        select_campaign.click()
        time.sleep(3)

        apply_filter = driver.find_element_by_xpath(
            "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        )
        apply_filter.click()
        time.sleep(5)

        selet_list_contract = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-contracts/app-responsive-table-multiple-items/div/table/tbody/tr[2]/td[2]/app-column-percentage/div/div[1]"
        )
        selet_list_contract.click()
        time.sleep(3)

        # validar tutilo del detalle 
        element = self.driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span')

        # Obtener el texto del elemento
        text_obtained = element.text
        
        # Validar el texto
        text_expected = "MIS CONTRATOS"
        self.assertEqual(text_obtained, text_expected)

        ##Imprimir la respuesta en consola
        print("El titulo de la pantalla es:", text_obtained)

        # validar numero de contrato 
        element = self.driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[1]/div[1]/div/span")

        number_obtained = element.text
        number_expected = "Contrato 120945"
        self.assertEqual(number_obtained, number_expected)
        print("El numero de contrato es:", number_obtained)

        # validar produto 
        element = self.driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[1]/div[2]/div[2]/div[2]/span[2]')

        # Obtener el texto del elemento
        text_obtained = element.text
        
        # Validar el texto
        text_expected = "De Soja"
        self.assertEqual(text_obtained, text_expected)

        ##Imprimir la respuesta en consola
        print("El tipo de producto es:", text_obtained)


        # Validar kilos pactados 

        element = self.driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[2]/div/span")

        number_obtained = element.text
        number_expected = "De 100,00 Tn Pactados"
        self.assertEqual(number_obtained, number_expected)
        print("La cantidad de tn pactados es:", number_obtained)



        # validar la cantidad de toneladas del contrato 
        element = self.driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[1]/div[2]/div[2]/div[2]/span[1]")

        number_obtained = element.text
        number_expected = "100,00 Tn"
        self.assertEqual(number_obtained, number_expected)
        print("La cantidad  de producto es:", number_obtained)

        # validar aplicadas
        element = self.driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[2]/app-card-with-grafic/div/div/swiper/div/div[1]/div[1]/div/div[2]/span[1]")

        number_obtained = element.text
        number_expected = "0,00 Tn"
        self.assertEqual(number_obtained, number_expected)
        print("La cantidad  de aplicadas es:", number_obtained)

        # validar fijadas
        element = self.driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[2]/app-card-with-grafic/div/div/swiper/div/div[1]/div[2]/div/div[2]/span[1]")

        number_obtained = element.text
        number_expected = "100,00 Tn"
        self.assertEqual(number_obtained, number_expected)
        print("La cantidad  de fijadas es:", number_obtained)

        # descargar archivo

        download_button = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/app-header-for-responsive-table/div/div/div[2]/div/div/app-download-button/div/button[2]"
        )
        download_button.click()
        time.sleep(2)

        select_files = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/app-header-for-responsive-table/div/div/div[2]/div/div/app-download-button/div/ul/li[1]/a"
        )
        select_files.click()
        time.sleep(5)

  
        
        
        go_out_pag = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        )
        go_out_pag.click()
        time.sleep(5)












    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'reporte_contrato'))
   