
import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import validate_character_numeric_element,  validate_text
from loginhelper import LoginHelper
from startSession import StartSession


class HomeTenant(unittest.TestCase):
   def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

   def test_start_tenant(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")
        time.sleep(3)

        
       
       ## validar si el texto es visible para el usuario 
        page_hello = '//p[text()=" Buen día JUAN DEMO! "]'
        text_expected = "Buen día JUAN DEMO!"
        validate_text(self.driver, page_hello, text_expected  )

        
     ##validar totalizadores vencidos a hoy 
       
        titlle_value1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[1]/app-number-values-card/div/div/div/div[1]/div/p"
        value_expected1 = "Vencido a hoy"
        validate_text(self.driver, titlle_value1, value_expected1)
     
        titlle_value2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[1]/app-number-values-card/div/div/div/div[2]/div/p"
        value_expected2 = "ars"
        validate_text(self.driver, titlle_value2, value_expected2)
        
        element1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[1]/app-number-values-card/div/div/div/div[3]/div/h4/span'
        validate_character_numeric_element(self.driver, element1  )
        
        titlle_value3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[2]/app-number-values-card/div/div/div/div[1]/div/p"
        value_expected3 = "Vencido a hoy"
        validate_text(self.driver, titlle_value3, value_expected3)

        titlle_value4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[2]/app-number-values-card/div/div/div/div[2]/div/p"
        value_expected4 = "usd"
        validate_text(self.driver, titlle_value4, value_expected4)
   
        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[2]/app-number-values-card/div/div/div/div[3]/div/h4/span'
        validate_character_numeric_element(self.driver, element2  )

        ##validar totalizadores  a vencer
        titlle_value5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[3]/app-number-values-card/div/div/div/div[1]/div/p"
        value_expected5 = "A Vencer"
        validate_text(self.driver, titlle_value5, value_expected5)

        titlle_value6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[3]/app-number-values-card/div/div/div/div[2]/div/p"
        value_expected6 = "ars"
        validate_text(self.driver, titlle_value6, value_expected6)  

        element3 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[3]/app-number-values-card/div/div/div/div[3]/div/h4/span'
        validate_character_numeric_element(self.driver, element3  )
        
        titlle_value7 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[4]/app-number-values-card/div/div/div/div[1]/div/p"
        value_expected7 = "A Vencer"
        validate_text(self.driver,titlle_value7, value_expected7)

        titlle_value8 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[4]/app-number-values-card/div/div/div/div[2]/div/p"
        value_expected8 = "usd"
        validate_text(self.driver, titlle_value8, value_expected8)

        element4 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[4]/app-number-values-card/div/div/div/div[3]/div/h4/span'
        validate_character_numeric_element(self.driver, element4  )

        

      
     
        
   def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(HomeTenant)
  runner = xmlrunner.XMLTestRunner(output='reportHomeTenat')
  runner.run(test_suite)
        
   

        
   
