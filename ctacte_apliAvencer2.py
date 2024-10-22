import time
import unittest
import xmlrunner
from Elements import calendar_todate_retro,  find_elements, find_elements_id, validate_character_numeric_element, validate_text
from Elements2 import validate_character_string_element
from loginhelper import LoginHelper
from startSession import StartSession


class cta_cte_apliAvencerV2(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_ctacte_apliAvencer(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

        # ingresar al menú de cuentas 

        select_menu_contrat = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver, select_menu_contrat)
        ## seleccionar cuenta corriente

        select_account = "//a[text()=' Cuenta Corriente ']"
        find_elements(self.driver, select_account)
        time.sleep(3)

        ## selecionar botón del filtro

        select_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/span"
        find_elements(self.driver, select_filter)
        time.sleep(2)

         ## aplicar filtro de los ultimos seis meses 

         ## aplicar filtro de rubros 

        apply_filter_1 = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-agricultural-category-container/div/app-agricultural-category-button[1]/div/img"
        find_elements(self.driver, apply_filter_1)
        time.sleep(2)

        apply_filter_2 = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-agricultural-category-container/div/app-agricultural-category-button[2]/div/img"
        find_elements(self.driver, apply_filter_2)
        time.sleep(2)

        apply_filter_3 = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-agricultural-category-container/div/app-agricultural-category-button[3]/div/img"
        find_elements(self.driver, apply_filter_3)
        time.sleep(2)

        apply_state = "A Vencer" 
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
        find_elements(self.driver,  apply_button_filter)
        time.sleep(2)

        ## validar titulo de pantalla cuenta corriente aplicada 

        title_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/div/div/div[1]"
        title_account_expected = "Cuenta Corriente Aplicada"
        validate_text(self.driver,title_account,title_account_expected )
        ## validar totalizadores 


        total_to_pay = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[1]/div/div[1]/app-totalizer/div/div[1]/div[2]/div[2]/span[1]'
        validate_character_numeric_element(self.driver, total_to_pay)

        ## validar saldos

        balance_ars = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[1]/div/div[2]/app-totalizer/div/div/div[2]/div[2]"
        validate_character_numeric_element(self.driver, balance_ars)


        balance_usd = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[1]/div/div[3]/app-totalizer/div/div/div[2]/div[2]"
        validate_character_numeric_element(self.driver, balance_usd)


        ## seleccionar el segundo movimientos del lisatos 

        movements_list_1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-responsive-table/div/div/table/tbody/tr[3]/th/input"
        find_elements(self.driver, movements_list_1)
        

         ## seleccionar botón descargar  

        select_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, select_button)

        ## descargar Excel 

        download_Excel = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver, download_Excel)
        time.sleep(3)

       

        select_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, select_button)
        ## descargar Excel 

        download_PDF = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, download_PDF)
        time.sleep(3)


        ## ingresar al detalle 

        detail_movements4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[1]/app-current-account-applied-list/app-responsive-table/div/div/table/tbody/tr[3]/td[2]"
        find_elements(self.driver, detail_movements4)
        time.sleep(3)

        ## validar titulo pantalla 
        title_detail = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        title_detail_expected = "CUENTA CORRIENTE"
        validate_text(self.driver,title_detail,title_detail_expected)

        ## validar datos del detalle 

        number_movements = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[1]/div"
        validate_character_string_element(self.driver, number_movements )


 
        balance_movements = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[2]/div/div[2]/div[1]"
        validate_character_string_element(self.driver, balance_movements )

        settlement = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[2]/div/div[2]/div[2]"
        validate_character_string_element(self.driver, settlement )

        ## Seleccionar salida al listado 

        go_out_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver, go_out_list)
        time.sleep(3)




    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(cta_cte_apliAvencerV2)
  runner = xmlrunner.XMLTestRunner(output='reportCtacteApliAvencerV2')
  runner.run(test_suite)