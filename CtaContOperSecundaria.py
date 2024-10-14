import unittest
import xmlrunner
import time
from Elements import find_and_click_element, find_and_click_element_selector, find_elements, validate_chain_text_xpaht,validate_text_by_text, validate_text_visible
from loginhelper import LoginHelper
from startSession import StartSession




class contrato_operSecundarias(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_contratc_oparSecondary(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("150000")

        # ingresar al menú de cuentas 

        select_menu_Account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver,select_menu_Account )

        

        select_contract = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[1]/a"
        find_elements(self.driver,select_contract )
        time.sleep(5)

        # Limpiar filtro que viene por default 
        
        select_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-contracts/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/span"
        find_elements(self.driver,select_filter )
        time.sleep(3)

        select_secondary = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-radio-button-list/div/app-radio[2]/div/input"
        find_elements(self.driver,select_secondary )
        time.sleep(3)

        # aplicar un nuevo filtro soja 2122 rango 10/12/2021 al 16/12/2021

        select_product_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[1]/div/div"
        find_elements(self.driver,select_product_filter )
        time.sleep(2)

        select_campaign = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[2]/div/div"
        find_elements(self.driver, select_campaign )
        time.sleep(2)

        select_date = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        find_elements(self.driver, select_date )
        time.sleep(2)

        arrow_filter1 = "body > div > div.flatpickr-months > div > div > div > span.arrowDown"
        amount_click1 = 2
        find_and_click_element_selector(self.driver, arrow_filter1, amount_click1)
        time.sleep(2)

        arrow_filter2 = "/html/body/div/div[1]/span[1]"
        amount_click2 = 10
        find_and_click_element(self.driver, arrow_filter2, amount_click2)
        time.sleep(2)

        select_date1 = "/html/body/div/div[2]/div/div[2]/div/span[12]"
        find_elements(self.driver, select_date1 )
        time.sleep(2)

        select_date2 = "/html/body/div/div[2]/div/div[2]/div/span[18]"
        find_elements(self.driver, select_date2 )
        time.sleep(2)

        apply_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver, apply_filter )
        time.sleep(5)

         # Validar el texto
        
        text_expected = "Estado De Mis Contratos"
        validate_text_by_text(self.driver, text_expected)
        
        #ingresar al detalle de segundo contrato del listado
        selet_list_contract = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-contracts/app-responsive-table-multiple-items/div/table/tbody/tr/td[1]/app-contract/div/div[2]/div[2]/div[2]"
        find_elements(self.driver, selet_list_contract )
        time.sleep(3)

        

        # validar numero de contrato 
        element1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div/div[1]/div/span"
        number_expected = "Contrato 2070"
        validate_text_visible(self.driver, element1, number_expected)

        # validar produto 
        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div/div[2]/div[2]/div[2]/span[2]'
        text_expected = "De Soja"
        validate_text_visible(self.driver, element2, text_expected)
        
        # validar campaña

        contract_campaign = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-detail-contract-secondary-table/div/div/div[1]/div[5]/div[2]/div[2]"
        contract_campaign_expected = "2122"
        validate_text_visible(self.driver, contract_campaign, contract_campaign_expected)

        # Validar kilos contrato

        
        amount_kilos = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div/div[2]/div[2]/div[2]/span[1]"
        amount_kilos_expected = ["0,00 Tn", "0,01 QQ", "1,00 Kg"]
        validate_chain_text_xpaht(self.driver, amount_kilos, amount_kilos_expected)
      


        # validar la cantidad de toneladas del contrato 
       

        

        # descargar archivo

        download_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/app-header-for-responsive-table/div/div/div[2]/div/div/app-download-button/div/button[2]"
        find_elements(self.driver, download_button )
        time.sleep(2)

        select_files = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/app-header-for-responsive-table/div/div/div[2]/div/div/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver, select_files )
        time.sleep(5)

    
        go_out_pag = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver, go_out_pag )
        time.sleep(5)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(contrato_operSecundarias)
  runner = xmlrunner.XMLTestRunner(output='reportCuentaContratos')
  runner.run(test_suite)
   