import unittest
import xmlrunner
import time
from Elements import find_and_click_element, find_and_click_element_selector, find_elements, validate_chain_text_xpaht, validate_text_by_text, validate_text_visible
from loginhelper import LoginHelper
from startSession import StartSession




class contrato_tenant(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_contrato_tenant(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

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

        cleam_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[1]/button"
        find_elements(self.driver,cleam_filter )
        time.sleep(3)

        # aplicar un nuevo filtro soja cosecha 2122 desde 02/02/2021 hasta 28/05/2021 estado cumplidos

        select_product_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[1]/div/img"
        find_elements(self.driver,select_product_filter )
        time.sleep(3)

        select_campaign = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[3]/div/div"
        find_elements(self.driver, select_campaign )
        time.sleep(3)

        select_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        find_elements(self.driver, select_filter )
        time.sleep(2)

        arrow_filter1 = "body > div > div.flatpickr-months > div > div > div > span.arrowDown"
        amount_click1 = 3
        find_and_click_element_selector(self.driver, arrow_filter1, amount_click1)

        arrow_filter2 = "/html/body/div/div[1]/span[1]"
        amount_click2 = 8
        find_and_click_element(self.driver, arrow_filter2, amount_click2)

        select_date1 = "/html/body/div/div[2]/div/div[2]/div/span[2]"
        find_elements(self.driver, select_date1 )

        arrow_filter3 = "/html/body/div/div[1]/span[2]"
        amount_click3 = 3
        find_and_click_element(self.driver, arrow_filter3, amount_click3)

        select_date2 = "/html/body/div/div[2]/div/div[2]/div/span[33]"
        find_elements(self.driver, select_date2 )

        apply_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver, apply_filter )
        time.sleep(5)


         # Validar el texto
        
        text_expected = "Estado De Mis Contratos"
        validate_text_by_text(self.driver, text_expected)
        
        #ingresar al detalle de segundo contrato del listado
        selet_list_contract = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-contracts/app-responsive-table-multiple-items/div/table/tbody/tr[2]/td[1]/app-contract/div/div[2]/div[2]/div[2]"
        find_elements(self.driver, selet_list_contract )
        time.sleep(3)

        

        # validar numero de contrato 
        element1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[1]/div[1]/div/span"
        number_expected = "Contrato 108435"
        validate_text_visible(self.driver, element1, number_expected)

        # validar produto 
        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[1]/div[2]/div[2]/div[2]/span[2]'
        text_expected = "De Soja"
        validate_text_visible(self.driver, element2, text_expected)


        # Validar kilos pactados 

        
        amount_kilos = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[2]/div/span"
        amount_kilos_expected = ["200,00 Tn", "De 2000,00 QQ Pactados", "De 200.000,00 Kg Pactados"]
        validate_chain_text_xpaht(self.driver, amount_kilos, amount_kilos_expected)
      


        # validar la cantidad de toneladas del contrato 
        amount_product = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[1]/div[2]/div[2]/div[2]/span[1]"
        amount_product_expected = ["200,00 Tn", "2000,00 QQ", "200.000,00 Kg"]
        validate_chain_text_xpaht(self.driver, amount_product, amount_product_expected)

        # validar aplicadas
        applied_contract = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[2]/app-card-with-grafic/div/div/swiper/div/div[1]/div[1]/div/div[2]/span[1]"
        applied_contract_expected = ["200,00 Tn", "2000,00 QQ", "200.000,00 Kg"]
        validate_chain_text_xpaht(self.driver, applied_contract, applied_contract_expected)

        # validar fijadas
        fixed_contract = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[2]/app-card-with-grafic/div/div/swiper/div/div[1]/div[2]/div/div[2]/span[1]"
        fixed_contract_expected = ["200,00 Tn", "2000,00 QQ", "200.000,00 Kg"]
        validate_chain_text_xpaht(self.driver, fixed_contract, fixed_contract_expected)

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
  test_suite = unittest.TestLoader().loadTestsFromTestCase(contrato_tenant)
  runner = xmlrunner.XMLTestRunner(output='reportCuentaContratos')
  runner.run(test_suite)
   