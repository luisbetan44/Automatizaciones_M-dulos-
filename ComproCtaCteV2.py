import unittest
import xmlrunner
import time
from Elements import  find_and_click_element, find_elements,validate_text
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession




class comprobanteCtaCteV2(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_comprobante_ctacteV2(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")



        # ingresar al menú de cuentas 

        select_menu_Account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver, select_menu_Account)

        select_older_tab = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[4]/a"
        find_elements(self.driver, select_older_tab)

        
        # validar el título de la pagina 

        title_vouchers = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-others/div/div/app-tab-receipts/app-receipts/div/span"
        title_vouchers_expected = "Mis Comprobantes"
        validate_text(self.driver, title_vouchers, title_vouchers_expected)
        time.sleep(2)

       ## seleccionar filtro de contrato

        select_filter_button1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-others/div/div/app-tab-receipts/app-receipts/app-header-for-responsive-table/div/div/div[2]/div/div/app-filter-button/button/div/span"
        find_elements(self.driver, select_filter_button1)
        time.sleep(2)
       
       # aplicar filtro con rango de fecha 29/12/2023 al 26/01/2024
       


        insert_date_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        find_elements(self.driver, insert_date_filter)
        time.sleep(2)

        select_arrow_filter1 = "/html/body/div/div[1]/span[1]"
        amount_click1 = 10 
        find_and_click_element(self.driver, select_arrow_filter1, amount_click1)
        time.sleep(2)

         ##Espera hasta que el checkbox esté visible y activo
      
        select_date_filter1 = "/html/body/div/div[2]/div/div[2]/div/span[33]"
        find_elements(self.driver, select_date_filter1)

        select_arrow_filter2 = "/html/body/div/div[1]/span[2]"
        amount_click2 = 1
        find_and_click_element(self.driver, select_arrow_filter2, amount_click2)
        time.sleep(2)

        select_date_filter2 = "/html/body/div/div[2]/div/div[2]/div/span[26]"
        find_elements(self.driver, select_date_filter2)


        apply_filter_button = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver, apply_filter_button)
        time.sleep(2)


        
        ## seleccionar contrato 


        select_contract_list1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-others/div/div/app-tab-receipts/app-receipts/app-responsive-table-multiple-items/div/table/tbody/tr[1]/th/input"
        find_elements(self.driver, select_contract_list1)
        time.sleep(2)
        ## validar numero de contrato

        contract_number1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-others/div/div/app-tab-receipts/app-receipts/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td/div/div[2]/div[2]/div[3]/span"
        validate_character_string_element(self.driver, contract_number1 )

        select_contract_list2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-others/div/div/app-tab-receipts/app-receipts/app-responsive-table-multiple-items/div/table/tbody/tr[2]/th/input"
        find_elements(self.driver, select_contract_list2)
        time.sleep(2)
        ## validar numero de contrato

        contract_number2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-others/div/div/app-tab-receipts/app-receipts/app-responsive-table-multiple-items/div/table/tbody/tr[2]/td/div/div[2]/div[2]/div[3]/span"
        validate_character_string_element(self.driver, contract_number2 )


        ## seleccionar boton descargar 

        download_button1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-others/div/div/app-tab-receipts/app-receipts/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver,  download_button1)
        time.sleep(2)
        
        select_type_document1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-others/div/div/app-tab-receipts/app-receipts/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver,  select_type_document1)
        time.sleep(2)

        
    
    

    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(comprobanteCtaCteV2)
  runner = xmlrunner.XMLTestRunner(output='reportcomprobanteCtaCteV2')
  runner.run(test_suite)