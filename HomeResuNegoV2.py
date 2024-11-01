import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_elements, validate_character_numeric_element, validate_image_xpaht, validate_text
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession
from selenium.webdriver.support.ui import WebDriverWait


class HomeResNegocioTenantV2(unittest.TestCase):
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
      
        
         ##seleccionar el botón filtro 
         
        Filter_campaign = "//span[contains(text(),' Filtros')]"
        find_elements(self.driver, Filter_campaign)
        time.sleep(1)
      
 
        ## seleccionar limpiar campaña

        delete_campaign = "//div[contains(text(), '24/25')]"
        find_elements(self.driver, delete_campaign)
        time.sleep(2)
     

        select_campaign = '/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[2]/div/div'
        find_elements(self.driver, select_campaign)

       
        selecct_button_aplicar = '/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button/span'
        find_elements(self.driver, selecct_button_aplicar)
        time.sleep(6)



        
        title_expected = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[1]/div[1]/div/p'
        title_obtained = "Resumen de Mis Negocios de Granos"
        validate_text(self.driver, title_expected,title_obtained)
      
        
        
      
        # validar imagen 

        image_1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[1]/div/img"
        image_1_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_xpaht(self.driver, image_1, image_1_expected)

        # validar valores 

   
       
        
        titlle_value1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[1]/div/div/div[1]/span"
        value_expected1 = "Soja"
        validate_text(self.driver, titlle_value1, value_expected1)

        element1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[1]/div/div/div[2]/span'
        validate_character_numeric_element(self.driver, element1  )
     
        titlle_value2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[2]/app-indicator-card/div/div[2]/div[1]/div[1]"
        value_expected2 = "Entregado:"
        validate_text(self.driver, titlle_value2, value_expected2)
        
        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[2]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element2  )
        
        titlle_value3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[2]/app-indicator-card/div/div[2]/div[2]/div[1]"
        value_expected3 = "Pendientes"
        validate_text(self.driver, titlle_value3, value_expected3)

        element3 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[2]/app-indicator-card/div/div[2]/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element3  )

        titlle_value4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[3]/app-indicator-card/div/div[2]/div[1]/div[1]"
        value_expected4 = "Fijado:"
        validate_text(self.driver, titlle_value4, value_expected4)
   
        element4 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[3]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element4  )

        # validar segundo cuadrente en dolares

        titlle_value5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[3]/app-indicator-card/div/div[2]/div[2]/div[1]"
        value_expected5 = "Pendientes"
        validate_text(self.driver, titlle_value5, value_expected5)

        element5 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[3]/app-indicator-card/div/div[2]/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element5  )
     
        titlle_value6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[4]/app-indicator-card/div/div[2]/div[1]/div[1]"
        value_expected6 = "Pesificado:"
        validate_text(self.driver, titlle_value6, value_expected6)
        
        element6 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[4]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element6  )
        
        titlle_value7 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[4]/app-indicator-card/div/div[2]/div[2]/div[1]"
        value_expected7 = "Pendientes"
        validate_text(self.driver, titlle_value7, value_expected7)

        element7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[4]/app-indicator-card/div/div[2]/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element7  )

        titlle_value8 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[5]/app-indicator-card/div/div[2]/div[1]/div[1]"
        value_expected8 = "Liquidado:"
        validate_text(self.driver, titlle_value8, value_expected8)
   
        element8 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[5]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element8  )

        titlle_value9 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[5]/app-indicator-card/div/div[2]/div[2]/div[1]"
        value_expected9 = "Pendientes"
        validate_text(self.driver, titlle_value9, value_expected9)
   
        element9 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[5]/app-indicator-card/div/div[2]/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element9  )

        titlle_value10 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[6]/app-indicator-card/div/div[2]/div[1]/div[1]"
        value_expected10 = "Pagado:"
        validate_text(self.driver, titlle_value10, value_expected10)
   
        element10 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[6]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element10  )

        titlle_value11 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[5]/app-indicator-card/div/div[2]/div[2]/div[1]"
        value_expected11 = "Pendientes"
        validate_text(self.driver, titlle_value11, value_expected11)
   
        element11 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[6]/app-indicator-card/div/div[2]/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element11  )





        
        
    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(HomeResNegocioTenantV2)
  runner = xmlrunner.XMLTestRunner(output='reportHomeResNegocioTenatV2')
  runner.run(test_suite)
        
   