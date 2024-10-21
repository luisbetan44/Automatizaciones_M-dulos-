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



        ## validar columnas de las entregas 

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
       

        fifth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[5]/span"
        fifth_column_expected = "Zarandeo"
        validate_text(self.driver,  fifth_column, fifth_column_expected )
       

        value_fifth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[6]"
        validate_character_numeric_element(self.driver,value_fifth_column1)

        value_fifth_column2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[7]"
        validate_character_numeric_element(self.driver,value_fifth_column2)
        

        sixth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[6]/span"
        sixth_column_expected = "Volátil"
        validate_text(self.driver,  sixth_column, sixth_column_expected )
        

        value_sixth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[8]"
        validate_character_numeric_element(self.driver,value_sixth_column1)

        value_sixth_column2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[9]"
        validate_character_numeric_element(self.driver,value_sixth_column2)
      

        seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[7]"
        seventh_column_expected = "Netos"
        validate_text(self.driver,  seventh_column, seventh_column_expected )
        

        value_seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[10]"
        validate_character_numeric_element(self.driver,value_seventh_column)
       

        eighth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[8]"
        eighth_column_expected = "Planta"
        validate_text(self.driver,  eighth_column, eighth_column_expected )
       

        value_eighth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[11]"
        validate_character_string_element(self.driver,value_eighth_column)
       

        ninth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[9]"
        ninth_column_expected = "Factor"
        validate_text(self.driver,  ninth_column, ninth_column_expected )
       

        value_ninth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[12]"
        validate_character_numeric_element(self.driver,value_ninth_column)

        tenth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[10]"
        tenth_column_expected = "Grado"
        validate_text(self.driver, tenth_column, tenth_column_expected)


        value_tenth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[13]"
        validate_character_numeric_element(self.driver,value_tenth_column)

        eleventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[11]"
        eleventh_column_expected = "N1116A"
        validate_text(self.driver, eleventh_column, eleventh_column_expected)

        value_eleventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[14]/a"
        validate_character_numeric_element(self.driver,value_eleventh_column)


        twelfth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[12]"
        twelfth_column_expected = "RM/CP"
        validate_text(self.driver, twelfth_column, twelfth_column_expected)

        value_twelfth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[15]"
        validate_character_numeric_element(self.driver,value_twelfth_column)

        thirteenth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[13]"
        thirteenth_column_expected = "Acarreo"
        validate_text(self.driver, thirteenth_column, thirteenth_column_expected)

        value_thirteenth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[16]"
        validate_character_string_element(self.driver,value_thirteenth_column)

        fourteenth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/thead/tr/th[14]"
        fourteenth_column_expected = "Empresa de Transporte"
        validate_text(self.driver, fourteenth_column, fourteenth_column_expected)

        value_fourteenth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[2]/app-rpt-deliv-and-sale-deliveries-list/div/div/div/div/p-table/div/div/table/tbody/tr[2]/td[17]"
        validate_character_string_element(self.driver,value_fourteenth_column)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        ## Validar ventas 

        title_sales = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/h2/button"
        title_sales_expected = "Ventas"
        validate_text(self.driver,title_sales, title_sales_expected )

        ## desplegar informacion

        select_chevron_deliveries ="/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/h2/button"
        find_elements(self.driver,select_chevron_deliveries)

        first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/thead/tr/th[1]"
        first_column_expected = "Fecha"
        validate_text(self.driver, first_column, first_column_expected )

        value_first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/tbody/tr[17]/td[1]"
        validate_character_string_element(self.driver, value_first_column)

        second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/thead/tr/th[2]"
        second_column_expected = "Comprobante"
        validate_text(self.driver, second_column, second_column_expected )

        value_second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/tbody/tr[17]/td[2]"
        validate_character_string_element(self.driver,value_second_column)
        

        third_column = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/thead/tr/th[3]'
        third_column_expected = "Puerto/Destino"
        validate_text(self.driver, third_column, third_column_expected )
        

        value_third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/tbody/tr[17]/td[3]"
        validate_character_string_element(self.driver, value_third_column)
   

        fourth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/thead/tr/th[4]" 
        fourth_column_expected = "Entrega desde"
        validate_text(self.driver,  fourth_column, fourth_column_expected )
       

        value_fourth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/tbody/tr[17]/td[4]"
        validate_character_string_element(self.driver,value_fourth_column1)

       
        fifth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/thead/tr/th[5]"
        fifth_column_expected = "Entrega hasta"
        validate_text(self.driver,  fifth_column, fifth_column_expected )
       

        value_fifth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/tbody/tr[17]/td[5]"
        validate_character_string_element(self.driver,value_fifth_column1)

        
        sixth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/thead/tr/th[6]"
        sixth_column_expected = "Kilos Totales"
        validate_text(self.driver,  sixth_column, sixth_column_expected )
        

        value_sixth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/tbody/tr[17]/td[7]"
        validate_character_numeric_element(self.driver,value_sixth_column1)

       
        seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/thead/tr/th[7]"
        seventh_column_expected = "Sin Fijar TC"
        validate_text(self.driver,  seventh_column, seventh_column_expected )
        

        value_seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/tbody/tr[17]/td[7]"
        validate_character_numeric_element(self.driver,value_seventh_column)
       

        eighth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/thead/tr/th[8]"
        eighth_column_expected = "Liquidados"
        validate_text(self.driver,  eighth_column, eighth_column_expected )
       

        value_eighth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/tbody/tr[17]/td[8]"
        validate_character_numeric_element(self.driver,value_eighth_column)
       

        ninth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/thead/tr/th[9]"
        ninth_column_expected = "Precios"
        validate_text(self.driver,  ninth_column, ninth_column_expected )
       

        value_ninth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/tbody/tr[17]/td[9]"
        validate_character_numeric_element(self.driver,value_ninth_column)

        tenth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/thead/tr/th[10]"
        tenth_column_expected = "Moneda"
        validate_text(self.driver, tenth_column, tenth_column_expected)


        value_tenth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[1]/div/div/table/tbody/tr[17]/td[10]"
        validate_character_string_element(self.driver,value_tenth_column)

        ## validar venta a fijar 

        title_sales = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/div"
        title_sales_expected = "Ventas a Fijar"
        validate_text(self.driver,title_sales, title_sales_expected )

       
        first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/thead/tr/th[1]"
        first_column_expected = "Fecha"
        validate_text(self.driver, first_column, first_column_expected )

        value_first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/tbody/tr[1]/td[1]"
        validate_character_string_element(self.driver, value_first_column)

        second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/thead/tr/th[2]"
        second_column_expected = "Comprobante"
        validate_text(self.driver, second_column, second_column_expected )

        value_second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/tbody/tr[1]/td[2]"
        validate_character_string_element(self.driver,value_second_column)
        

        third_column = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/thead/tr/th[3]'
        third_column_expected = "Puerto/Destino"
        validate_text(self.driver, third_column, third_column_expected )
        

        value_third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/tbody/tr[1]/td[3]"
        validate_character_string_element(self.driver, value_third_column)
   

        fourth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/thead/tr/th[4]" 
        fourth_column_expected = "Entrega desde"
        validate_text(self.driver,  fourth_column, fourth_column_expected )
       

        value_fourth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/tbody/tr[1]/td[4]"
        validate_character_string_element(self.driver,value_fourth_column1)

       
        fifth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/thead/tr/th[5]"
        fifth_column_expected = "Entrega hasta"
        validate_text(self.driver,  fifth_column, fifth_column_expected )
       

        value_fifth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/tbody/tr[1]/td[5]"
        validate_character_string_element(self.driver,value_fifth_column1)

        
        sixth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/thead/tr/th[6]"
        sixth_column_expected = "Kilos a Fijar"
        validate_text(self.driver,  sixth_column, sixth_column_expected )
        

        value_sixth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/tbody/tr[1]/td[7]"
        validate_character_numeric_element(self.driver,value_sixth_column1)

       
        seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/thead/tr/th[7]"
        seventh_column_expected = "Kilos Totales"
        validate_text(self.driver,  seventh_column, seventh_column_expected )
        

        value_seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/tbody/tr[1]/td[7]"
        validate_character_numeric_element(self.driver,value_seventh_column)
       

        eighth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/thead/tr/th[8]"
        eighth_column_expected = "Entregados"
        validate_text(self.driver,  eighth_column, eighth_column_expected )
       

        value_eighth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/tbody/tr[1]/td[8]"
        validate_character_numeric_element(self.driver,value_eighth_column)
       

        ninth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/thead/tr/th[9]"
        ninth_column_expected = "Pendientes"
        validate_text(self.driver,  ninth_column, ninth_column_expected )
       

        value_ninth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[3]/app-rpt-deliv-and-sale-sales-list/div/div/div/div/p-table[2]/div/div/table/tbody/tr[1]/td[9]"
        validate_character_numeric_element(self.driver,value_ninth_column)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)


        ## Validar otro movimientos 
        title_older_movements = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/h2/button"
        title_older_movements_expected = "Otros Movimientos"
        validate_text(self.driver,title_older_movements, title_older_movements_expected )

        ## desplegar informacion

        select_chevron_deliveries ="/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/h2/button"
        find_elements(self.driver,select_chevron_deliveries)

        first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/div/div/p-table/div/div/table/thead/tr/th[1]"
        first_column_expected = "Fecha"
        validate_text(self.driver, first_column, first_column_expected )

        value_first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/div/div/p-table/div/div/table/tbody/tr[1]/td[1]"
        validate_character_string_element(self.driver, value_first_column)

        second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/div/div/p-table/div/div/table/thead/tr/th[2]"
        second_column_expected = "Comprobante"
        validate_text(self.driver, second_column, second_column_expected )

        value_second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/div/div/p-table/div/div/table/tbody/tr[1]/td[2]"
        validate_character_string_element(self.driver,value_second_column)
        

        third_column = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/div/div/p-table/div/div/table/thead/tr/th[3]'
        third_column_expected = "Comprobante Origen"
        validate_text(self.driver, third_column, third_column_expected )
        

        value_third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/div/div/p-table/div/div/table/tbody/tr[1]/td[3]"
        validate_character_string_element(self.driver, value_third_column)
   

        fourth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/div/div/p-table/div/div/table/thead/tr/th[5]" 
        fourth_column_expected = "Entradas"
        validate_text(self.driver,  fourth_column, fourth_column_expected )
       

        value_fourth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/div/div/p-table/div/div/table/tbody/tr[1]/td[4]"
        validate_character_string_element(self.driver,value_fourth_column1)

       
        fifth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/div/div/p-table/div/div/table/thead/tr/th[6]"
        fifth_column_expected = "Salidas"
        validate_text(self.driver,  fifth_column, fifth_column_expected )
       

        value_fifth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/div/div/p-table/div/div/table/tbody/tr[1]/td[6]"
        validate_character_string_element(self.driver,value_fifth_column1)

        
        sixth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/div/div/p-table/div/div/table/thead/tr/th[7]"
        sixth_column_expected = "Observaciones"
        validate_text(self.driver,  sixth_column, sixth_column_expected )
        

        value_sixth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[2]/app-tab-deliveries-and-sales/app-deliveries-and-sales/div[2]/div[4]/app-rpt-deliv-and-sale-others-mov-list/div/div/div/div/p-table/div/div/table/tbody/tr[1]/td[7]"
        validate_character_numeric_element(self.driver,value_sixth_column1)

       
        
       



    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(EntregasVentasV2)
  runner = xmlrunner.XMLTestRunner(output='EntregasVentasV2')
  runner.run(test_suite)
        