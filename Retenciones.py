import time
import unittest
import xmlrunner
from Elements import calendar_todate_retro,find_elements, find_elements_id, validate_character_numeric_element, validate_text
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession


class cuenta_retenciones(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_ctacte_historica(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("484")

        # ingresar al menú de cuentas 

        select_menu_contrat = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver, select_menu_contrat)
        
        ## seleccionar cuenta corriente

        select_account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[4]/a"
        find_elements(self.driver, select_account)
        time.sleep(3)

     

        

        ## seleccionar solapa cta cte historica 

        select_account_withholdings = 'current-account-withholdings-tab'
        find_elements_id(self.driver, select_account_withholdings)
        

        
        # aplicar filtro de fecha actual a seis meses para atras 

        select_calendar = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-with-holdings-list/div/div[1]/app-date-picker/div/input[2]"
        popup_xpath = "//div[contains(@class, 'flatpickr-calendar')]"
        select_chevron = "//span[@class='flatpickr-prev-month']"
        popup_xpath2 = "//div[contains(@class, 'flatpickr-calendar')]"
        click_chevron = 6
        calendar_todate_retro(self.driver, select_calendar, popup_xpath, select_chevron, popup_xpath2, clicks=click_chevron)
        time.sleep(2)


        apply_button_filter = "//span[text() = 'Generar']"
        find_elements(self.driver, apply_button_filter)
        time.sleep(3)

        ## validar titulo de pantalla cuenta corriente aplicada 

        title_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-with-holdings-list/div[2]/div/div"
        title_account_expected = "Retenciones"
        validate_text(self.driver,title_account,title_account_expected )
       
       
        ## validar valores del listado 

        date_movements = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-with-holdings-list/p-table/div/div/table/tbody/tr[1]/td[1]"
        validate_character_string_element(self.driver,date_movements )


        number_certificate = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-with-holdings-list/p-table/div/div/table/tbody/tr[1]/td[2]"
        validate_character_numeric_element(self.driver,number_certificate )

        data_regime = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-with-holdings-list/p-table/div/div/table/tbody/tr[1]/td[3]"
        validate_character_string_element(self.driver,data_regime )

        data_tax = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-with-holdings-list/p-table/div/div/table/tbody/tr[1]/td[4]"
        validate_character_string_element(self.driver,data_tax )

        number_voucher  = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-with-holdings-list/p-table/div/div/table/tbody/tr[1]/td[5]"
        validate_character_string_element(self.driver,number_voucher )



        balance_ars = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-with-holdings-list/p-table/div/div/table/tbody/tr[1]/td[6]"
        validate_character_numeric_element(self.driver, balance_ars)


        balance_alicuota = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-with-holdings-list/p-table/div/div/table/tbody/tr[1]/td[7]"
        validate_character_numeric_element(self.driver, balance_alicuota)


        balance_withholdings = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-with-holdings-list/p-table/div/div/table/tbody/tr[1]/td[8]"
        validate_character_numeric_element(self.driver, balance_withholdings)
        

    
 

        

    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(cuenta_retenciones)
  runner = xmlrunner.XMLTestRunner(output='reportCatRetenciones')
  runner.run(test_suite)