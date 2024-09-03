from telnetlib import EC
import unittest
import xmlrunner
import time
from Elements import  calendar_todate, find_elements, find_elements_id
from loginhelper import LoginHelper
from startSession import StartSession



class mis_intenciones(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_my_intentions(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

        select_grain = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span"
        find_elements(self.driver,select_grain)
        time.sleep(2)

        select_my_intentions = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[5]/a"
        find_elements(self.driver,select_my_intentions)
        time.sleep(2)

        # aplicar el filtro solo con los productos maiz y soja 

        select_button_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-intentions-list/app-header-for-responsive-table/div/div/div[2]/div/div/app-filter-button/button/div/span"
        find_elements(self.driver,select_button_filter)
        time.sleep(2)

        select_product1 = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[4]/div/img"
        find_elements(self.driver,select_product1)
        time.sleep(2)

        select_product2 = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[3]/div/img"
        find_elements(self.driver,select_product2)
        time.sleep(2)

        select_data_day = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        popup_calendar1 = "//div[contains(@class, 'flatpickr-calendar')]"
        calendar_todate(self.driver, select_data_day, popup_calendar1)
        time.sleep(2)

        appliy_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver,appliy_filter)
        time.sleep(2)

        select_movements_list1 = "Shape"
        find_elements_id(self.driver, select_movements_list1)
        time.sleep(2)

        select_button_process = "/html/body/ngb-modal-window/div/div/app-sales-intent-modal/div[2]/app-sales-intent-form/div/div[7]/app-button[2]/button"
        find_elements(self.driver, select_button_process)
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0,400);")
        time.sleep(2)

        select_button_next = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div/div[1]/section/form/div/div/div[16]/div/div[2]/app-button/button"
        find_elements(self.driver, select_button_next)
        time.sleep(3)

        select_button_continue = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div/div[1]/section/form/div/div/div[16]/div/div[2]/app-button/button"
        find_elements(self.driver, select_button_continue)
        time.sleep(2)

        select_button_cofirtm = "/html/body/div[3]/div/div[6]/button[3]"
        find_elements(self.driver, select_button_cofirtm)
        time.sleep(2)

        select_button_accept = "/html/body/div[3]/div/div[6]/button[3]"
        find_elements(self.driver, select_button_accept)
        time.sleep(2)

        select_button_accept = "/html/body/div/div/div[6]/button[1]"
        find_elements(self.driver, select_button_accept)
        time.sleep(2)


        


    def tearDown(self):
           self.driver.close()

if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(mis_intenciones)
  runner = xmlrunner.XMLTestRunner(output='reportGranosDashboardGranos')
  runner.run(test_suite)