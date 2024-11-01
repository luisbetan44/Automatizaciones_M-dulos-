import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_elements, validate_character_numeric_element,  validate_text
from loginhelper import LoginHelper
from startSession import StartSession


class HomeSaldoCuentHoyV2(unittest.TestCase):
   def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

   def test_start_tenantV2(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")
        time.sleep(3)

        
       
       ## validar si el texto es visible para el usuario 
        page_hello = '//p[text()=" Buen día JUAN DEMO! "]'
        text_expected = "Buen día JUAN DEMO!"
        validate_text(self.driver, page_hello, text_expected  )

        
     ##validar primer cuadrante en pesos 
       
        titlle_value1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[1]/app-balance-v2/div/div[1]/div[1]"
        value_expected1 = "PESOS (ARS)"
        validate_text(self.driver, titlle_value1, value_expected1)
     
        titlle_value2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[1]/app-balance-v2/div/div[1]/div[2]"
        value_expected2 = "Total"
        validate_text(self.driver, titlle_value2, value_expected2)
        
        element1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[1]/app-balance-v2/div/div[1]/div[3]'
        validate_character_numeric_element(self.driver, element1  )
        
        titlle_value3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[1]/app-balance-v2/div/div[2]/div[1]/div/div[1]"
        value_expected3 = "Total Vencido"
        validate_text(self.driver, titlle_value3, value_expected3)

        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[1]/app-balance-v2/div/div[2]/div[1]/div/div[2]'
        validate_character_numeric_element(self.driver, element2  )

        titlle_value4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[1]/app-balance-v2/div/div[2]/div[2]/div/div[1]"
        value_expected4 = "Total a vencer"
        validate_text(self.driver, titlle_value4, value_expected4)
   
        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[1]/app-balance-v2/div/div[2]/div[2]/div/div[2]'
        validate_character_numeric_element(self.driver, element2  )

        # validar segundo cuadrente en dolares

        titlle_value1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[2]/app-balance-v2/div/div[1]/div[1]"
        value_expected1 = "DÓLARES (USD)"
        validate_text(self.driver, titlle_value1, value_expected1)
     
        titlle_value2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[2]/app-balance-v2/div/div[1]/div[2]"
        value_expected2 = "Total"
        validate_text(self.driver, titlle_value2, value_expected2)
        
        element1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[2]/app-balance-v2/div/div[1]/div[3]'
        validate_character_numeric_element(self.driver, element1  )
        
        titlle_value3 = "//html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[2]/app-balance-v2/div/div[2]/div[1]/div/div[1]"
        value_expected3 = "Total Vencido"
        validate_text(self.driver, titlle_value3, value_expected3)

        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[2]/app-balance-v2/div/div[2]/div[1]/div/div[2]'
        validate_character_numeric_element(self.driver, element2  )

        titlle_value4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[2]/app-balance-v2/div/div[2]/div[2]/div/div[1]"
        value_expected4 = "Total a vencer"
        validate_text(self.driver, titlle_value4, value_expected4)
   
        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[2]/app-balance-v2/div/div[2]/div[2]/div/div[2]'
        validate_character_numeric_element(self.driver, element2  )

        # validar redireccionamientos a cta cte 

        select_button_redirect_ARS = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[1]/app-balance-v2/div/div[3]/div/button/div/div[1]"
        find_elements(self.driver, select_button_redirect_ARS)

        select_return_home = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[2]/a/span"
        find_elements(self.driver, select_return_home)

        select_button_redirect_USD = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[1]/app-balance-v2-container/div/div[2]/div[2]/app-balance-v2/div/div[3]/div/button/div/div[1]"
        find_elements(self.driver, select_button_redirect_USD)

        select_return_home = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[2]/a/span"
        find_elements(self.driver, select_return_home)

        
      
     
        
   def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(HomeSaldoCuentHoyV2)
  runner = xmlrunner.XMLTestRunner(output='HomeSaldoCuentHoyV2')
  runner.run(test_suite)
        
   
