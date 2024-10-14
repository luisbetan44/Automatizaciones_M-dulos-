

import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_elements,  validate_chain_text_xpaht,validate_image_css_selector, validate_image_xpaht, validate_text
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession
from selenium.webdriver.support.ui import WebDriverWait


class HomeResNegocioTenant(unittest.TestCase):
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

        delete_campaign = "//div[contains(text(), '23/24')]"
        find_elements(self.driver, delete_campaign)
        time.sleep(2)
     

        select_campaign = '/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[2]/div/div'
        find_elements(self.driver, select_campaign)

       
        selecct_button_aplicar = '/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button/span'
        find_elements(self.driver, selecct_button_aplicar)
        time.sleep(6)



        
        title_expected = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[2]/app-business-indicators/div[1]/div[1]/div/p'
        title_obtained = "Resumen de Mis Negocios de Granos"
        validate_text(self.driver, title_expected,title_obtained)
      
        
        
      
        # validar imagen 

        image_1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[1]/div/img"
        image_1_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_xpaht(self.driver, image_1, image_1_expected)

        # validar valores 

        ## entregado
       
        
        element6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[2]/app-indicator-card/div/div[2]/div[1]/div[2]"
        validate_character_string_element(self.driver, element6  )
        time.sleep(2)




        
        
    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(HomeResNegocioTenant)
  runner = xmlrunner.XMLTestRunner(output='reportHomeResNegocioTenat')
  runner.run(test_suite)
        
   

        
   
