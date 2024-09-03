import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import  calendar_todate_retro, find_and_click_element, find_elements, validate_character_numeric_element, validate_text
from loginhelper import LoginHelper
from startSession import StartSession

class reportPendFacturar(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_Report_PendFacturar(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")


        # ingresar al menú de cuentas 

        select_menu_Account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver,select_menu_Account)


        # ingresar al submenú de reportes 

        select_menu_reports ="/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[6]/a"
        find_elements(self.driver,select_menu_reports)

        # seleccionar el filtro 

        select_filter_reports = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-reports/div/app-header-for-responsive-table/div/div/div[2]/div/div/app-filter-button/button/div/span"
        find_elements(self.driver,select_filter_reports)
        time.sleep(2)

        select_receipts_pending = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-radio-button-list/div/app-radio[1]/div/input"
        find_elements(self.driver,select_receipts_pending)
        time.sleep(2)

        ## seleccionar filtro de los ultimos seis meses 

        select_calendar = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-reports-options/app-date-filter/div/app-date-picker/div/input[2]"
        popup_xpath = "//div[contains(@class, 'flatpickr-calendar')]"
        select_chevron = "//span[@class='flatpickr-prev-month']"
        popup_xpath2 = "//div[contains(@class, 'flatpickr-calendar')]"
        click_chevron = 6
        calendar_todate_retro(self.driver, select_calendar, popup_xpath, select_chevron, popup_xpath2, clicks=click_chevron)
        time.sleep(2)

        apply_option_select = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver,apply_option_select)
        time.sleep(2)

        # validar título de la pantalla 

        title_page_receipts = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/div/div/div[1]"
        title_page_receipts_expected = "Comprobantes Pendientes de Facturar"
        validate_text(self.driver,title_page_receipts,title_page_receipts_expected )
      
        # validar formato de la pagina 

        first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/thead/tr/th[2]"
        first_column_expected = "Comprobante"
        validate_text(self.driver,first_column,first_column_expected )

        value_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/tbody/tr[1]/td[1]/span/div/span"
        value_column_expected1 = "PED 0051 00017084"
        validate_text(self.driver,value_column1,value_column_expected1 )
      

        second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/thead/tr/th[3]"
        second_column_expected = "Artículo"
        validate_text(self.driver,second_column,second_column_expected )

        value_column2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/tbody/tr[1]/td[2]/span/div/span"
        value_column_expected2 = "110002 - Aceite mineral Novaoil x 20 lts NOVA SA."
        validate_text(self.driver,value_column2,value_column_expected2 )
      

        third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/thead/tr/th[4]"
        third_column_column_expected = "Cantidad"
        validate_text(self.driver,third_column,third_column_column_expected )

        value_column3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/tbody/tr[1]/td[3]/span/div/span"
        validate_character_numeric_element(self.driver,value_column3)

        quarter_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/thead/tr/th[5]"
        quarter_column_expected = "Cant. Pend."
        validate_text(self.driver,quarter_column,quarter_column_expected )

        value_column4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/tbody/tr[1]/td[4]/span/div/span"
        validate_character_numeric_element(self.driver,value_column4)

        fifth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/thead/tr/th[6]"
        fifth_column_expected = "Moneda"
        validate_text(self.driver,fifth_column,fifth_column_expected )

        value_column5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/tbody/tr[1]/td[5]/span/div/span"
        value_column_expected5 = "USD"
        validate_text(self.driver,value_column5,value_column_expected5 )

        sixth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/thead/tr/th[7]"
        sixth_column_expected = "Precio"
        validate_text(self.driver,sixth_column,sixth_column_expected )

        value_column6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/tbody/tr[1]/td[6]/span/div/span"
        validate_character_numeric_element(self.driver,value_column6)

        seventh_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/thead/tr/th[8]"
        sixth_column_expected = "Total USD"
        validate_text(self.driver, seventh_column,sixth_column_expected )

        value_column7 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/tbody/tr[1]/td[7]/span/div/span"
        validate_character_numeric_element(self.driver,value_column7)

        eighth_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/thead/tr/th[9]"
        sixth_column_expected = "Total ARS"
        validate_text(self.driver, eighth_column,sixth_column_expected )

    
        value_column8 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/tbody/tr[1]/td[8]/span/div/span"
        validate_character_numeric_element(self.driver,value_column8)
        
        

        # ingresar al detalle 
             
        enter_detail = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/tbody/tr[1]/td[2]"
        find_elements(self.driver,  enter_detail)


        # validar titulo del detalle 

        title_detail = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-pendient/div[1]/section/div/h2"
        title_detail_expected = "DATOS DEL COMPROBANTE PENDIENTE DE FACTURAR"
        validate_text(self.driver,title_detail,title_detail_expected )
    
    
     # validar descripcion de los campos del detalle 

        field_date =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-pendient/div[1]/section/div/div[1]/div[1]/strong/div"
        field_date_expected = "FECHA"
        validate_text(self.driver,field_date, field_date_expected )

        date_voucher = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-pendient/div[1]/section/div/div[1]/div[1]/div"
        validate_character_numeric_element(self.driver,date_voucher)
        

        field_article =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-pendient/div[1]/section/div/div[1]/div[2]/strong/div"
        field_article_expected = "ARTÍCULO"
        validate_text(self.driver,field_article, field_article_expected)

        

        descrition_article = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-pendient/div[1]/section/div/div[1]/div[2]/div"
        descrition_article_expected = "110002 - Aceite mineral Novaoil x 20 lts NOVA SA."
        validate_text(self.driver,descrition_article, descrition_article_expected)
       
       

        # salir del detalle 

        go_out_page = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver,  go_out_page)
        time.sleep(2)
       
       # descargar compromabtes 

        selecct_moviments_list1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/div/table/tbody/tr[1]/th/input"
        find_elements(self.driver, selecct_moviments_list1)

        dowlnload_button1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, dowlnload_button1)

        selecct_option1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver, selecct_option1)
        time.sleep(2)

        dowlnload_button2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, dowlnload_button2)

        selecct_option2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, selecct_option2)
        time.sleep(2)


        




    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(reportPendFacturar)
  runner = xmlrunner.XMLTestRunner(output='reportPendFacturar')
  runner.run(test_suite)

 