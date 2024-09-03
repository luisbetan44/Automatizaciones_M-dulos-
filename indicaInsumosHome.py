import time
import unittest
import xmlrunner
from Elements import  validate_chain_text_xpaht, validate_character_numeric_element, validate_text
from startSession import StartSession
from loginhelper import LoginHelper



class IndicaInsumosHome(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test__indicators_home(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("484")

       
      
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        
     ##validar titulos de los indicadores 
       
        titlle_value1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/p"
        value_expected1 = ["Indicadores de Insumos (correspondiente a los últimos  6 meses)","Indicadores de Insumos (correspondiente a los últimos  12 meses)"]
        validate_chain_text_xpaht(self.driver, titlle_value1, value_expected1)
     
        titlle_value2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div/swiper/div/div[1]/div[1]/app-supplies-indicator/div/div[1]/div"
        value_expected2 = "Insumos Pendientes de Retirar"
        validate_text(self.driver, titlle_value2, value_expected2)
        time.sleep(2)


        # validaciones de los indicadores del grafico 

        produtc_value_primary1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div/swiper/div/div[1]/div[1]/app-supplies-indicator/div/div[3]/div[1]/div[2]"
        produtc_expected1 = ["Semillas Hibrida","Agroquimico","Varios"," Balanceado ", "Fertilizante"]
        validate_chain_text_xpaht(self.driver, produtc_value_primary1,  produtc_expected1)

        product_quantity1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div/swiper/div/div[1]/div[1]/app-supplies-indicator/div/div[3]/div[1]/div[3]"
        validate_character_numeric_element(self.driver,product_quantity1)


        titlle_value3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div/swiper/div/div[1]/div[2]/app-supplies-indicator/div/div[1]/div"
        value_expected3 = "Mercadería Remitida"
        validate_text(self.driver, titlle_value3, value_expected3)

        produtc_value_primary2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div/swiper/div/div[1]/div[2]/app-supplies-indicator/div/div[3]/div[1]/div[2]"
        produtc_expected2 = ["Semillas Hibrida","Agroquimico","Varios"," Balanceado ", "Fertilizante"]
        validate_chain_text_xpaht(self.driver, produtc_value_primary2,  produtc_expected2)

        product_quantity2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div/swiper/div/div[1]/div[2]/app-supplies-indicator/div/div[3]/div[1]/div[3]"
        validate_character_numeric_element(self.driver,product_quantity2)
        
        
        titlle_value4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div/swiper/div/div[1]/div[3]/app-supplies-indicator/div/div[1]/div"
        value_expected4 = "Mercadería Facturada"
        validate_text(self.driver, titlle_value4, value_expected4)



        produtc_value_primary2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div/swiper/div/div[1]/div[3]/app-supplies-indicator/div/div[3]/div[1]/div[2]"
        produtc_expected2 = ["Semillas Hibrida","Agroquimico","Varios"," Balanceado ", "Fertilizante", "Diferencia De Cambio"]
        validate_chain_text_xpaht(self.driver, produtc_value_primary2,  produtc_expected2)

        product_quantity3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div/swiper/div/div[1]/div[3]/app-supplies-indicator/div/div[3]/div[1]/div[3]"
        validate_character_numeric_element(self.driver,product_quantity3)
        



       
    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(IndicaInsumosHome)
  runner = xmlrunner.XMLTestRunner(output='reportIndicaInsumosHome')
  runner.run(test_suite)
        
   
