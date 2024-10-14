
import unittest
import xmlrunner
import time
from Elements import calendar_todate_retro, find_and_click_element, find_elements, validate_chain_text_xpaht, validate_character_numeric_element, validate_text, validate_text_by_text, validate_text_visible, validate_text_visible_selector
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession




class cuenta_ventas(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_cuenta_ventas(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

        # ingresar al menú de cuentas 

        select_menu_Account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver,select_menu_Account )


        select_sales = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[3]/a"
        find_elements(self.driver, select_sales )
        time.sleep(3)



        #   Validar titulo de la pantalla 

        title_menu = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/div/span"
        tille_expected = "Mis Ventas"
        validate_text_visible(self.driver, title_menu, tille_expected )  


        # selecionar botón del filtro
        selct_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/span"
        find_elements(self.driver,selct_filter )
        time.sleep(2)
 


        # limpiar  filtro 

        clean_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[1]/button"
        find_elements(self.driver,clean_filter )
        time.sleep(2)

        # aplicar filtro  

        apply_product_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[1]/div/img"
        find_elements(self.driver,apply_product_filter )
        time.sleep(2)

        apply_Campaign_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[1]/div/div"
        find_elements(self.driver,apply_Campaign_filter )
        time.sleep(2)

        

        select_calendar = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        popup_xpath = "//div[contains(@class, 'flatpickr-calendar')]"
        select_chevron = "//span[@class='flatpickr-prev-month']"
        popup_xpath2 = "//div[contains(@class, 'flatpickr-calendar')]"
        click_chevron = 6
        calendar_todate_retro(self.driver, select_calendar, popup_xpath, select_chevron, popup_xpath2, clicks=click_chevron)
        time.sleep(2)

        apply_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver,apply_filter )
        time.sleep(2)

        # seleccionar dos movimientos 

        select_product_list_1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[1]/th/input"
        find_elements(self.driver, select_product_list_1 )
        time.sleep(1)


        select_product_list_2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[2]/th/input"
        find_elements(self.driver, select_product_list_2 )
        time.sleep(1)



        select_product_list_3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[3]/th/input"
        find_elements(self.driver, select_product_list_3 )
        time.sleep(1)

        # selecionar el botón para descargar los movimientos 

        button_download = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, button_download )
        time.sleep(1)

        select_format = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, select_format )
        time.sleep(3)

         
    
         # validar venta


        validate_product = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/thead/tr/th[2]"
        validate_character_string_element(self.driver, validate_product)
        
     
        type_product = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[1]/td[1]/span/div/span"
        validate_character_string_element(self.driver,type_product) 

        validate_date = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/thead/tr/th[3]"
        validate_character_string_element(self.driver, validate_date)

        date_data = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[1]/td[2]/span/div/span"
        validate_character_string_element(self.driver, date_data )


        validate_number_boucher = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/thead/tr/th[4]"
        validate_character_string_element(self.driver, validate_number_boucher)

        validate_number = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[1]/td[3]/span/div/span"
        validate_character_string_element(self.driver, validate_number)

        account_sales_title = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/thead/tr/th[5]"
        validate_character_string_element(self.driver, account_sales_title )


        account_sales = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[1]/td[4]/span/div/span'
        validate_character_numeric_element(self.driver, account_sales  )
       
        
        title_price = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/thead/tr/th[6]"
        title_price_expected = "Precio"
        validate_text_visible(self.driver,title_price, title_price_expected ) 

        number_price = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[1]/td[5]/span/div/span'
        validate_character_numeric_element(self.driver, number_price  ) 

        validate_title_money = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/thead/tr/th[7]"
        validate_title_money_expected = "Moneda"
        validate_text(self.driver, validate_title_money, validate_title_money_expected) 

        validate_type_money = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[1]/td[6]/span/div/span"
        validate_type_money_expected = "ARS"
        validate_text(self.driver, validate_type_money, validate_type_money_expected) 

  

        

        
        
       

        



  





    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  
  test_suite = unittest.TestLoader().loadTestsFromTestCase(cuenta_ventas)
  runner = xmlrunner.XMLTestRunner(output='reportCuentaVentas')
  runner.run(test_suite)
   
