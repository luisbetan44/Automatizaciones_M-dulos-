import unittest
import time
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from Elements import calendar_todate, find_and_click_element, find_elements, find_send_element, find_send_element_selector, search_and_select_producer, select_option_click, validate_strt, validate_text
from LoginSample import LoginSample
from startSession import StartSession


class Fijaciones_precio(unittest.TestCase):


    def    setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_grain_pipup(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()
        

       

        select_grain = '/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span'
        find_elements(self.driver,select_grain )
        time.sleep(2)



        select_fijaciones =  '/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[1]/a'
        find_elements(self.driver,select_fijaciones )
        time.sleep(3)


        ## validar que estamos en la solapa fijaciones habilitadas 
        element = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/ul/li[1]/a'
        value_expected = "Fijaciones Habilitadas"
        validate_text(self.driver, element, value_expected  )

       ## localiza el input y envia el número de la cuenta 
        xpath_search_input = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/div/div[1]/app-bindings-enabled-list/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/div/div/div[2]/input"
        account_number = '484'
        xpath_search_results = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/div/div[1]/app-bindings-enabled-list/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[5]/span"
        search_and_select_producer(self.driver, xpath_search_input, xpath_search_results, account_number)
        time.sleep(5)
        # aplicar filtro  rango de fecha 09/01/2024 al 22/02/2024
         
        apply_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/div/div[1]/app-bindings-enabled-list/app-header-for-responsive-table/div/div/div[2]/div/div/app-filter-button/button/div/span"
        find_elements(self.driver, apply_filter )
        time.sleep(3)
       
        select_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        find_elements(self.driver, select_filter )
        time.sleep(2)

        arrow_filter1 = "/html/body/div/div[1]/span[1]"
        amount_click1 = 6
        find_and_click_element(self.driver, arrow_filter1, amount_click1)

        select_date = "/html/body/div/div[2]/div/div[2]/div/span[9]"
        find_elements(self.driver, select_date )
        time.sleep(2)

        arrow_filter2 = "/html/body/div/div[1]/span[2]"
        amount_click2 = 1
        find_and_click_element(self.driver, arrow_filter2, amount_click2)


        select_date = "/html/body/div/div[2]/div/div[2]/div/span[25]"
        find_elements(self.driver, select_date )
        time.sleep(2)

        apply_filter_button = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver, apply_filter_button )
        time.sleep(3)


        select_button_pinup = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/div/div[1]/app-bindings-enabled-list/app-responsive-table-multiple-items/div/table/tbody/tr[2]/td[6]/div/div[2]/app-button/button"
        find_elements(self.driver,select_button_pinup )
        ## validar titulo de la pagima 


        title_pinup_grain = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div[1]/div[1]/section/form/div/h2"
        title_pinup_grain_expected = "Nueva Fijación de Precio"
        validate_text(self.driver,title_pinup_grain, title_pinup_grain_expected  )

        ## ingresar cantidad a fijar 
        insert_amount_grain = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div[1]/div[1]/section/form/div/div/div[6]/div/div/input"
        send_amount_grain = "100"
        find_send_element(self.driver,insert_amount_grain, send_amount_grain )
        time.sleep(2)

        ## selecciona el mercado 

        select_market = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div/div[1]/section/form/div/div/div[8]/div/select'
        send_market = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div/div[1]/section/form/div/div/div[8]/div/select/option[3]"
        select_option_click(self.driver,select_market, send_market )

        ## insertar el precio

        insert_price_grain = "#layout-wrapper > div > div > div > app-set-price > div > div.col-12.col-md-7.mb-md-0.p > section > form > div > div > div:nth-child(12) > div > div > input"
        send_price_grain = "30000"
        find_send_element_selector(self.driver, insert_price_grain, send_price_grain )
        time.sleep(2)

        ## seleccionar fecha tc desde 

        select_data_day = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div/div[1]/section/form/div/div/div[14]/app-date-picker/div/input[2]"
        popup_calendar1 = "//div[contains(@class, 'flatpickr-calendar')]"
        calendar_todate(self.driver, select_data_day, popup_calendar1)
        time.sleep(2)
        
         ## seleccionar fechas tc hasta 01/12/2024

        select_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div/div[1]/section/form/div/div/div[16]/app-date-picker/div/input[2]"
        find_elements(self.driver, select_filter )
        time.sleep(2)

        arrow_filter1 = "/html/body/div[2]/div[1]/span[2]"
        amount_click1 = 6
        find_and_click_element(self.driver, arrow_filter1, amount_click1)

        select_date = "/html/body/div[2]/div[2]/div/div[2]/div/span[7]"
        find_elements(self.driver, select_date )
        time.sleep(2)
        

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        select_nex_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div/div[1]/section/form/div/div/div[18]/div/div[2]/app-button/button"
        find_elements(self.driver,select_nex_button )
        time.sleep(2)

        continue_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div/div[1]/section/form/div/div/div[18]/div/div[2]/app-button/button"
        find_elements(self.driver,continue_button )
        time.sleep(2)

        confim_button = "/html/body/div[4]/div/div[6]/button[3]"
        find_elements(self.driver,confim_button )
        time.sleep(2)

        ## validar respuesta

        message_finalized = "/html/body/div[4]/div/h2"
        message_expected = "Tu fijación fue enviada al sistema"
        validate_strt(self.driver, message_expected,message_finalized )

        accept_button = "/html/body/div[4]/div/div[6]/button[3]"
        find_elements(self.driver,accept_button )
        time.sleep(2)







    
    def tearDown(self):
        self.driver.quit()







if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'reporte_fijaciones'))
        