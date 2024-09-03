import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import calendar_todate_retro, find_elements, validate_character_numeric_element_selector, validate_strt_selector, validate_text
from loginhelper import LoginHelper
from startSession import StartSession

class ReportinsumosPendRetirar(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_Report_suppliesWithdrawal(self):
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

        

        select_option_supplies = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-radio-button-list/div/app-radio[3]/div/input"
        find_elements(self.driver,select_option_supplies)
        time.sleep(2)

        # aplicar filtro de fecha actual a seis meses para atras 

        select_calendar = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-reports-options/app-date-filter/div/app-date-picker/div/input[2]"
        popup_xpath = "//div[contains(@class, 'flatpickr-calendar')]"
        select_chevron = "//span[@class='flatpickr-prev-month']"
        popup_xpath2 = "//div[contains(@class, 'flatpickr-calendar')]"
        click_chevron = 6
        calendar_todate_retro(self.driver, select_calendar, popup_xpath, select_chevron, popup_xpath2, clicks=click_chevron)
        time.sleep(2)

        apply_filter_supplies = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver,apply_filter_supplies)
        time.sleep(3)

        # validar titulo de la pantalla 

        title_page_supplies = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/div/div/div[1]"
        title_page_supplies_expected = "Insumos Pendientes de Retirar"
        validate_text(self.driver,title_page_supplies, title_page_supplies_expected )
        # validar numero de comprobante de primer  movimiento 

        column_voucher = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/div/table/thead/tr/th[2]"
        column_voucher_expected = "Comprobante"
        validate_text(self.driver,column_voucher, column_voucher_expected )

        list_movements1 = "#layout-wrapper > div > div > div > app-supplies-pending > app-responsive-table > div > div > table > tbody > tr:nth-child(1) > td.text-nowrap.align-middle.f-size-12.fw-bold.cursor-pointer.ellipsis-cell > span > div"
        validate_strt_selector(self.driver, "", list_movements1)

        # validar descripcion del articulo del primer movimiento
        column_article = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/div/table/thead/tr/th[3]"
        column_article_expected = "Artículo"
        validate_text(self.driver,column_article, column_article_expected )


        description_article1 ="#layout-wrapper > div > div > div > app-supplies-pending > app-responsive-table > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span > div > span"
        validate_strt_selector(self.driver, "", description_article1)

        # validar monto del primer movimiento pemdiente 
        column_pending = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/div/table/thead/tr/th[5]"
        column_pending_expected = "Cant. Pend."
        validate_text(self.driver,column_pending, column_pending_expected )


        pending_amount1 = "#layout-wrapper > div > div > div > app-supplies-pending > app-responsive-table > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > span > div > span"
        validate_character_numeric_element_selector(self.driver, pending_amount1 )

        

        # seleccionar movimientos del listado y descargar 

        select_first_movements ="/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/div/table/tbody/tr[1]/th/input"
        find_elements(self.driver,select_first_movements)

        select_second_movements = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-responsive-table/div/div/table/tbody/tr[2]/th/input"
        find_elements(self.driver,select_second_movements)

        # descargar movimientos seleccionados 

        select_button_download1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver,select_button_download1)
        time.sleep(2)

        download_option_Excel = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver,download_option_Excel)
        time.sleep(3)

        select_button_download2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver,select_button_download2)
        time.sleep(2)

        download_option_PDF = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-pending/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver,download_option_PDF)
        time.sleep(3)




    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(ReportinsumosPendRetirar)
  runner = xmlrunner.XMLTestRunner(output='reportInsuPendRetirar')
  runner.run(test_suite)
        