
import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_elements, validate_character_numeric_element, validate_image_css_selector, validate_image_xpaht, validate_text, validate_text_by_strt
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

        ##seleccionar el botón filtro 
        Filter_campaign = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[1]/div[2]/app-filter-button/button/div/span"
        find_elements(self.driver, Filter_campaign)
      
 
        ## seleccionar filtro 

        delete_campaign = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-tag-container/div/div/div[7]/app-tag/div/div/i"
        find_elements(self.driver, delete_campaign)
     

        select_campaign = '/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[2]/div/div'
        find_elements(self.driver, select_campaign)

       
        selecct_button_aplicar = '/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button'
        find_elements(self.driver, selecct_button_aplicar)
        time.sleep(3)
       
       ## validar si el texto es visible para el usuario 
        page_hello = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/app-welcome-home/div/div[1]/div/p'
        text_expected = "Buen día JUAN DEMO!"
        validate_text(self.driver, page_hello, text_expected  )


     ##validar totalizadores vencidos a hoy 
       
        titlle_value1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[1]/app-number-values-card/div/div/div/div[1]/div/p"
        value_expected1 = "VENCIDO A HOY"
        validate_text(self.driver, titlle_value1, value_expected1)
     
        titlle_value2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[1]/app-number-values-card/div/div/div/div[2]/div/p"
        value_expected2 = "ARS"
        validate_text(self.driver, titlle_value2, value_expected2)
        
        element1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[1]/app-number-values-card/div/div/div/div[3]/div/h4/span'
        validate_character_numeric_element(self.driver, element1  )
        
        titlle_value3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[2]/app-number-values-card/div/div/div/div[1]/div/p"
        value_expected3 = "VENCIDO A HOY"
        validate_text(self.driver, titlle_value3, value_expected3)

        titlle_value4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[2]/app-number-values-card/div/div/div/div[2]/div/p"
        value_expected4 = "USD"
        validate_text(self.driver, titlle_value4, value_expected4)
   
        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[2]/app-number-values-card/div/div/div/div[3]/div/h4/span'
        validate_character_numeric_element(self.driver, element2  )

        ##validar totalizadores  a vencer
        titlle_value5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[3]/app-number-values-card/div/div/div/div[1]/div/p"
        value_expected5 = "A VENCER"
        validate_text(self.driver, titlle_value5, value_expected5)

        titlle_value6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[3]/app-number-values-card/div/div/div/div[2]/div/p"
        value_expected6 = "ARS"
        validate_text(self.driver, titlle_value6, value_expected6)  

        element3 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[3]/app-number-values-card/div/div/div/div[3]/div/h4/span'
        validate_character_numeric_element(self.driver, element3  )
        
        titlle_value7 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[4]/app-number-values-card/div/div/div/div[1]/div/p"
        value_expected7 = "A VENCER"
        validate_text(self.driver,titlle_value7, value_expected7)

        titlle_value8 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[4]/app-number-values-card/div/div/div/div[2]/div/p"
        value_expected8 = "USD"
        validate_text(self.driver, titlle_value8, value_expected8)

        element4 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[4]/app-number-values-card/div/div/div/div[3]/div/h4/span'
        validate_character_numeric_element(self.driver, element4  )
         
         ## Seleccionar el elemento que contiene el texto 

        element5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[1]/div[1]/div/p"
        text_expected = "Resumen de Mis Negocios de Granos"
        validate_text(self.driver,element5 , text_expected)

        # Seleccionar el elemento de la imagen
        
        image_1 = 'img[src="assets/images/grains/soja.svg"]'
        image_1_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_css_selector(self.driver, image_1, image_1_expected)

        # Seleccionar el elemento de la imagen

        image_2 = 'img[src="assets/images/grains/maiz.svg"]'
        image_2_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_css_selector(self.driver, image_2, image_2_expected)

        # Seleccionar el elemento de la imagen
        
        image_3 = 'img[src="assets/images/grains/trigo.svg"]'
        image_3_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_css_selector(self.driver, image_3, image_3_expected)

        ## validar los campor del resumen de mis negocios 
    
       ## entregado
       
        element6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[2]/app-indicator-card/div/div[2]/div[1]/div[2]"
        validate_character_numeric_element(self.driver, element6  )

        ## fijado 

        element7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[3]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element7  )

         ## pesificado

        element8 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[4]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element8  )

        ## liquidado

        element9 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[5]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element9  )

          ## pagado

        element10 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[6]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element10  )

        # validar entregas recientes 

        element11 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/p'
        text_expected = "Entregas y Ventas Recientes"
        validate_text(self.driver, element11, text_expected)

        # validar la imagen del producto 

        image_4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[1]/img"
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
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(HomeTenant)
  runner = xmlrunner.XMLTestRunner(output='reportHomeTenat')
  runner.run(test_suite)
        
   
