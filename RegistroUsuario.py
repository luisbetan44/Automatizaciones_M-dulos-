from ast import Bytes
import time
import unittest
import xmlrunner
from selenium.webdriver.common.by import By
from StartSession2 import StartSession
from EmailGenerator import EmailGenerator
from selenium.webdriver.common.keys import Keys
from LoginSample import LoginSample
from Elements import displace_element, displace_element_clear_send_keys, find_elements, validate_text, validate_text_by_strt

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

        element1 = '/html/body/app-root/app-register-main/div/div[2]/div/div/app-register-form/div/div/div/div/div[1]/h5'
        value_expected1 = "Crear usuario"
        validate_text(self.driver, element1, value_expected1  )


        insert_email_new = "/html/body/app-root/app-register-main/div/div[2]/div/div/app-register-form/div/div/div/div/div[2]/form/div[1]/app-input/div[2]/input"
        send_email_new = test_email
        displace_element_clear_send_keys(self.driver,insert_email_new, send_email_new)
        time.sleep(2)

        insert_password_new = self.driver.find_element(By.ID,"password")
        insert_password_new.send_keys("Bet$123456")
        insert_password_new.send_keys(Keys.ENTER) 
        time.sleep(2)

        confirt_password_new = self.driver.find_element(By.ID,"passwordConfirmacion")
        confirt_password_new.send_keys("Bet$123456")
        confirt_password_new.send_keys(Keys.ENTER) 
        time.sleep(2)

        

        insert_user = "/html/body/app-root/app-register-main/div/div[2]/div/div/app-register-form/div/div/div/div/div[2]/form/div[4]/app-button/button"
        find_elements(self.driver, insert_user)
        time.sleep(2)

        messeger_checkin = "/html/body/app-root/app-register-main/div/div[2]/div/div/app-register-confirmation/div/div/div/div/div/p[1]"
        validate_text_by_strt(self.driver, messeger_checkin)



        self.register_user.close_session()

        # validar email 

        self.start_session = StartSession("https://yopmail.com/es/wm")
        self.driver = self.start_session.driver

        validate_email_new = "/html/body/div/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div[1]/div[2]/div/input"
        send_email_validate = test_email
        displace_element_clear_send_keys(self.driver,validate_email_new, send_email_validate)
        time.sleep(2)

        select_chevron = "/html/body/div/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div[1]/div[4]/button/i"
        find_elements(self.driver, select_chevron)
        time.sleep(2)

        element2 = '/html/body/header/div[3]/div[1]'
        value_expected2 = "Bienvenido a Gaviglio Digital"
        validate_text(self.driver, element2, value_expected2  )

        self.start_session.close_session()

        self.register_user = StartSession("https://pwa-portal-staging.silohub.ag/login")
        self.driver = self.register_user.driver
        time.sleep(3)

        self.login_sample = LoginSample(self.driver)

        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()

        select_menu_config = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[10]/a"
        find_elements(self.driver, select_menu_config)
        time.sleep(2)

        select_submenu_admin = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[10]/div/ul/li[1]/a"
        find_elements(self.driver, select_submenu_admin)
        time.sleep(2)

        validate_email_new2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-users-adm/div/input"
        send_email_validate2 = test_email
        displace_element_clear_send_keys(self.driver,validate_email_new2, send_email_validate2)
        time.sleep(2)
       
        search_email_admin = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-users-adm/div/span"
        find_elements(self.driver,  search_email_admin)
        time.sleep(2)


        validate_email_admin = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-users-adm/app-responsive-table/div/div[2]/table/tbody/tr/td[7]/div/button"
        find_elements(self.driver,  validate_email_admin)
        time.sleep(2)

        continue_email_admin = "/html/body/div/div/div[6]/button[3]"
        find_elements(self.driver,  continue_email_admin)
        time.sleep(2)

        element3 = '/html/body/div/div/h2'
        value_expected3 = "Email del usuario validado correctamente."
        validate_text(self.driver, element3, value_expected3  )

        accept_email_admin = "/html/body/div/div/div[6]/button[1]"
        find_elements(self.driver,  accept_email_admin)
        time.sleep(2)

        self.start_session.close_session()

        self.register_user = StartSession("https://pwa-portal-staging.silohub.ag/login")
        self.driver = self.register_user.driver
        time.sleep(3)

        self.login_sample = LoginSample(self.driver)

        self.login_sample.login(test_email, "Bet$123456")
        self.login_sample.select_tenant()

        into_login = "/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button"
        find_elements(self.driver,  into_login)
        time.sleep(2)

        element4 = '/html/body/div/div/h2/strong'
        value_expected4 = "Cuenta Pendiente de Vincular"
        validate_text(self.driver, element4, value_expected4  )


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRegistroUsuario)
    runner = xmlrunner.XMLTestRunner(output='reportRegistroUsuario')
    runner.run(test_suite)