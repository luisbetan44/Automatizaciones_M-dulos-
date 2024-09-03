from telnetlib import EC
import unittest
import xmlrunner
import time
from Elements import  calendar_todate, find_elements
from loginhelper import LoginHelper
from SelectListDashboard import verify_text_and_click
from startSession import StartSession



class dashboard_granos(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_dashboard_grain(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

        select_grain = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span"
        find_elements(self.driver,select_grain)
        time.sleep(2)

        select_dashboard_grain = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[4]/a"
        find_elements(self.driver,select_dashboard_grain)
        time.sleep(2)

        # aplicar el filtro solo con los productos maiz y soja 

        select_button_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grain-dashboard/app-grain-dashboard-list/app-header-for-responsive-table/div/div/div[2]/div/div/app-filter-button/button/div/i"
        find_elements(self.driver,select_button_filter)
        time.sleep(2)

        select_product1 = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[4]/div/img"
        find_elements(self.driver,select_product1)
        time.sleep(2)

        select_product2 = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[6]/div/img"
        find_elements(self.driver,select_product2)
        time.sleep(2)

        select_data_day = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        popup_calendar1 = "//div[contains(@class, 'flatpickr-calendar')]"
        calendar_todate(self.driver, select_data_day, popup_calendar1)
        time.sleep(2)

        appliy_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver,appliy_filter)
        time.sleep(2)

        select_movements_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grain-dashboard/app-grain-dashboard-list/app-responsive-table/div/div/table/tbody/tr[1]/td[1]"
        validate_status1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr/td[5]/span/span/div/div[1]"
        select_dropdown_option1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr/td[5]/span/span/div/div[2]/button/i"
        select_option1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr/td[5]/span/span/div/div[2]/div/a[1]"
        validate_status2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr[2]/td[5]/span/span/div/div[1]"
        select_dropdown_option2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr[2]/td[5]/span/span/div/div[2]/button/i"
        select_option2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr[2]/td[5]/span/span/div/div[2]/div/a[1]"
        validate_status3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr[3]/td[5]/span/span/div/div[1]"
        select_dropdown_option3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr[3]/td[5]/span/span/div/div[2]/button/i"
        select_option3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr[3]/td[5]/span/span/div/div[2]/div/a[1]"
        select_go_to1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        verify_text_and_click(self.driver, select_movements_list, validate_status1, select_dropdown_option1, select_option1, validate_status2, select_dropdown_option2, select_option2, validate_status3, select_dropdown_option3, select_option3, select_go_to1)
        time.sleep(2)

        select_movements_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grain-dashboard/app-grain-dashboard-list/app-responsive-table/div/div/table/tbody/tr[2]/td[1]"
        validate_status1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr/td[5]/span/span/div/div[1]"
        select_dropdown_option1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr/td[5]/span/span/div/div[2]/button/i"
        select_option1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr/td[5]/span/span/div/div[2]/div/a[1]"
        validate_status2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr[2]/td[5]/span/span/div/div[1]"
        select_dropdown_option2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr[2]/td[5]/span/span/div/div[2]/button/i"
        select_option2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr[2]/td[5]/span/span/div/div[2]/div/a[1]"
        validate_status3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr[3]/td[5]/span/span/div/div[1]"
        select_dropdown_option3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr[3]/td[5]/span/span/div/div[2]/button/i"
        select_option3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-intentions-detail/app-responsive-table/div/div/table/tbody/tr[3]/td[5]/span/span/div/div[2]/div/a[1]"
        select_go_to1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        verify_text_and_click(self.driver, select_movements_list, validate_status1, select_dropdown_option1, select_option1, validate_status2, select_dropdown_option2, select_option2, validate_status3, select_dropdown_option3, select_option3, select_go_to1)
        time.sleep(2)

        select_button_accept = "/html/body/div[1]/div/div[6]/button[1]"
        find_elements(self.driver,select_button_accept)
        time.sleep(2)



    def tearDown(self):
           self.driver.close()

if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(dashboard_granos)
  runner = xmlrunner.XMLTestRunner(output='reportGranosDashboardGranos')
  runner.run(test_suite)
