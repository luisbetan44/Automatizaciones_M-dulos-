import unittest
import time
import xmlrunner
from Elements import find_elements, find_send_element,  validate_text
from LoginSample import LoginSample
from startSession import StartSession


class confi_Solicitudes(unittest.TestCase):


    def    setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_settings_User(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()
        

       

        select_settings = '/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[10]/a/span'
        find_elements(self.driver,select_settings )
        time.sleep(2)



        select_requests = '/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[10]/div/ul/li[4]/a'
        find_elements(self.driver,select_requests )
        time.sleep(5)


        ## validar titulo 
        title_page = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        value_expected = "SOLICITUDES"
        validate_text(self.driver, title_page, value_expected  )

        # validar buscador locar 

        insert_email1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-users-request/div/div[1]/div[1]/div/div[1]/input"
        send_name = "_eqc5i5q3@yopmail.com"
        find_send_element(self.driver,  insert_email1, send_name )
        time.sleep(2)

        select_option1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-users-request/div/div[1]/div[1]/div/div[1]/span'
        find_elements(self.driver,select_option1 )
        time.sleep(5)


        insert_email2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-users-request/div/div[1]/div[1]/div/div[1]/input"
        send_name = "_irnfen2a@yopmail.com"
        find_send_element(self.driver,  insert_email2, send_name )
        time.sleep(2)

        select_option2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-users-request/div/div[1]/div[1]/div/div[1]/span'
        find_elements(self.driver,select_option2 )
        time.sleep(5)

        select_button_download = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-users-request/div/div[1]/div[2]/app-button/button'
        find_elements(self.driver,select_button_download )
        time.sleep(10)

        print("Test finalizado con éxito")


       

    
    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(confi_Solicitudes)
  runner = xmlrunner.XMLTestRunner(output='reportconfi_Solicitudes')
  runner.run(test_suite)