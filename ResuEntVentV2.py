import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_elements, find_elements_id, validate_character_numeric_element, validate_character_numeric_element_selector, validate_text
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession

class resuEntregasVentas(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_Report_deliverySales(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")


        # ingresar al menú de cuentas 

        select_menu_Account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver,select_menu_Account)


        # ingresar al submenú de reportes 

        select_menu_grain ="/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[2]/a"
        find_elements(self.driver,select_menu_grain)

    
        ## validar titulo de la pantalla 

        title_deliveries_sales = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/div[2]/div/div/div"
        title_deliveries_sales_expected = "Resumen de Entregas y Ventas"
        validate_text(self.driver,title_deliveries_sales, title_deliveries_sales_expected )

        ## validar columnas de la pantalla 

        first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/thead/tr/th[1]"
        first_column_expected = "Especie/Cosecha"
        validate_text(self.driver, first_column, first_column_expected )

        value_first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/tbody/tr[1]/td[1]"
        validate_character_string_element(self.driver, value_first_column)

        second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/thead/tr/th[2]"
        second_column_expected = "Entregas (Kg.)"
        validate_text(self.driver, second_column, second_column_expected )

        value_second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/tbody/tr[1]/td[2]"
        validate_character_numeric_element(self.driver,value_second_column)
        

        third_column = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/thead/tr/th[3]'
        third_column_expected = "Retiros (Kg.)"
        validate_text(self.driver, third_column, third_column_expected )
        

        value_third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/tbody/tr[1]/td[3]"
        validate_character_numeric_element(self.driver, value_third_column)
   

        fourth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/thead/tr/th[4]" 
        fourth_column_expected = "Transf. (Kg.)"
        validate_text(self.driver,  fourth_column, fourth_column_expected )
       

        value_fourth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/tbody/tr[1]/td[4]"
        validate_character_numeric_element(self.driver,value_fourth_column)
       

        fifth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/thead/tr/th[5]"
        fifth_column_expected = "Ventas (Kg.)"
        validate_text(self.driver,  fifth_column, fifth_column_expected )
       

        value_fifth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/tbody/tr[1]/td[5]"
        validate_character_numeric_element(self.driver,value_fifth_column)
        

        sixth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/thead/tr/th[6]"
        sixth_column_expected = "Saldo (Kg.)"
        validate_text(self.driver,  sixth_column, sixth_column_expected )
        

        value_sixth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/tbody/tr[1]/td[6]"
        validate_character_numeric_element(self.driver,value_sixth_column)
      

        seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/thead/tr/th[7]"
        seventh_column_expected = "Pend. Liq. (Kg.)"
        validate_text(self.driver,  seventh_column, seventh_column_expected )
        

        value_seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/tbody/tr[1]/td[7]"
        validate_character_numeric_element(self.driver,value_seventh_column)
       

        eighth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/thead/tr/th[8]"
        eighth_column_expected = "Precio Ponderado"
        validate_text(self.driver,  eighth_column, eighth_column_expected )
       

        value_eighth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/tbody/tr[1]/td[8]"
        validate_character_numeric_element(self.driver,value_eighth_column)
       

         # descargar listado 

        select_button_downloads1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/div[1]/form/div/div[3]/app-header-for-responsive-table/div/div/div[2]/div/div/app-download-button/div/button[2]"
        find_elements(self.driver, select_button_downloads1)
        time.sleep(2)

        select_option_excel = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/div[1]/form/div/div[3]/app-header-for-responsive-table/div/div/div[2]/div/div/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver, select_option_excel)
        time.sleep(10)

        select_button_downloads2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/div[1]/form/div/div[3]/app-header-for-responsive-table/div/div/div[2]/div/div/app-download-button/div/button[2]"
        find_elements(self.driver, select_button_downloads2)
        time.sleep(2)

        select_option_pdf = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/div[1]/form/div/div[3]/app-header-for-responsive-table/div/div/div[2]/div/div/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, select_option_pdf)
        time.sleep(2)

        ## validar switch sin saldo 


        select_switch ="flexSwitchCheckChecked"
        find_elements_id(self.driver, select_switch)
        time.sleep(5)

        sixth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/thead/tr/th[6]"
        sixth_column_expected = "Saldo (Kg.)"
        validate_text(self.driver,  sixth_column, sixth_column_expected )
        

        value_sixth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/tbody/tr[1]/td[6]"
        validate_character_numeric_element(self.driver,value_sixth_column)
      

        seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/thead/tr/th[7]"
        seventh_column_expected = "Pend. Liq. (Kg.)"
        validate_text(self.driver,  seventh_column, seventh_column_expected )
        

        value_seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/tbody/tr[1]/td[7]"
        validate_character_numeric_element(self.driver,value_seventh_column)
       

        go_out_reports = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver, go_out_reports)
        time.sleep(3)







    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(resuEntregasVentas)
  runner = xmlrunner.XMLTestRunner(output='resuEntregasVentas')
  runner.run(test_suite)
        
