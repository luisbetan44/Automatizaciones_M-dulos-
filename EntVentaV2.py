import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_elements, find_elements_id, select_option_click, validate_character_numeric_element, validate_text
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession

class EntregasVentasV2(unittest.TestCase):
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

        select_tab_deliveries ="current-deliveries_and_sales-tab"
        find_elements_id(self.driver,select_tab_deliveries)
        time.sleep(2)

        ## seleccionar filtro 

        button_dropdown1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div/form/div/div[1]/ng-select/div/span"
        option_desired1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div/form/div/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        select_option_click(self.driver, button_dropdown1, option_desired1)
        time.sleep(2)

        button_dropdown2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div/form/div/div[2]/ng-select/div/span"
        option_desired2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div/form/div/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[2]/span"
        select_option_click(self.driver, button_dropdown2, option_desired2)
        time.sleep(2)

        select_button_generate = "//span[text()='Generar']"
        find_elements(self.driver, select_button_generate)

    
        ## validar titulo de la pantalla 

        title_deliveries_sales = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/h2/button"
        title_deliveries_sales_expected = " Entregas "
        validate_text(self.driver,title_deliveries_sales, title_deliveries_sales_expected )

        ## desplegar informacion

        select_chevron_deliveries ="/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/h2/button"
        find_elements(self.driver,select_chevron_deliveries)

        ## validar totalizador 
        first_tote = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[1]/swiper/div/div[1]/div[1]/app-number-without-currency-card/div/div/div/div[1]/div/p"
        first_tote_expected = "Kilos Vendidos"
        validate_text(self.driver, first_tote, first_tote_expected )

        value_first_tote = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[1]/swiper/div/div[1]/div[1]/app-number-without-currency-card/div/div/div/div[2]/div/h4/span"
        validate_character_string_element(self.driver, value_first_tote)

        second_tote = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[1]/swiper/div/div[1]/div[2]/app-number-without-currency-card/div/div/div/div[1]/div/p"
        second_tote_expected = "Kilos a Fijar"
        validate_text(self.driver, second_tote, second_tote_expected )

        value_second_tote = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[1]/swiper/div/div[1]/div[2]/app-number-without-currency-card/div/div/div/div[2]/div/h4/span"
        validate_character_numeric_element(self.driver,value_second_tote)
        

        third_tote = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[1]/swiper/div/div[1]/div[3]/app-number-without-currency-card/div/div/div/div[1]/div/p'
        third_tote_expected = "Kilos Entregados"
        validate_text(self.driver, third_tote, third_tote_expected )
        

        value_third_tote = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[1]/swiper/div/div[1]/div[3]/app-number-without-currency-card/div/div/div/div[2]/div/h4/span"
        validate_character_numeric_element(self.driver, value_third_tote)
   

        fourth_tote = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[1]/swiper/div/div[1]/div[4]/app-number-without-currency-card/div/div/div/div[1]/div/p" 
        fourth_tote_expected = "Otros Movimientos"
        validate_text(self.driver,  fourth_tote, fourth_tote_expected )

        value_fourth_tote = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[1]/swiper/div/div[1]/div[4]/app-number-without-currency-card/div/div/div/div[2]/div/h4/span"
        validate_character_numeric_element(self.driver, value_fourth_tote)

        fifth_tote = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[1]/swiper/div/div[1]/div[5]/app-number-without-currency-card/div/div/div/div[1]/div/p"
        fifth_tote_expected = "Saldo"
        validate_text(self.driver,  fifth_tote, fifth_tote_expected )
       

        value_fifth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[1]/swiper/div/div[1]/div[5]/app-number-without-currency-card/div/div/div/div[2]/div/h4/span"
        validate_character_numeric_element(self.driver,value_fifth_column)



        ## validar columnas de la pantalla 

        first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[1]"
        first_column_expected = "Fecha"
        validate_text(self.driver, first_column, first_column_expected )

        value_first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[1]"
        validate_character_string_element(self.driver, value_first_column)

        second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[2]"
        second_column_expected = "Comprobante"
        validate_text(self.driver, second_column, second_column_expected )

        value_second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[2]"
        validate_character_numeric_element(self.driver,value_second_column)
        

        third_column = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[3]'
        third_column_expected = "Brutos"
        validate_text(self.driver, third_column, third_column_expected )
        

        value_third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[3]"
        validate_character_numeric_element(self.driver, value_third_column)
   

        fourth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[4]/span" 
        fourth_column_expected = "Humedad"
        validate_text(self.driver,  fourth_column, fourth_column_expected )
       

        value_fourth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[4]"
        validate_character_numeric_element(self.driver,value_fourth_column1)

        value_fourth_column2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[5]"
        validate_character_numeric_element(self.driver,value_fourth_column2)
       

        """"fifth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[1]/app-tab-deliveries-and-sales-summary/app-deliveries-and-sales-summary/p-table/div/div/table/thead/tr/th[5]"
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
        time.sleep(3)"""







    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(EntregasVentasV2)
  runner = xmlrunner.XMLTestRunner(output='EntregasVentasV2')
  runner.run(test_suite)
        