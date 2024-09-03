import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_and_click_element_selector, find_elements, validate_character_numeric_element, validate_text
from loginhelper import LoginHelper
from startSession import StartSession

class reportenImpositivas(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_Report_tenImpositivas(self):
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

        select_holdings_tax = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-radio-button-list/div/app-radio[6]/div/input"
        find_elements(self.driver,select_holdings_tax)
        time.sleep(2)

        # aplicar rando de fecha 01/01/2024 

        select_date_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-reports-options/app-date-filter/div/app-date-picker/div/input[2]"
        find_elements(self.driver,select_date_filter)
        time.sleep(2)

        select_arrow_1 = "body > div > div.flatpickr-months > span.flatpickr-prev-month"
        clicks = 2
        find_and_click_element_selector(self.driver, select_arrow_1, clicks)
        time.sleep(2)

        
        select_date = "/html/body/div/div[2]/div/div[2]/div/span[1]"
        find_elements(self.driver, select_date)
        time.sleep(2)


        apply_button_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver, apply_button_filter)
        time.sleep(3)

         # validar título de la pantalla 

        title_page_tax = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/div[1]/div/div"
        title_page_tax_expected = "Tenencias Impositivas"
        validate_text(self.driver,title_page_tax,title_page_tax_expected )

        title_description_stock = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-responsive-table/div/div[1]/span"
        title_description_expected = "STOCK DE GRANOS NO LIQUIDADOS"
        validate_text(self.driver,title_description_stock,title_description_expected )

        # validar listado de movimientos 
        first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-responsive-table/div/div[2]/table/thead/tr/th[2]"
        first_column_expected = "Producto"
        validate_text(self.driver,first_column,first_column_expected )
        
        product_movements = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[1]/span/span"
        product_movements_expected = "MAIZ"
        validate_text(self.driver,product_movements,product_movements_expected )

        second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-responsive-table/div/div[2]/table/thead/tr/th[3]"
        second_column_expected = "Kg. Netos"
        validate_text(self.driver,second_column,second_column_expected )

        kilos_net = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[2]/span/span"
        validate_character_numeric_element(self.driver,kilos_net)

        third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-responsive-table/div/div[2]/table/thead/tr/th[4]"
        third_column_column_expected = "Campaña"
        validate_text(self.driver,third_column,third_column_column_expected )

        campaign_description2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[3]/span/span"
        campaign_description2_expected = "2223"
        validate_text(self.driver,campaign_description2,campaign_description2_expected )

        quarter_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-responsive-table/div/div[2]/table/thead/tr/th[5]"
        quarter_column_expected = "Kg. Pendientes Cert."
        validate_text(self.driver,quarter_column,quarter_column_expected )

        pending_kilos = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[4]/span/span"
        validate_character_numeric_element(self.driver,pending_kilos)
        
        # validar saldos de cuenta corriente 

        title_account_balance = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/div[2]/div[1]/div"
        title_description_expected = "SALDOS DE CUENTA CORRIENTE"
        validate_text(self.driver,title_account_balance,title_description_expected)

        balance_ARS = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/div[2]/div[2]/div[1]/app-totalizer-down/div/div/div/div[2]/span"
        validate_character_numeric_element(self.driver,balance_ARS)

        balance_USD = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/div[2]/div[2]/div[2]/app-totalizer-down/div/div/div/div[2]/span"
        validate_character_numeric_element(self.driver,balance_USD)

        balance_accountant = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/div[2]/div[2]/div[3]/app-totalizer-down/div/div/div/div[2]/span"
        validate_character_numeric_element(self.driver,balance_accountant)

           
       # descargar compromabtes 

        selecct_moviments_list1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-responsive-table/div/div[2]/table/tbody/tr[1]/th/input"
        find_elements(self.driver, selecct_moviments_list1)

        selecct_moviments_list2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-responsive-table/div/div[2]/table/tbody/tr[2]/th/input"
        find_elements(self.driver, selecct_moviments_list2)

        selecct_moviments_list3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-responsive-table/div/div[2]/table/tbody/tr[3]/th/input"
        find_elements(self.driver, selecct_moviments_list3)

        dowlnload_button1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, dowlnload_button1)

        selecct_option1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver, selecct_option1)
        time.sleep(2)

        dowlnload_button2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, dowlnload_button2)

        selecct_option2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, selecct_option2)
        time.sleep(5)

        dowlnload_button3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, dowlnload_button3)

        selecct_option3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-tax-holdings/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[3]/a"
        find_elements(self.driver, selecct_option3)
        time.sleep(5)

       

        




    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(reportenImpositivas)
  runner = xmlrunner.XMLTestRunner(output='reportenImpositivas')
  runner.run(test_suite)
