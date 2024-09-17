from telnetlib import EC
import unittest
import xmlrunner
import time
from Elements import  calendar_todate, click_icon_delete,displace_element, find_and_click_element_selector, find_elements, find_send_element, generate_and_send_number, search_and_displace_account,select_option_click, validate_text
from LoginSample import LoginSample
from startSession import StartSession




class precio_granos(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_granos_contratos(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()

        select_grain = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span"
        find_elements(self.driver,select_grain)
        time.sleep(2)

        select_price_grain = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[3]/a"
        find_elements(self.driver,select_price_grain)
        time.sleep(2)

        # validar titulo de la pantalla
        
        title_pag_market = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        value_expected = "MERCADOS"
        validate_text(self.driver, title_pag_market, value_expected)
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,500);")
        time.sleep(2)

        # borrar listado de disponible

        delete_price_grain1 = "#layout-wrapper > div > div > div > app-market-main > app-grain-price > div:nth-child(2) > app-grain-price-table:nth-child(1) > div > div > table > tbody > tr > td.pt-3.padding-last-column > svg-icon > svg"
        click_icon_delete(self.driver, delete_price_grain1)
        time.sleep(2)

        delete_price_grain2 = "#layout-wrapper > div > div > div > app-market-main > app-grain-price > div:nth-child(2) > app-grain-price-table:nth-child(3) > div > div > table > tbody > tr > td.pt-3.padding-last-column > svg-icon > svg"
        click_icon_delete(self.driver, delete_price_grain2)
        time.sleep(2)


        
        # agrgar productos 

        available = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/app-grain-price-table-header/div/div[2]/app-add-and-clean/div/div[1]/app-button/button"
        find_elements(self.driver,available)

        

        switch_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[1]/app-switch/div/input"
        find_elements(self.driver,switch_button)
        time.sleep(2)

        select_option_grain = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[2]/app-select/select"
        option_grain = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr[1]/td[2]/app-select/select/option[14]"
        select_option_click(self.driver, select_option_grain, option_grain )
        time.sleep(2)

        select_campaign = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr[1]/td[3]/app-select/select"
        option_campaign = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr[1]/td[3]/app-select/select/option[2]"
        select_option_click(self.driver, select_campaign, option_campaign )
        time.sleep(2)

        select_destination = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[4]/app-select/select"
        option_destination = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[4]/app-select/select/option[3]"
        select_option_click(self.driver, select_destination, option_destination )
        time.sleep(2)

        select_money = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[5]/app-select/select"
        option_money = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[5]/app-select/select/option[1]"
        select_option_click(self.driver, select_money, option_money )
        time.sleep(2)

        insert_price = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[6]/input"
        send_price = "3000"
        find_send_element(self.driver, insert_price, send_price )

       # seleccionar rango de fecha 02/12/2024 al 27/12/2024

        select_data_day = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[7]/app-date-picker/div/input[2]"
        popup_calendar1 = "//span[@class='flatpickr-day today' and @aria-current='date']"
        calendar_todate(self.driver, select_data_day, popup_calendar1)
        time.sleep(2)
        
        insert_amount1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[8]/input"
        send_amount1 = "8000"
        find_send_element(self.driver, insert_amount1, send_amount1 )


        insert_observation = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[9]/input'
        number_generate = generate_and_send_number(self.driver, insert_observation)

        select_idea = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[10]/input"
        find_elements(self.driver, select_idea)
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(600,0);")
        time.sleep(2)

        select_post = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[1]/app-grain-price-header/app-grain-price-header-release/div/div[2]/div/div[2]/app-button/button"
        find_elements(self.driver, select_post)
        time.sleep(2)

        select_accept_post = "//button[text()='Publicar']"
        find_elements(self.driver, select_accept_post)
        time.sleep(2)

        select_button_accept = "//button[text()='Aceptar']"
        find_elements(self.driver, select_button_accept)
        time.sleep(2)

        select_menu = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        find_elements(self.driver, select_menu)
        time.sleep(2)

         # Llamar a la función verify_and_click con el número generado
        select_hand = '(//*[contains(@id, "Grupo_10473")])[1]'
        displace_element(self.driver, select_hand)
        time.sleep(2)


        
        located_element = "/html/body/ngb-modal-window/div/div/app-sales-intent-modal/div[2]/app-sales-intent-form/div/div[1]/div/div[2]/div/app-customer-searcher/ng-select/div/div/div[2]/input"
        select_input = "/html/body/ngb-modal-window/div/div/app-sales-intent-modal/div[2]/app-sales-intent-form/div/div[1]/div/div[2]/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        account_number = "1023"
        search_and_displace_account(self.driver, account_number, select_input, located_element )
        time.sleep(2)

        insert_amount2 = "/html/body/ngb-modal-window/div/div/app-sales-intent-modal/div[2]/app-sales-intent-form/div/div[2]/div/div[2]/div/div/input"
        send_amount = "300"
        find_send_element(self.driver, insert_amount2, send_amount )

        select_button_request = "/html/body/ngb-modal-window/div/div/app-sales-intent-modal/div[2]/app-sales-intent-form/div/div[5]/app-button[2]/button"
        find_elements(self.driver, select_button_request)
        time.sleep(2)



        


    
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(precio_granos)
  runner = xmlrunner.XMLTestRunner(output='reportGranosprecio')
  runner.run(test_suite)
