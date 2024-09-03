

import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_elements,  validate_chain_text_xpaht,validate_image_css_selector, validate_text
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
      
        wait = WebDriverWait(self.driver, 10)

         ##seleccionar el botón filtro 
         
        Filter_campaign = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[1]/div[2]/app-filter-button/button/div/span"
        find_elements(self.driver, Filter_campaign)
        time.sleep(1)
      
 
        ## seleccionar filtro 

        delete_campaign = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-tag-container/div/div/div[7]/app-tag/div/div/i"
        find_elements(self.driver, delete_campaign)
     

        select_campaign = '/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[2]/div/div'
        find_elements(self.driver, select_campaign)

       
        selecct_button_aplicar = '/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button'
        find_elements(self.driver, selecct_button_aplicar)
        time.sleep(6)



        
        title_expected = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[1]/div[1]/div/p'
        title_obtained = "Resumen de Mis Negocios de Granos"
        validate_text(self.driver, title_expected,title_obtained)
      
        
        
      
        # validar imagen 

        image_1 = 'img[src="assets/images/grains/soja.svg"]'
        image_1_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_css_selector(self.driver, image_1, image_1_expected)

        # validar valores 

        ## entregado
       
        
        element6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[2]/app-indicator-card/div/div[2]/div[1]/div[2]"
        element6_expected = ["0 Kg ","0 Tn","58.505,31 QQ"]
        validate_chain_text_xpaht(self.driver, element6, element6_expected  )
        time.sleep(2)




        
        
    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(HomeResNegocioTenant)
  runner = xmlrunner.XMLTestRunner(output='reportHomeResNegocioTenat')
  runner.run(test_suite)
        
   

        
   
