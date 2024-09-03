import unittest
import time
import xmlrunner
from Elements import display_and_do_click, find_elements,  find_send_element,  validate_text
from LoginSample import LoginSample
from startSession import StartSession


class confi_registro_cliente(unittest.TestCase):


    def    setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_record_client(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()
        

       

        select_settings = '/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[10]/a/span'
        find_elements(self.driver,select_settings )
        time.sleep(2)


        select_requests = '/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[10]/div/ul/li[5]/a'
        display_and_do_click(self.driver,select_requests )
        time.sleep(2)


        ## validar titulo 
        title_page = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-customers/div/app-responsive-table-multiple-items/div/div/span"
        value_expected = "Clientes"
        validate_text(self.driver, title_page, value_expected  )

        # validar buscador locar 

        insert_client1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-customers/div/div/div/div/div/input"
        send_client1 = "G P AGRO S.A"
        find_send_element(self.driver,  insert_client1, send_client1 )
        time.sleep(2)

        select_option1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-customers/div/div/div/div/div/span'
        find_elements(self.driver,select_option1 )
        time.sleep(5)


        insert_client2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-customers/div/div/div/div/div/input"
        send_client2 = "5 B S.A."
        find_send_element(self.driver,  insert_client2, send_client2 )
        time.sleep(2)

        select_option2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-customers/div/div/div/div/div/span'
        find_elements(self.driver,select_option2 )
        time.sleep(5)

        select_detail_client = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-customers/div/app-responsive-table-multiple-items/div/table/tbody/tr/td[1]/div/p[1]'
        find_elements(self.driver,select_detail_client )
        time.sleep(2)

        #Validar datos del cliente 

        title_detalil1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-customer/div/app-detail-customer-table/section/div/h2[1]"
        value_expected = "DATOS GENERALES"
        validate_text(self.driver,title_detalil1, value_expected  )

        business_name = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-customer/div/app-detail-customer-table/section/div/div[1]/div[1]/strong/div"
        value_expected = "RAZON SOCIAL"
        validate_text(self.driver,business_name, value_expected  )

        value_business_name = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-customer/div/app-detail-customer-table/section/div/div[1]/div[1]/div"
        value_expected = "5 B S.A."
        validate_text(self.driver,value_business_name, value_expected  )

        munber_cuit = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-customer/div/app-detail-customer-table/section/div/div[1]/div[3]/strong/div"
        value_expected = "CUIT"
        validate_text(self.driver,munber_cuit, value_expected  )

        value_munber_cuit = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-customer/div/app-detail-customer-table/section/div/div[1]/div[3]/div"
        value_expected = "30-71227027-2"
        validate_text(self.driver,value_munber_cuit, value_expected  )

        number_phone = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-customer/div/app-detail-customer-table/section/div/div[2]/div[1]/strong/div"
        value_expected = "CELULAR"
        validate_text(self.driver,number_phone, value_expected  )

        value_number_phone = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-customer/div/app-detail-customer-table/section/div/div[2]/div[1]/div"
        value_expected = "03406 - 480479 / 15645641"
        validate_text(self.driver,value_number_phone, value_expected  )

        title_detalil2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-customer/div/app-detail-customer-table/section/div/h2[2]"
        value_expected = "DATOS EXTRA"
        validate_text(self.driver,title_detalil2, value_expected  )

        Businessman = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-customer/div/app-detail-customer-table/section/div/div[3]/div[3]/strong/div"
        value_expected = "COMERCIAL"
        validate_text(self.driver,Businessman, value_expected  )

        value_Businessman = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-customer/div/app-detail-customer-table/section/div/div[3]/div[3]/div"
        value_expected = "CORDOBA, RAMIRO"
        validate_text(self.driver,value_Businessman, value_expected  )

        account_client = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-customer/div/app-detail-customer-table/section/div/div[5]/div[1]/strong/div"
        value_expected = "CUENTA"
        validate_text(self.driver,account_client, value_expected  )

        value_account_client = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-customer/div/app-detail-customer-table/section/div/div[5]/div[1]/div"
        value_expected = "(2903) - 5 B S.A."
        validate_text(self.driver,value_account_client, value_expected  )


        print("Test finalizado con éxito")


       

    
    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(confi_registro_cliente)
  runner = xmlrunner.XMLTestRunner(output='reportconfi_registro_cliente')
  runner.run(test_suite)