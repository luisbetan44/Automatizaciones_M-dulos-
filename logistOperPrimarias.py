import unittest
import time
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_elements, select_option_click, send_element, validate_text 
from Elements2 import verify_todate
from LoginSample import LoginSample
from startSession import StartSession



class logistOperPrimarias(unittest.TestCase):


    def    setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_Logistics_primary(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()
        

       

        select_menu_logistics = "//span[text() =' Logística']"
        find_elements(self.driver,select_menu_logistics )
        time.sleep(2)



        quota_request =  "//a[text()= ' Solicitud de Cupos ']"
        find_elements(self.driver, quota_request )
        time.sleep(2)

        select_input_account = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[1]/div/div[1]/div[2]/app-customer-searcher/ng-select/div/div/div[3]/input'
        send_account = '1023'
        send_element(self.driver, select_input_account, send_account )
        time.sleep(2)

        select_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[1]/div/div[1]/div[2]/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        find_elements(self.driver, select_account)
        time.sleep(2)

        button_dopdown1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[1]/div/div[2]/div[2]/div/div[1]/select"
        option_desired1 =  '//option[text() = " TRIGO "]'
        select_option_click(self.driver, button_dopdown1, option_desired1, )
        time.sleep(2)

        button_dopdown2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[1]/div/div[2]/div[2]/div/div[2]/select"
        option_desired2 =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[1]/div/div[2]/div[2]/div/div[2]/select/option[3]"
        select_option_click(self.driver, button_dopdown2, option_desired2, )
        time.sleep(2)

        button_dopdown3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[2]/div/div[1]/div[2]/select"
        option_desired3 =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[2]/div/div[1]/div[2]/select/option[8]"
        select_option_click(self.driver, button_dopdown3, option_desired3, )
        time.sleep(2)

        button_dopdown4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[2]/div/div[2]/div[2]/select"
        option_desired4 =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[2]/div/div[2]/div[2]/select/option[4]"
        select_option_click(self.driver, button_dopdown4, option_desired4, )
        time.sleep(2)

        select_quota1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-quotas/div/table/tbody/tr[1]/td[2]/input'
        send_quota1 = '10'
        send_element(self.driver, select_quota1, send_quota1 )
        time.sleep(2)

        select_quota2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-quotas/div/table/tbody/tr[2]/td[2]/input'
        send_quota2 = '20'
        send_element(self.driver, select_quota2, send_quota2 )
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        select_button_confirm = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/div/button[2]"
        find_elements(self.driver, select_button_confirm)
        time.sleep(5)

        select_button_accept = "/html/body/div[8]/div/div[6]/button[3]"
        find_elements(self.driver, select_button_accept)
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

        select_menu_myrequest = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[1]/ul/li[2]/a"
        find_elements(self.driver, select_menu_myrequest)

        select_input_account2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/div/div/div[2]/input'
        send_account2 = '1023'
        send_element(self.driver, select_input_account2, send_account2 )
        time.sleep(2)

        select_account2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        find_elements(self.driver, select_account2)
        time.sleep(5)

        select_todate = '//*[@id="current-account-file"]/app-my-reservations/div/table/tbody/tr[2]/td[4]'
        verify_todate(self.driver,select_todate)
        time.sleep(2)

        canceled_amount = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[2]/td[7]/div/div[1]"
        value_amount = "10"
        validate_text(self.driver, canceled_amount, value_amount)

        got_to_page = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver, got_to_page)
        time.sleep(3)




    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(logistOperPrimarias)
  runner = xmlrunner.XMLTestRunner(output='reportlogistOperPrimar')
  runner.run(test_suite)
        