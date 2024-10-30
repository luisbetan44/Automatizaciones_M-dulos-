import time
import unittest
import xmlrunner
from Elements import find_and_click_element, find_elements, find_elements_id, find_send_element,validate_character_numeric_element, validate_text
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession


class cuenta_mercaderia_remitidaV2(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_mercaderia_remitidaV2(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")
        # ingresar al menú de cuentas 

        select_menu_contrat = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver, select_menu_contrat)
        ## seleccionar cuenta corriente

        select_account = "//a[text()= ' Insumos ']  "
        find_elements(self.driver, select_account)
        time.sleep(3)

        # seleccionar tab mercaderia facturada 

        select_tab_invoiced_merchandise = "current-shipped_merchandise-tab"
        find_elements_id(self.driver, select_tab_invoiced_merchandise)

    
        
        # aplicar filtro de fecha del 30/04/2024 al 30/10/2024 

        select_calendar = '//*[@id="current-shipped_merchandise"]/app-tab-shipped-merchandise/app-remitted-merchandise/div[1]/div[2]/app-date-picker/div/input[2]'
        find_elements(self.driver, select_calendar)

        arrow_filter2 = "/html/body/div[4]/div[1]/span[1]"
        amount_click2 = 6
        find_and_click_element(self.driver, arrow_filter2, amount_click2)

        select_date1 = "/html/body/div[4]/div[2]/div/div[2]/div/span[30]"
        find_elements(self.driver, select_date1 )

        arrow_filter3 = "/html/body/div[4]/div[1]/span[2]"
        amount_click3 = 6
        find_and_click_element(self.driver, arrow_filter3, amount_click3)

        select_date2 = "/html/body/div[4]/div[2]/div/div[2]/div/span[31]"
        find_elements(self.driver, select_date2 )
        time.sleep(2)

        # ingresar datos en el campo que contenga del filtro

        send_data_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[1]/div[1]/input"
        value_data = "Premezcla"
        find_send_element(self.driver, send_data_filter, value_data)


        apply_button_filter = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[1]/div[4]/div/div[2]/app-button/button/span'
        find_elements(self.driver,  apply_button_filter)
        time.sleep(2)


        totes_value_ARS = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[2]/app-header-for-responsive-table/div/div/div[1]/div/div[1]/app-totalizer/div/div/div[2]/div[2]/span[1]"
        validate_character_numeric_element(self.driver,totes_value_ARS)

        totes_value_USD = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[2]/app-header-for-responsive-table/div/div/div[1]/div/div[2]/app-totalizer/div/div/div[2]/div[2]/span[1]"
        validate_character_numeric_element(self.driver,totes_value_USD)

        ## validar titulo de pantalla cuenta corriente aplicada 

        title_account = "//span[text() = 'Mercadería Remitida']"
        title_account_expected = "Mercadería Remitida"
        validate_text(self.driver,title_account,title_account_expected )
        ## validar totalizadores 


        ## validar informacion de los campos del primer movimiento en la pantalla 

        first_column = "//th[text()= 'Fecha'] "
        first_column_expected = "Fecha"
        validate_text(self.driver, first_column, first_column_expected )

        value_first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[1]/span/div/span"
        validate_character_string_element(self.driver, value_first_column)

        second_column = "//th[text()= ' Comprobante '] "
        second_column_expected = "Comprobante"
        validate_text(self.driver, second_column, second_column_expected )

        value_second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[2]/span/div/span"
        validate_character_numeric_element(self.driver,value_second_column)
        

        third_column = "//th[text()= ' Artículo '] "
        third_column_expected = "Artículo"
        validate_text(self.driver, third_column, third_column_expected )
        

        value_third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[3]/span/div/span"
        validate_character_string_element(self.driver, value_third_column)
   

        fourth_column = "//th[text()= ' Comp. Origen ']  " 
        fourth_column_expected = "Comp. Origen"
        validate_text(self.driver,  fourth_column, fourth_column_expected )
       

        value_fourth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[4]/span/div/span"
        validate_character_numeric_element(self.driver,value_fourth_column1)

        

        fifth_column = '//*[@id="current-shipped_merchandise"]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/thead/tr/th[7]' 
        fifth_column_expected = "Moneda"
        validate_text(self.driver,  fifth_column, fifth_column_expected )
        

        value_fifth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[6]/span/div/span"
        validate_character_string_element(self.driver,value_fifth_column1)


        sixth_column = "//th[text()= ' Precio ']  "
        sixth_column_expected = "Precio"
        validate_text(self.driver,  sixth_column, sixth_column_expected )
       

        value_sixth_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[7]/span/div/span"
        validate_character_numeric_element(self.driver,value_sixth_column1)


       

        seventh_column = '//*[@id="current-shipped_merchandise"]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/thead/tr/th[9]'
        seventhh_column_expected = "Total Neto USD"
        validate_text(self.driver,  seventh_column, seventhh_column_expected )
       

        value_seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[8]/span/div/span"
        validate_character_numeric_element(self.driver,value_seventh_column)

        ninth_column = '//*[@id="current-shipped_merchandise"]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/thead/tr/th[10]'
        ninth_column_expected = "Total Neto ARS"
        validate_text(self.driver,  ninth_column, ninth_column_expected )
       

        value_ninth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[9]/span/div/span"
        validate_character_numeric_element(self.driver,value_ninth_column)


        ## Seleccionar y descargar movimientos del listado 

        movements_list_1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/tbody/tr[1]/th/input"
        find_elements(self.driver, movements_list_1)

        movements_list_2 =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/tbody/tr[2]/th/input"
        find_elements(self.driver, movements_list_2)

        movements_list_3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[3]/app-responsive-table/div/div[2]/table/tbody/tr[3]/th/input"
        find_elements(self.driver, movements_list_3)
        time.sleep(2)

        
       ## seleccionar botón descargar  

        select_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[1]/div[4]/div/div[1]/app-header-for-responsive-table/div/div/div[2]/div/div/app-download-button/div/button[2]"
        find_elements(self.driver,   select_button)
        time.sleep(2)

        ## descargar Excel 

        download_document_Excel = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[1]/div[4]/div/div[1]/app-header-for-responsive-table/div/div/div[2]/div/div/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver, download_document_Excel)
        time.sleep(3)

        select_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[1]/div[4]/div/div[1]/app-header-for-responsive-table/div/div/div[2]/div/div/app-download-button/div/button[2]"
        find_elements(self.driver,   select_button)
        time.sleep(2)

        ## descargar PDF 

        download_document_PDF = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/div/div[4]/app-tab-shipped-merchandise/app-remitted-merchandise/div[1]/div[4]/div/div[1]/app-header-for-responsive-table/div/div/div[2]/div/div/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, download_document_PDF)
        time.sleep(3)

       
    


        go_out_list = "//a[text()= 'Reportes']  "
        find_elements(self.driver, go_out_list)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(cuenta_mercaderia_remitidaV2)
  runner = xmlrunner.XMLTestRunner(output='cuenta_mercaderia_remitidaV2')
  runner.run(test_suite)