import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_elements, validate_character_numeric_element, validate_image_css_selector, validate_image_xpaht, validate_text
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession


class HomeEntVentRecientesV2(unittest.TestCase):
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


        self.driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(2)

         
      # validar entregas recientes 

        titlle_value1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[1]/p'
        value_expected1= "Entregas y Ventas Recientes"
        validate_text(self.driver, titlle_value1, value_expected1)

        titlle_value2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/div/span[1]"
        value_expected2 = "Entregas Recientes"
        validate_text(self.driver, titlle_value2, value_expected2)

        titlle_value3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/thead/tr/th[1]"
        value_expected3 = "Producto"
        validate_text(self.driver, titlle_value3, value_expected3)



        # validar la imagen del producto 

        image_1 = "#layout-wrapper > div > div > div > app-home-switch > app-home-v2 > div > div:nth-child(4) > app-recent-grain-movements > div:nth-child(2) > div:nth-child(1) > app-recent-deliveries > app-responsive-table-multiple-items > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > div.me-2 > img"
        image_1_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_css_selector(self.driver, image_1, image_1_expected)

        #validar especie y cosecha

        element1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[1]/span'
        validate_character_string_element(self.driver, element1  )

       # validar  fecha
        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[2]/span'
        validate_character_numeric_element(self.driver, element2  )

        titlle_value4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/thead/tr/th[2]"
        value_expected4 = "CTG/CRT"
        validate_text(self.driver, titlle_value4, value_expected4)

        element3 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span'
        validate_character_numeric_element(self.driver, element3  )

        titlle_value5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/thead/tr/th[3]"
        value_expected5 = "Kg Netos"
        validate_text(self.driver, titlle_value5, value_expected5)

        element4 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span'
        validate_character_numeric_element(self.driver, element4  )


        
         # validar ventas recientes 

        titlle_value6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/div/span[1]"
        value_expected6 = "Ventas Recientes"
        validate_text(self.driver, titlle_value6, value_expected6)

        titlle_value7 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/thead/tr/th[1]"
        value_expected7 = "Producto"
        validate_text(self.driver, titlle_value7, value_expected7)



        # validar la imagen del producto 

        image_2 = "#layout-wrapper > div > div > div > app-home-switch > app-home-v2 > div > div:nth-child(4) > app-recent-grain-movements > div:nth-child(2) > div:nth-child(2) > app-recent-sales > app-responsive-table-multiple-items > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > div.me-2 > img"
        image_2_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_css_selector(self.driver, image_2, image_2_expected)

        #validar especie y cosecha

        element5 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[1]/span'
        validate_character_string_element(self.driver, element5  )

       # validar  fecha
        element6 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[2]/span'
        validate_character_numeric_element(self.driver, element6  )

        titlle_value8 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/thead/tr/th[2]"
        value_expected8 = "Kg Netos"
        validate_text(self.driver, titlle_value8, value_expected8)

        element7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span'
        validate_character_numeric_element(self.driver, element7  )

        titlle_value9 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/thead/tr/th[3]"
        value_expected9 = "Precio"
        validate_text(self.driver, titlle_value9, value_expected9)

        element8 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span[1]'
        validate_character_string_element(self.driver, element8  )

        element9 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span[2]'
        validate_character_numeric_element(self.driver, element9  )

       
     
   def tearDown(self):
        self.driver.close()
        





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(HomeEntVentRecientesV2)
  runner = xmlrunner.XMLTestRunner(output='reportHomeEntVentRecientesV2')
  runner.run(test_suite)
        