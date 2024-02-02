import time
import unittest
import xmlrunner

from StartSession2 import StartSession
from EmailGenerator import EmailGenerator
from Elements import displace_element, displace_element_clear_send_keys, find_elements, make_send_visible_id

class TestRegistroUsuario(unittest.TestCase):
    def setUp(self):
        # Crea una instancia del navegador en la configuración inicial
        self.start_session = StartSession("https://yopmail.com/es/wm")
        self.driver = self.start_session.driver

    def test_register_user(self):
        # Abrir sesión en la página de generación de email

        # Generar un email de prueba
        test_email = EmailGenerator.generate_email()

        # Tomar el email generado
        print(f"Email generado: {test_email}")

        # Cerrar sesión en la página de generación de email
        self.start_session.close_session()

    
        self.register_user = StartSession("https://pwa-portal-staging.silohub.ag/login")
        self.driver = self.register_user.driver
        time.sleep(3)

        
 
        select_register = "/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[2]/p/a"
        displace_element(self.driver, select_register)
        time.sleep(3)


        insert_email_new = "/html/body/app-root/app-register-main/div/div[2]/div/div/app-register-form/div/div/div/div/div[2]/form/div[1]/app-input/div[2]/input"
        send_email_new = test_email
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

        

        insert_user = "/html/body/app-root/app-register-main/div/div[2]/div/div/app-register-form/div/div/div/div/div[2]/form/div[4]/app-button/button"
        find_elements(self.driver, insert_user)
        time.sleep(2)


        self.register_user.close_session()

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRegistroUsuario)
    runner = xmlrunner.XMLTestRunner(output='reportRegistroUsuario')
    runner.run(test_suite)