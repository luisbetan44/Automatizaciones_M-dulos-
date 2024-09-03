import time
import unittest
import xmlrunner
from Elements import find_and_click_element, find_elements, validate_character_numeric_element, validate_text, validate_text_by_strt
from loginhelper import LoginHelper
from StartSessionFirefox import StartSessionFirefox


class cta_cte_pesiFechaCompro(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSessionFirefox()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_ctacte_date_voucher(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

        # ingresar al menú de cuentas 

        select_menu_contrat = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver, select_menu_contrat)

        select_account_menu = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[4]/a"
        find_elements(self.driver, select_account_menu)
        
        ## seleccionar cuenta corriente pasificado

        select_account = '//*[@id="current-account-pesified-tab"]'
        find_elements(self.driver, select_account)
        time.sleep(3)

        ## selecionar botón del filtro

        select_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-pesified-list/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/span"
        find_elements(self.driver, select_filter)
        time.sleep(2)


        ## seleccionar rango de fecha 01-01-2024 a 27/03/2024

        select_field_date = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        find_elements(self.driver, select_field_date)
        time.sleep(2)

        select_arrow_1 = "/html/body/div/div[1]/span[1]"
        clicks = 7
        find_and_click_element(self.driver, select_arrow_1, clicks)
        time.sleep(2)

        select_date_1 = "/html/body/div/div[2]/div/div[2]/div/span[1]"
        find_elements(self.driver, select_date_1)
        time.sleep(2)

        select_arrow_2 = "/html/body/div/div[1]/span[2]"
        clicks = 2
        find_and_click_element(self.driver, select_arrow_2, clicks)
        time.sleep(2)

        select_date_2 = "/html/body/div/div[2]/div/div[2]/div/span[31]"
        find_elements(self.driver, select_date_2)
        time.sleep(2)

        apply_button_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver,  apply_button_filter)
        time.sleep(2)

        ## validar titulo de pantalla cuenta corriente aplicada 

        title_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-pesified-list/div/div/div"
        title_account_expected = "Cuenta Pesificada"
        validate_text(self.driver,title_account,title_account_expected )
       
        ## validar totalizadores 



        ## validar saldos

        balance_ars = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-pesified-list/app-header-for-responsive-table/div/div/div[1]/div/div/app-totalizer/div/div/div[2]/div[2]/span[1]"
        validate_character_numeric_element(self.driver, balance_ars)


        


        ## seleccionar el segundo movimientos del lisatos 

        movements_list_1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-pesified-list/app-responsive-table/div/div/table/tbody/tr[2]/th/input"
        find_elements(self.driver, movements_list_1)
        

         ## seleccionar botón descargar  

        select_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-pesified-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, select_button)

        ## descargar Excel 

        download_Excel = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-pesified-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver, download_Excel)
        time.sleep(3)

       

        select_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-pesified-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, select_button)
        ## descargar Excel 

        download_PDF = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-pesified-list/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, download_PDF)
        time.sleep(3)


        ## ingresar al detalle del segundo movimiento 

        detail_movements4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-current-account/div/div/div[2]/app-current-account-pesified-list/app-responsive-table/div/div/table/tbody/tr[2]/td[2]/span/div"
        find_elements(self.driver, detail_movements4)
        time.sleep(3)

        ## validar titulo pantalla 
        title_detail = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        title_detail_expected = "CUENTA CORRIENTE"
        validate_text(self.driver,title_detail,title_detail_expected)

        ## validar datos del detalle 

        number_movements = "Movimiento FR 0055 00005555"
        validate_text_by_strt(self.driver, number_movements )


 
        balance_movements = "+ ARS 726.000,00"
        validate_text_by_strt(self.driver, balance_movements )

        settlement = "ventas de productos -"
        validate_text_by_strt(self.driver, settlement )

        ## Seleccionar salida al listado 

        go_out_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver, go_out_list)
        time.sleep(3)




    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(cta_cte_pesiFechaCompro)
  runner = xmlrunner.XMLTestRunner(output='reportCtacteApliApagar')
  runner.run(test_suite)