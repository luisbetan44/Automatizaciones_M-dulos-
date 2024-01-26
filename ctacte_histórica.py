import time
import unittest
import xmlrunner
from Elements import find_and_click_element, find_elements, validate_character_numeric_element, validate_text
from loginhelper import LoginHelper
from startSession import StartSession


class cuenta_ctacte_historica(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_ctacte_historica(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

        # ingresar al menú de cuentas 

        select_menu_contrat = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver, select_menu_contrat)
        
        ## seleccionar cuenta corriente

        select_account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[4]/a"
        find_elements(self.driver, select_account)
        time.sleep(3)

     

        

        ## seleccionar solapa cta cte historica 

        select_account_history = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/ul/li[2]/a"
        find_elements(self.driver, select_account_history)
        ## selecionar botón del filtro

        select_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/span"
        find_elements(self.driver, select_filter)
        time.sleep(2)

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

        ## seleccionar filtro ordenado por 

        older_by_expiration = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-radio-button-list[1]/div/app-radio[2]/div/input"
        find_elements(self.driver,   older_by_expiration)

        ## seleccionar rango de fecha

        select_field_date = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        find_elements(self.driver,   select_field_date)
        time.sleep(2)

      
        select_arrow_1 = "/html/body/div/div[1]/span[1]"
        clicks = 9
        find_and_click_element(self.driver, select_arrow_1, clicks)
        time.sleep(2)

        select_date_1 = "/html/body/div/div[2]/div/div[2]/div/span[6]"
        find_elements(self.driver, select_date_1)
        time.sleep(2)


        select_arrow_2 = "/html/body/div/div[1]/span[2]"
        clicks = 1
        find_and_click_element(self.driver, select_arrow_2, clicks)
        time.sleep(2)

        select_date_2 ="/html/body/div/div[2]/div/div[2]/div/span[31]"
        find_elements(self.driver, select_date_2)
        time.sleep(2)

        apply_button_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver, apply_button_filter)
        time.sleep(3)

        ## validar titulo de pantalla cuenta corriente aplicada 

        title_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        title_account_expected = "CUENTA CORRIENTE"
        validate_text(self.driver,title_account,title_account_expected )
        ## validar totalizadores 



        balance_ars = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[1]/div/div[1]/app-totalizer/div/div/div[2]/div[2]/span[1]"
        validate_character_numeric_element(self.driver, balance_ars)


        balance_usd = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[1]/div/div[2]/app-totalizer/div/div/div[2]/div[2]/span[1]"
        validate_character_numeric_element(self.driver, balance_usd)


        ## seleccionar movimientos del lisatos 

        movements_list_1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-responsive-table/div/div/table/tbody/tr[1]/th/input"
        find_elements(self.driver, movements_list_1)

        movements_list_2 =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-responsive-table/div/div/table/tbody/tr[2]/th/input"
        find_elements(self.driver, movements_list_2)

        movements_list_3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-responsive-table/div/div/table/tbody/tr[3]/th/input"
        find_elements(self.driver, movements_list_3)

        movements_list_4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-responsive-table/div/div/table/tbody/tr[4]/th/input"
        find_elements(self.driver, movements_list_4)
      
       ## seleccionar botón descargar  

        select_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver,   select_button)

        ## descargar Excel 

        download_Excel = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver, download_Excel)
        time.sleep(3)

        ## descargar PDF 

        select_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver,  select_button)

        ## descargar Excel 

        download_PDF = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, download_PDF)
        time.sleep(3)


        ## ingresar al detalle 

        detail_movements = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-file-list/app-responsive-table/div/div/table/tbody/tr[4]/td[2]"
        find_elements(self.driver, detail_movements)
        time.sleep(3)

        ## validar titulo pantalla 
        title_detail = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        title_detail_expected = "CUENTA CORRIENTE"
        validate_text(self.driver,title_detail,title_detail_expected)

        ## validar datos del detalle 

        number_movements = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[1]/div"
        number_movements_expected = "Movimiento RI 0011 00077998"
        validate_text(self.driver,number_movements,number_movements_expected )

        balance_movements = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[2]/div/div[2]/div[1]"
        balance_movements_expected = "+ ARS 1.234,20"
        validate_text(self.driver, balance_movements, balance_movements_expected )


        settlement = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account-detail/app-header-for-detail/div[2]/div/div[2]/div[2]"
        settlement_expected = "Comprobante Contrapartida de: OP 0001 - 00038025 0"
        validate_text(self.driver,  settlement, settlement_expected )

        ## Seleccionar salida al listado 

        go_out_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver, go_out_list)
        time.sleep(3)



        

    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(cuenta_ctacte_historica)
  runner = xmlrunner.XMLTestRunner(output='reportCtacteHistorica')
  runner.run(test_suite)