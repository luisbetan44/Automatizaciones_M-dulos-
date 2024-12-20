import time
import unittest
import xmlrunner
from Elements import calendar_todate_retro,find_elements, find_elements_id, validate_character_numeric_element, validate_text
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession


class cuenta_ctacte_histVencidoV2(unittest.TestCase):
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

        select_menu_account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver, select_menu_account)
        ## seleccionar cuenta corriente

        select_current_account = "//a[text()=' Cuenta Corriente ']"
        find_elements(self.driver, select_current_account)
        time.sleep(3)

        select_tab_current_account = "current-account-file-tab"
        find_elements_id(self.driver, select_tab_current_account)

        ## selecionar botón del filtro

        select_filter = "//span[text()=' Filtros ' ]"
        find_elements(self.driver, select_filter)

          ## aplicar filtro de rubros

        apply_filter_1 = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-agricultural-category-container/div/app-agricultural-category-button[1]/div/img"
        find_elements(self.driver, apply_filter_1)
        time.sleep(2)

        

        apply_state = "Vencido" 
        find_elements_id(self.driver, apply_state)

        
        # aplicar filtro de fecha actual a seis meses para atras 

        select_calendar = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        popup_xpath = "//div[contains(@class, 'flatpickr-calendar')]"
        select_chevron = "//span[@class='flatpickr-prev-month']"
        popup_xpath2 = "//div[contains(@class, 'flatpickr-calendar')]"
        click_chevron = 6
        calendar_todate_retro(self.driver, select_calendar, popup_xpath, select_chevron, popup_xpath2, clicks=click_chevron)
        time.sleep(2)


        apply_button_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver, apply_button_filter)
        time.sleep(3)

        ## validar titulo de pantalla cuenta corriente aplicada 

        title_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-file-list/div/div/div"
        title_account_expected = "Cuenta Corriente"
        validate_text(self.driver,title_account,title_account_expected )
        ## validar totalizadores 



        balance_ars = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-file-list/app-header-for-responsive-table/div/div/div[1]/div/div[1]/app-totalizer/div/div/div[2]/div[2]/span[1]"
        validate_character_numeric_element(self.driver, balance_ars)


        balance_usd = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-file-list/app-header-for-responsive-table/div/div/div[1]/div/div[2]/app-totalizer/div/div/div[2]/div[2]/span[1]"
        validate_character_numeric_element(self.driver, balance_usd)


        ## seleccionar movimientos del lisatos 

        movements_list_1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-file-list/app-responsive-table/div/div/table/tbody/tr[1]/th/input"
        find_elements(self.driver, movements_list_1)

        movements_list_2 =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-file-list/app-responsive-table/div/div/table/tbody/tr[2]/th/input"
        find_elements(self.driver, movements_list_2)

        movements_list_3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-file-list/app-responsive-table/div/div/table/tbody/tr[3]/th/input"
        find_elements(self.driver, movements_list_3)
        time.sleep(2)

        
       ## seleccionar botón descargar  

        select_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-file-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver,   select_button)
        time.sleep(2)

        ## descargar Excel 

        download_Excel = "//a[contains(text(), 'Descargar a Excel')]"
        find_elements(self.driver, download_Excel)
        time.sleep(3)

        ## seleccionar botón descargar  


        select_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-file-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver,   select_button)
        
        ## descargar PDF 

        download_PDF = "//a[contains(text(), 'Descargar listado')]"
        find_elements(self.driver, download_PDF)
        time.sleep(3)


        ## ingresar al detalle  del tercer movimiento

        detail_movements = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div/app-current-account-file-list/app-responsive-table/div/div/table/tbody/tr[3]/td[1]/span/div"
        find_elements(self.driver, detail_movements)
        time.sleep(3)

        ## validar titulo pantalla 
        title_detail = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        title_detail_expected = "CUENTA CORRIENTE"
        validate_text(self.driver,title_detail,title_detail_expected)

        ## validar datos del detalle 

        number_movements = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[1]/div"
        validate_character_string_element(self.driver,number_movements )

        balance_movements = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[2]/div/div[2]/div[1]"
        validate_character_string_element(self.driver, balance_movements )


        settlement = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[2]/div/div[2]/div[2]"
        validate_character_string_element(self.driver,  settlement )

        ## Seleccionar salida al listado 

        go_out_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver, go_out_list)
        time.sleep(3)

 

        

    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(cuenta_ctacte_histVencidoV2)
  runner = xmlrunner.XMLTestRunner(output='reportCtacteHistVencidoV2')
  runner.run(test_suite)