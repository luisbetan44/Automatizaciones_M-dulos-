import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import calendar_todate_retro, find_elements, find_elements_id, select_option_click, validate_character_numeric_element,  validate_text
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession


class TenenImpositivasV2(unittest.TestCase):
   def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

   def test_tax_holdings(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")
        time.sleep(3)

        
       
        # ingresar al menú de cuentas 

        select_menu_Account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver,select_menu_Account)

        # ingresar al submenú de granos

        select_menu_grain ="/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[2]/a"
        find_elements(self.driver,select_menu_grain)

        select_tab_deliveries ="current-tenencias-tab"
        find_elements_id(self.driver,select_tab_deliveries)
        time.sleep(8)

        ## refrescar busqueda 
        select_button_generate = "//span[text()='Generar']"
        find_elements(self.driver, select_button_generate)
        time.sleep(3)

        ## validar totalizadores 

        first_tolalyzers = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/div[2]/div[2]/div[1]/app-totalizer-down/div/div/div/div[1]/span"
        first_tolalyzers_expected = "Saldo ARS"
        validate_text(self.driver,first_tolalyzers,first_tolalyzers_expected )

        value_first_tolalyzers = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/div[2]/div[2]/div[1]/app-totalizer-down/div/div/div/div[2]/span"
        validate_character_numeric_element(self.driver, value_first_tolalyzers)

        second_tolalyzers = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/div[2]/div[2]/div[2]/app-totalizer-down/div/div/div/div[1]/span"
        second_tolalyzers_expected = "Saldo USD"
        validate_text(self.driver,second_tolalyzers,second_tolalyzers_expected )

        value_second_tolalyzers = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/div[2]/div[2]/div[2]/app-totalizer-down/div/div/div/div[2]/span"
        validate_character_numeric_element(self.driver, value_second_tolalyzers)

        third_tolalyzers = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/div[2]/div[2]/div[3]/app-totalizer-down/div/div/div/div[1]/span"
        third_tolalyzers_expected = "Saldo Contable"
        validate_text(self.driver,third_tolalyzers,third_tolalyzers_expected )

        value_third_tolalyzers = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/div[2]/div[2]/div[3]/app-totalizer-down/div/div/div/div[2]/span"
        validate_character_numeric_element(self.driver, value_third_tolalyzers)


        # validar listado de movimientos 
        first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/app-responsive-table/div/div/table/thead/tr/th[1]"
        first_column_expected = "Producto"
        validate_text(self.driver,first_column,first_column_expected )
        
        value_first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/app-responsive-table/div/div/table/tbody/tr[1]/td[1]/span/div/span"
        validate_character_string_element(self.driver,value_first_column )

        second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/app-responsive-table/div/div/table/thead/tr/th[2]"
        second_column_expected = "Campaña"
        validate_text(self.driver,second_column,second_column_expected )

        value_second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/app-responsive-table/div/div/table/tbody/tr[1]/td[2]/span/div/span"
        validate_character_string_element(self.driver,value_second_column)

        third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/app-responsive-table/div/div/table/thead/tr/th[3]"
        third_column_column_expected = "Kg. Netos"
        validate_text(self.driver,third_column,third_column_column_expected )

        value_third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/app-responsive-table/div/div/table/tbody/tr[1]/td[3]/span/div/span"
        validate_character_numeric_element(self.driver,value_third_column )
       
        quarter_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/app-responsive-table/div/div/table/thead/tr/th[4]"
        quarter_column_expected = "Kg. Pendientes Cert."
        validate_text(self.driver,quarter_column,quarter_column_expected )

        pending_kilos = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/app-responsive-table/div/div/table/tbody/tr[1]/td[4]/span/div/span"
        validate_character_numeric_element(self.driver,pending_kilos)

        ## descargar comprobantes
        
        select_button_download1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/div[1]/div[3]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, select_button_download1)
        time.sleep(2)

        select_option_Excel = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/div[1]/div[3]/div/div[1]/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver, select_option_Excel)
        time.sleep(2)

        select_button_download2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/div[1]/div[3]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, select_button_download2)
        time.sleep(2)

        select_option_PDF = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[7]/app-tab-tenencias-impositivas/app-tax-holdings/div[1]/div[3]/div/div[1]/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, select_option_PDF)
        time.sleep(2)

       







        

      
     
        
   def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(TenenImpositivasV2)
  runner = xmlrunner.XMLTestRunner(output='reportTenenImpositivasV2t')
  runner.run(test_suite)
        
   