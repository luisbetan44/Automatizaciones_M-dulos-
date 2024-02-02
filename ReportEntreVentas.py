import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_elements, validate_character_numeric_element, validate_character_numeric_element_selector, validate_text
from loginhelper import LoginHelper
from startSession import StartSession

class reportEntregasVentas(unittest.TestCase):
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

        select_menu_reports ="/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[6]/a"
        find_elements(self.driver,select_menu_reports)

        # seleccionar el filtro 

        select_filter_reports = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-reports/div/app-header-for-responsive-table/div/div/div[2]/div/div/app-filter-button/button/div/span"
        find_elements(self.driver,select_filter_reports)
        time.sleep(2)


        select_deliveries_sales = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-radio-button-list/div/app-radio[2]/div/input"
        find_elements(self.driver,select_deliveries_sales)
        time.sleep(2)

        select_filter_product = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[1]/div/img"
        find_elements(self.driver, select_filter_product)


        select_Campaign_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[1]/div/div"
        find_elements(self.driver, select_Campaign_filter)


        apply_filter_button = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver, apply_filter_button)

        time.sleep(3)

        # validar formatos de reportes de entregas y ventas 

        title_deliveries_sales = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div/span"
        title_deliveries_sales_expected = "Entregas y Ventas"
        validate_text(self.driver,title_deliveries_sales, title_deliveries_sales_expected )

        selected_grain = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[1]/div[1]/span"
        selected_grain_expected = "Soja"
        validate_text(self.driver, selected_grain, selected_grain_expected )

        selected_campaign = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[1]/div[2]/span"
        selected_campaign_expected = "23/24"
        validate_text(self.driver, selected_campaign, selected_campaign_expected )

        kilos_delivered = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[1]/span/span"
        kilos_delivered_expected = "Kilos Entregados"
        validate_text(self.driver, kilos_delivered, kilos_delivered_expected )

        total_delivered = "#layout-wrapper > div > div > div > sales-deliveries > app-responsive-table > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(2) > span > span"
        validate_character_numeric_element_selector(self.driver,total_delivered,)


        other_movenment = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[2]/table/tbody/tr[2]/td[1]/span/span'
        other_movenment_expected = "Otros Movimientos"
        validate_text(self.driver, other_movenment, other_movenment_expected )

        total_other_movenment = "#layout-wrapper > div > div > div > sales-deliveries > app-responsive-table > div > div.table-responsive > table > tbody > tr:nth-child(2) > td:nth-child(2) > span > span"
        validate_character_numeric_element_selector(self.driver,total_other_movenment)

        kilos_sales = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[2]/table/tbody/tr[3]/td[1]/span/span" 
        kilos_sales_expected = "Kilos Vendidos"
        validate_text(self.driver,  kilos_sales, kilos_sales_expected )

        total_sales = "#layout-wrapper > div > div > div > sales-deliveries > app-responsive-table > div > div.table-responsive > table > tbody > tr:nth-child(3) > td:nth-child(2) > span > span"
        validate_character_numeric_element_selector(self.driver,total_sales)

        kilos_requested = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[2]/table/tbody/tr[4]/td[1]/span/span"
        kilos_requested_expected = "Kilos Solicitados"
        validate_text(self.driver,  kilos_requested, kilos_requested_expected )

        total_requested = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[2]/table/tbody/tr[4]/td[2]/span/span"
        validate_character_numeric_element(self.driver,total_requested)


        kilos_pinup = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[2]/table/tbody/tr[5]/td[1]/span/span"
        kilos_pinup_expected = "Kilos a Fijar"
        validate_text(self.driver,  kilos_pinup, kilos_pinup_expected )

        total_pinup = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[2]/table/tbody/tr[5]/td[2]/span/span"
        validate_character_numeric_element(self.driver,total_pinup)

        movement_balance = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[2]/table/tbody/tr[6]/td[1]/span/span"
        movement_balance_expected = "Saldo"
        validate_text(self.driver,  movement_balance, movement_balance_expected )

        total_balance = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[2]/table/tbody/tr[6]/td[2]/span/span"
        validate_character_numeric_element(self.driver,total_balance)

        balance_commercial = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[2]/table/tbody/tr[7]/td[1]/span/span"
        balance_commercial_expected = "Saldo Comercial"
        validate_text(self.driver,  balance_commercial, balance_commercial_expected )

        total_balance_commercial = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div[2]/table/tbody/tr[7]/td[2]/span/span"
        validate_character_numeric_element(self.driver,total_balance_commercial)


         # descargar movimientos 

        select_button_downloads1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, select_button_downloads1)
        time.sleep(2)

        select_option_excel = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver, select_option_excel)
        time.sleep(10)

        select_button_downloads2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, select_button_downloads2)
        time.sleep(2)

        select_option_pdf = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, select_option_pdf)
        time.sleep(10)

        go_out_reports = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver, go_out_reports)
        time.sleep(3)







    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(reportEntregasVentas)
  runner = xmlrunner.XMLTestRunner(output='reportEntregasVentas')
  runner.run(test_suite)
        

 