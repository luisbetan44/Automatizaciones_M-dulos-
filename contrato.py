import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xmlrunner


class contrato_tenant(unittest.TestCase):

    def    setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver.exe")
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

        # ingresar al menú de cuentas 
        
        select_account = driver.find_element_by_css_selector("#navbar-nav > li:nth-child(5) > a > span")
        select_account.click()
        

        select_contract = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[1]/a"
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
            "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[1]/button"
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
        number_expected = "Contrato 121190"
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

        
        amount_kilos = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[2]/div/span")
        amount_kilos_obtained = amount_kilos.text
        amount_kilos_expected = ["De 900,00 QQ Pactados", "De 90,00 Tn Pactados", "De 90.000,00 Kg Pactados"]
        
        if amount_kilos_obtained in amount_kilos_expected:
            print("La cantidad de kilos pactados son:", amount_kilos_obtained)
        else:
            print("La cantidad de kilos pactados no es la correcta")
        # validar producto


        # validar la cantidad de toneladas del contrato 
        amount_product = self.driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[1]/div[2]/div[2]/div[2]/span[1]")

        amount_product_obtained = amount_product.text
        amount_product_expected = ["900,00 QQ", "90,00 Tn", "90.000,00 Kg"]
        
        if amount_product_obtained in amount_product_expected:
            print("La cantidad  de producto es:", amount_product_obtained)

        else:
            print("la cantidad de producto no es correcta")

        # validar aplicadas
        applied_contract = self.driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[2]/app-card-with-grafic/div/div/swiper/div/div[1]/div[1]/div/div[2]/span[1]")

        applied_contract_obtained = applied_contract.text
        applied_contract_expected = ["0,00 QQ","0,00 Kg","0,00 Tn"]
      
        if applied_contract_obtained in applied_contract_expected:
           print("La cantidad  de aplicadas es:", applied_contract_obtained)

        else:
            print("La cantidad aplicada no es correcta")

        # validar fijadas
        fixed_contract = self.driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[2]/app-card-with-grafic/div/div/swiper/div/div[1]/div[2]/div/div[2]/span[1]")

        fixed_contract_obtained = fixed_contract.text
        fixed_contract_expected = ["0,10 Tn","1,00 QQ","100,00 Kg"]

        if fixed_contract_obtained in fixed_contract_expected:
           print("La cantidad  de fijadas es:", fixed_contract_obtained)

        else:
            print("La cantidad fijadas no es la correcta")

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
  test_suite = unittest.TestLoader().loadTestsFromTestCase(contrato_tenant)
  runner = xmlrunner.XMLTestRunner(output='reportCuentaContratos')
  runner.run(test_suite)
   