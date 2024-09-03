from telnetlib import EC
import unittest
import xmlrunner
import time
from Elements import displace_element, find_and_click_element, find_elements, find_send_element,  search_and_displace_account,select_option_click, validate_text, validate_text_by_text
from LoginSample import LoginSample
from startSession import StartSession




class granos_contratos(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_granos_contratos(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()

        select_grain = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span"
        find_elements(self.driver,select_grain)
        time.sleep(2)

        select_confir_sales = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[2]/a"
        find_elements(self.driver,select_confir_sales)
        time.sleep(2)

        # validar titulo de la pantalla
        
        
        text_expected = "CONTRATOS"
        validate_text_by_text(self.driver, text_expected)


        # cargar opción de tipo de confirmación
      
        button_dropdown = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[2]/div[2]/ng-select/div/span"
        option_desired = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[2]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[8]/span"
        select_option_click(self.driver, button_dropdown, option_desired)
        time.sleep(2)

        #seleccionar cuenta en el buscador 
       
        located_element = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[3]/div[2]/div/app-customer-searcher/ng-select/div/div/div[2]/input"
        select_input = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[3]/div[2]/div/app-customer-searcher/ng-select/div/div/div[2]/input"
        account_number = "1023"
        search_and_displace_account(self.driver, account_number, select_input, located_element )

        select_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[3]/div[2]/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        find_elements(self.driver,select_account)
        time.sleep(2)

        
        # selecionar especie

        button_dopdown2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[4]/div[2]/ng-select/div/span"
        option_desired2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[4]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[14]/span"
        select_option_click(self.driver, button_dopdown2, option_desired2, )

        

        # Cargar coseha
       
        button_dopdown3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[5]/div[2]/ng-select/div/span"
        option_desired3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[5]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        select_option_click(self.driver, button_dopdown3, option_desired3, )

        

        # ingresar cantidad
        
        insert_amount = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/app-input-for-long-form[1]/div/div[2]/div/input"
        send_amount = "300"
        find_send_element(self.driver,insert_amount,send_amount )

        # seleccionar modena

        button_dopdown4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[6]/div[2]/ng-select/div/span"
        option_desired4 =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[6]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        select_option_click(self.driver, button_dopdown4, option_desired4, ) 

        

        # ingresar precio

        insert_price = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/app-input-for-long-form[2]/div/div[2]/div/input"
        send_price = "3000"
        find_send_element(self.driver, insert_price, send_price )

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # seleccionar pizarra

        button_dopdown5 ="/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[7]/div[2]/ng-select/div/span"
        option_desired5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[7]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[6]/span"
        select_option_click(self.driver, button_dopdown5, option_desired5  )
        
        
        # codigo estandar 
        button_dopdown6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[8]/div[2]/ng-select/div/span"
        option_desired6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[8]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div/span"
        select_option_click(self.driver, button_dopdown6, option_desired6 )
       

        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # seleccionar fecha de pago

        select_date = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[2]/div[2]/app-date-picker/div/input[2]"
        displace_element(self.driver, select_date)

        select_arrow = "/html/body/div[1]/div[1]/span[2]"
        clicks = 1
        find_and_click_element(self.driver, select_arrow, clicks)

        insert_date = "/html/body/div[1]/div[2]/div/div[2]/div/span[30]"
        find_elements(self.driver, insert_date)
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
   
        # seleccionar la fecha desde 01/11/2024 al 30/11/2024

        select_date = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[1]/div[2]/app-date-picker/div/input[2]"
        displace_element(self.driver, select_date)
        time.sleep(2)

        select_arrow2 = "/html/body/div[5]/div[1]/span[2]"
        clicks = 6
        find_and_click_element(self.driver, select_arrow2, clicks) 
        time.sleep(2)

        select_calendar1 = "/html/body/div[5]/div[2]/div/div[2]/div/span[5]"
        find_elements(self.driver, select_calendar1)
        time.sleep(1)

        select_calendar2 = "/html/body/div[5]/div[2]/div/div[2]/div/span[34]"
        find_elements(self.driver, select_calendar2)
        time.sleep(2)

       
         # insertar campo plata
        
        select_input = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/app-search-selector/ng-select"
        find_elements(self.driver, select_input)
        time.sleep(2)
       
        select_option = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[2]/span"
        find_elements(self.driver, select_option)
        time.sleep(2)
       

        # insertar procedenia
        
        select_input = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/app-search-selector/ng-select/div/div/div[2]/input"
        find_elements(self.driver, select_input)
        time.sleep(2)
       
        select_option = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[3]/span"
        find_elements(self.driver, select_option)
        time.sleep(2)
        
        
        

        # insertar destino
      
        select_input = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/app-search-selector/ng-select/div/div/div[2]/input"
        find_elements(self.driver, select_input)
        time.sleep(2)
       
        select_option = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[6]/span"
        find_elements(self.driver, select_option)
        time.sleep(2)
        
     

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        #insertar fecha de fijacióm Tdc 16/05/2024

        select_date = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[4]/div[2]/app-date-picker/div/input[2]"
        displace_element(self.driver, select_date)
        time.sleep(2)

        select_arrow3 = "/html/body/div[2]/div[1]/span[2]"
        clicks = 1
        find_and_click_element(self.driver, select_arrow3, clicks) 
        time.sleep(2)

        select_calendar3 = "/html/body/div[2]/div[2]/div/div[2]/div/span[18]"
        find_elements(self.driver, select_calendar3)
        time.sleep(1)

        

        # seleccionar el botón de continuar

        select_button_continue = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[2]/app-button[2]/button"
        find_elements(self.driver, select_button_continue)
        time.sleep(2)

        select_button_confirm = "/html/body/div[6]/div/div[6]/button[3]"
        find_elements(self.driver, select_button_confirm)
        time.sleep(2)

        # validar el mensaje de respuesta

      
        element_text_8 = "/html/body/div[6]/div/h2"
        text_expected_8 = "Confirmación de venta generada con éxito."
        validate_text(self.driver, element_text_8, text_expected_8 )
        time.sleep(2)

        select_finish = "/html/body/div[6]/div/div[6]/button[1]"
        find_elements(self.driver, select_finish)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(granos_contratos)
  runner = xmlrunner.XMLTestRunner(output='reportGranosContratos')
  runner.run(test_suite)