import time
import unittest
import xmlrunner
from Elements import find_and_click_element, find_and_click_element_selector, find_elements, validate_character_numeric_element, validate_text
from loginhelper import LoginHelper
from startSession import StartSession

class reportUsuarios(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_Report_user(self):
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

        select_report_user = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-radio-button-list/div/app-radio[7]/div/input"
        find_elements(self.driver,select_report_user)
        time.sleep(2)

        # aplicar rando de fecha 01/01/2024 al 15/03/2024

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

        select_arrow_2 = "/html/body/div/div[1]/span[2]"
        clicks = 2
        find_and_click_element(self.driver, select_arrow_2, clicks)
        time.sleep(2)

        
        select_date = "/html/body/div/div[2]/div/div[2]/div/span[19]"
        find_elements(self.driver, select_date)
        time.sleep(2)


        apply_button_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver, apply_button_filter)
        time.sleep(3)

         # validar título de la pantalla 

        title_page_user = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-report-users/app-responsive-table/div/div[1]/span"
        title_page_user_expected = "Reporte de usuarios"
        validate_text(self.driver,title_page_user,title_page_user_expected )

        
        # validar listado de movimientos 
        first_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-report-users/app-responsive-table/div/div[2]/table/thead/tr/th[1]"
        first_column_expected = "Correo Electrónico"
        validate_text(self.driver,first_column,first_column_expected )
        
        email_user = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-report-users/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[1]/span/span"
        email_user_expected = "fernando@silohub.ag"
        validate_text(self.driver,email_user,email_user_expected )

        second_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-report-users/app-responsive-table/div/div[2]/table/thead/tr/th[2]"
        second_column_expected = "Rol"
        validate_text(self.driver,second_column,second_column_expected )

        rol_user = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-report-users/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[2]/span/span"
        rol_user_expected = "Admin"
        validate_text(self.driver,rol_user,rol_user_expected )

        third_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-report-users/app-responsive-table/div/div[2]/table/thead/tr/th[3]"
        third_column_column_expected = "Fecha de Registro"
        validate_text(self.driver,third_column,third_column_column_expected )

        date_record = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-report-users/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[3]/span/span"
        date_record_expected = "03/01/2023 10:52:46"
        validate_text(self.driver,date_record,date_record_expected )

        quarter_column = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-report-users/app-responsive-table/div/div[2]/table/thead/tr/th[5]"
        quarter_column_expected = "Ult.Login"
        validate_text(self.driver,quarter_column,quarter_column_expected )

        pending_kilos = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-report-users/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[5]/span/span"
        validate_character_numeric_element(self.driver,pending_kilos)
        
        
       # descargar compromabtes 
 
        dowlnload_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-report-users/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-button/button"
        find_elements(self.driver, dowlnload_button)
        time.sleep(5)

        

    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(reportUsuarios)
  runner = xmlrunner.XMLTestRunner(output='reportUsuarios')
  runner.run(test_suite)
