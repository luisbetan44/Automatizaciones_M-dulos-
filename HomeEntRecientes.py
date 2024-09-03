import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import validate_character_numeric_element, validate_image_css_selector, validate_image_xpaht, validate_text
from loginhelper import LoginHelper
from startSession import StartSession


class HomeEntRecientesTenant(unittest.TestCase):
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
        page_hello = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/app-welcome-home/div/div[1]/div/p'
        text_expected = "Buen día JUAN DEMO!"
        validate_text(self.driver, page_hello, text_expected  )

         
      # validar entregas recientes 

        element11 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/p'
        text_expected = "Entregas y Ventas Recientes"
        validate_text(self.driver, element11, text_expected)

        # validar la imagen del producto 

        image_4 = "#layout-wrapper > div > div > div > app-home > div > div:nth-child(4) > app-recent-grain-movements > div > div:nth-child(1) > app-recent-deliveries > app-responsive-table-multiple-items > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > div.me-2 > img"
        image_4_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_css_selector(self.driver, image_4, image_4_expected)

        #validar el numero de comprobante del movimiento 

        element12 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span'
        validate_character_numeric_element(self.driver, element12  )

       # validar los Kilos netos 
        element13 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span'
        validate_character_numeric_element(self.driver, element13  )
        
         # validar ventas recientes 

        element14 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/div/span[1]'
        text_expected = "Ventas Recientes"
        validate_text(self.driver, element14, text_expected)

        
        # validar la imagen del producto 


        image_5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[1]/img"
        image_5_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_xpaht(self.driver, image_5, image_5_expected)
       
        #validar la cantidad neta de la venta 

        element15 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span'
        validate_character_numeric_element(self.driver, element15  )

       # validar precio de la venta 
        element16 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span[2]'
        validate_character_numeric_element(self.driver, element16  )

     
   def tearDown(self):
        self.driver.close()
        





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(HomeEntRecientesTenant)
  runner = xmlrunner.XMLTestRunner(output='reportHomeEntRecientesTenat')
  runner.run(test_suite)
        
   

        
   
