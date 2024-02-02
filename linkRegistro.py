import time
import unittest
import xmlrunner
from Elements import displace_element, displace_element_clear_send_keys,  make_send_visible_id
from startSession import StartSession


class link_register(unittest.TestCase):


    def    setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        time.sleep(3)
    
    def test_start_tenant(self):
        select_register = "/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[2]/p/a"
        displace_element(self.driver, select_register)
        time.sleep(3)

        insert_email_new = "/html/body/app-root/app-register-main/div/div[2]/div/div/app-register-form/div/div/div/div/div[2]/form/div[1]/app-input/div[2]/input"
        send_email_new = "luis@"
        displace_element_clear_send_keys(self.driver,insert_email_new, send_email_new)
        time.sleep(2)

        select_password_new = "password"
        insert_password_new = "Bet$123456"
        make_send_visible_id(self.driver, insert_password_new, select_password_new)
        time.sleep(2)

        confirt_password_new = "passwordConfirmacion"
        repeat_password_new = "Bet$123456"
        make_send_visible_id(self.driver, repeat_password_new, confirt_password_new)
        time.sleep(2)




    def tearDown(self):
        self.driver.quit()


   




if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(link_register)
  runner = xmlrunner.XMLTestRunner(output='reportlinkregritro')
  runner.run(test_suite)
        
   
