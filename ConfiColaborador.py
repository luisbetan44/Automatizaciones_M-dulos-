import unittest
import time
import xmlrunner
from Elements import display_and_do_click, find_elements, find_send_element,  validate_text
from LoginSample import LoginSample
from startSession import StartSession


class confi_colaborador(unittest.TestCase):


    def    setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_record_collaborator(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()
        

       

        select_settings = '/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[10]/a/span'
        find_elements(self.driver,select_settings )
        time.sleep(2)

        select_collaborator = '/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[10]/div/ul/li[6]/a'
        display_and_do_click(self.driver,select_collaborator )
        time.sleep(2)


        ## validar titulo 
        title_page = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-collaborators/div/div/div[1]/div/div/input"
        value_expected = "COLABORADORES"
        validate_text(self.driver, title_page, value_expected  )

        # validar buscador locar 

        insert_client1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-collaborators/div/div/div[1]/div/div/input"
        send_client1 = "COMERCIAL DEMO"
        find_send_element(self.driver,  insert_client1, send_client1 )
        time.sleep(2)

        select_option1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-collaborators/div/div/div[1]/div/div/span'
        find_elements(self.driver,select_option1 )
        time.sleep(5)


        insert_client2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-collaborators/div/div/div[1]/div/div/input"
        send_client2 = "20247795767"
        find_send_element(self.driver,  insert_client2, send_client2 )
        time.sleep(2)

        select_option2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-collaborators/div/div/div[1]/div/div/span'
        find_elements(self.driver,select_option2 )
        time.sleep(5)
      
        ## ingresar al detalle del segundo colaborador 
        select_detail_client = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-collaborators/div/app-responsive-table-multiple-items/div/table/tbody/tr[2]/td[1]/div/p[2]'
        find_elements(self.driver,select_detail_client )
        time.sleep(2)

        #Validar datos del cliente 

        title_detalil1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-collaborator/div/section/div/h2[1]"
        value_expected = "DATOS GENERALES"
        validate_text(self.driver,title_detalil1, value_expected  )

        business_name = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-collaborator/div/section/div/div[1]/div[1]/strong/div"
        value_expected = "RAZON SOCIAL"
        validate_text(self.driver,business_name, value_expected  )

        value_business_name = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-collaborator/div/section/div/div[1]/div[1]/div"
        value_expected = "PRODUCTOR 90116"
        validate_text(self.driver,value_business_name, value_expected  )

        identification_number  = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-collaborator/div/section/div/div[1]/div[2]/strong/div"
        value_expected = "DNI"
        validate_text(self.driver,identification_number, value_expected  )

        value_identification_number = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-collaborator/div/section/div/div[1]/div[2]/div"
        value_expected = "24.779.576"
        validate_text(self.driver,value_identification_number, value_expected  )


        munber_cuit = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-collaborator/div/section/div/div[1]/div[3]/strong/div"
        value_expected = "CUIT"
        validate_text(self.driver,munber_cuit, value_expected  )

        value_munber_cuit = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-collaborator/div/section/div/div[1]/div[3]/div"
        value_expected = "20-24779576-7"
        validate_text(self.driver,value_munber_cuit, value_expected  )

        title_detalil2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-collaborator/div/section/div/h2[2]"
        value_expected = "DATOS DEL COLABORADOR"
        validate_text(self.driver,title_detalil2, value_expected  )

        number_file = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-collaborator/div/section/div/div[3]/div[1]/strong/div"
        value_expected = "NÚMERO DE LEGAJO"
        validate_text(self.driver,number_file, value_expected  )

        value_number_file = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-collaborator/div/section/div/div[3]/div[1]/div"
        value_expected = "90116"
        validate_text(self.driver,value_number_file, value_expected  )

        type_collaborator = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-collaborator/div/section/div/div[3]/div[2]/strong/div"
        value_expected = "TIPO DE COLABORADOR"
        validate_text(self.driver, type_collaborator, value_expected  )

        value_type_collaborator = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-collaborator/div/section/div/div[3]/div[2]/div"
        value_expected = "Colaborador"
        validate_text(self.driver,value_type_collaborator, value_expected  )

        select_to_going = '/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a'
        find_elements(self.driver, select_to_going )
        time.sleep(2)

        select_button_download = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-collaborators/div/div/div[2]/app-button/button'
        find_elements(self.driver,select_button_download )
        time.sleep(5)
      
      


        print("Test finalizado con éxito")


       

    
    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(confi_colaborador)
  runner = xmlrunner.XMLTestRunner(output='reportconfi_confi_colaborador')
  runner.run(test_suite)