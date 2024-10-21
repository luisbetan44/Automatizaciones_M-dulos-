import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import calendar_todate_retro, find_elements, find_elements_id, select_option_click, validate_character_numeric_element, validate_text
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession

class SerFacturadosV2(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def services_billed(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")


        # ingresar al menú de cuentas 

        select_menu_Account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver,select_menu_Account)


        # ingresar al submenú de granos

        select_menu_grain ="/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[2]/a"
        find_elements(self.driver,select_menu_grain)

        select_tab_deliveries ="current-billed-services-tab"
        find_elements_id(self.driver,select_tab_deliveries)
        time.sleep(2)

        ## seleccionar filtro 

        button_dropdown1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div/form/div/div[1]/ng-select/div/span"
        option_desired1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[1]/form/div/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        select_option_click(self.driver, button_dropdown1, option_desired1)
        time.sleep(2)

        button_dropdown2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div/form/div/div[2]/ng-select/div/span"
        option_desired2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[1]/form/div/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        select_option_click(self.driver, button_dropdown2, option_desired2)
        time.sleep(2)

        # aplicar filtro de fecha actual a seis meses para atras 

        select_calendar = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[1]/form/div/div[3]/app-date-picker/div/input[2]"
        popup_xpath = "//div[contains(@class, 'flatpickr-calendar')]"
        select_chevron = "//span[@class='flatpickr-prev-month']"
        popup_xpath2 = "//div[contains(@class, 'flatpickr-calendar')]"
        click_chevron = 6
        calendar_todate_retro(self.driver, select_calendar, popup_xpath, select_chevron, popup_xpath2, clicks=click_chevron)
        time.sleep(2)

        select_button_generate = "//span[text()='Generar']"
        find_elements(self.driver, select_button_generate)

    
        ## validar titulo de la pantalla 

        title_deliveries_sales = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[2]/div/div"
        title_deliveries_sales_expected = "Gastos Tickets"
        validate_text(self.driver,title_deliveries_sales, title_deliveries_sales_expected )
        time.sleep(3)

        ## validar columnas de la pantalla 

    
        first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/thead/tr/th[1]"
        first_column_expected = "Fecha"
        validate_text(self.driver, first_column, first_column_expected )
      

        value_first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/tbody/tr[1]/td[1]"
        validate_character_string_element(self.driver, value_first_column)
      

        second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/thead/tr/th[2]"
        second_column_expected = "Comprobante"
        validate_text(self.driver, second_column, second_column_expected )

        value_second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/tbody/tr[1]/td[2]/span"
        validate_character_numeric_element(self.driver,value_second_column)
      
        

        third_column = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/thead/tr/th[3]'
        third_column_expected = "Acarreo/Flete"
        validate_text(self.driver, third_column, third_column_expected )
        

        value_third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/tbody/tr[1]/td[3]"
        validate_character_numeric_element(self.driver, value_third_column)
     
   

        fourth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/thead/tr/th[4]" 
        fourth_column_expected = "Imp. Secada"
        validate_text(self.driver,  fourth_column, fourth_column_expected )
       

        value_fourth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/tbody/tr[1]/td[4]"
        validate_character_numeric_element(self.driver,value_fourth_column1)
      

        

        fifth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/thead/tr/th[5]"
        fifth_column_expected = "Imp. Percepción"
        validate_text(self.driver,  fifth_column, fifth_column_expected )
       

        value_fifth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/tbody/tr[1]/td[5]"
        validate_character_numeric_element(self.driver,value_fifth_column1)
    

        

        sixth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/thead/tr/th[6]"
        sixth_column_expected = "Imp. Otros"
        validate_text(self.driver,  sixth_column, sixth_column_expected )
        

        value_sixth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/tbody/tr[1]/td[6]"
        validate_character_numeric_element(self.driver,value_sixth_column1)

        
        seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/thead/tr/th[7]"
        seventh_column_expected = "Imp. Total"
        validate_text(self.driver,  seventh_column, seventh_column_expected )
        

        value_seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[3]/app-tab-billed-services/app-billed-services/div[3]/p-table/div/div/table/tbody/tr[1]/td[7]"
        validate_character_numeric_element(self.driver,value_seventh_column)

       




    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(SerFacturadosV2)
  runner = xmlrunner.XMLTestRunner(output='SerFacturadosV2')
  runner.run(test_suite)
        