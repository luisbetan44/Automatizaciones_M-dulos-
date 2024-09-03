import unittest
import time
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
import xmlrunner
from Elements import find_elements,  find_send_element_selector, select_option_click,  validate_text
from LoginSample import LoginSample
from startSession import StartSession


class Perfil_Usuario(unittest.TestCase):


    def    setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_Profile_User(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()
        

       

        select_profile = '/html/body/app-root/app-layout/app-vertical/div/app-topbar/header/div/div/div[2]/app-profile/div/button/span/img'
        find_elements(self.driver,select_profile )
        time.sleep(2)



        select_my_profile = '/html/body/app-root/app-layout/app-vertical/div/app-topbar/header/div/div/div[2]/app-profile/div/div/div[2]/button'
        find_elements(self.driver,select_my_profile )
        time.sleep(2)


        ## validar que estamos en mis datos 
        title_page = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        value_expected = "MIS DATOS"
        validate_text(self.driver, title_page, value_expected  )

        data_person = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-left-side/app-personal-data-section/div/span"
        value_expected = "Datos personales"
        validate_text(self.driver, data_person, value_expected  )


       ## ingresar valores al formulario 
        

        insert_name = "#layout-wrapper > div > div > div > app-my-profile > div > div.bg-white.rounded.border.pb-2.container-card > div > app-form-profile-left-side > app-personal-data-section > div > form > div:nth-child(1) > div.col-9.col-sm-10 > input"
        send_name = "Administrador"
        find_send_element_selector(self.driver,  insert_name, send_name )
        time.sleep(2)

        insert_lastname = "#layout-wrapper > div > div > div > app-my-profile > div > div.bg-white.rounded.border.pb-2.container-card > div > app-form-profile-left-side > app-personal-data-section > div > form > div:nth-child(2) > div.col-9.col-sm-10 > input"
        send_lastname = "Silohub"
        find_send_element_selector(self.driver,  insert_lastname, send_lastname )
        time.sleep(2)

        select_sex = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-left-side/app-personal-data-section/div/form/div[3]/div[2]/select"
        option_sex = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-left-side/app-personal-data-section/div/form/div[3]/div[2]/select/option[1]"
        select_option_click(self.driver, select_sex, option_sex)
        time.sleep(2)


        select_date = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-left-side/app-personal-data-section/div/form/div[4]/div[2]/app-date-picker/div/input[2]"
        find_elements(self.driver,  select_date )
        time.sleep(2)

        
        select_date1 = "/html/body/div/div[2]/div/div[2]/div/span[18]"
        find_elements(self.driver, select_date1)
        time.sleep(2)

    

        insert_nationality = '#layout-wrapper > div > div > div > app-my-profile > div > div.bg-white.rounded.border.pb-2.container-card > div > app-form-profile-left-side > app-personal-data-section > div > form > div:nth-child(5) > div.col-9.col-sm-10 > input'
        send_nationality = "Argentina"
        find_send_element_selector(self.driver,  insert_nationality, send_nationality )
        time.sleep(2)

        insert_number_cuit = "#layout-wrapper > div > div > div > app-my-profile > div > div.bg-white.rounded.border.pb-2.container-card > div > app-form-profile-left-side > app-personal-data-section > div > form > div:nth-child(6) > div.col-9.col-sm-10 > input"
        send_number_cuit = "32965824529"
        find_send_element_selector(self.driver,  insert_number_cuit, send_number_cuit )
        time.sleep(2)

        insert_number_dni = "#layout-wrapper > div > div > div > app-my-profile > div > div.bg-white.rounded.border.pb-2.container-card > div > app-form-profile-left-side > app-personal-data-section > div > form > div:nth-child(7) > div.col-9.col-sm-10 > input"
        send_number_dni = "95362132"
        find_send_element_selector(self.driver,  insert_number_dni, send_number_dni )
        time.sleep(2)

        select_country = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-right-side/form/app-address-section/form/app-country-selector/div/div[2]/select"
        option_country = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-right-side/form/app-address-section/form/app-country-selector/div/div[2]/select/option[12]"
        select_option_click(self.driver, select_country, option_country)
        time.sleep(2)

        select_province = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-right-side/form/app-address-section/form/app-province-selector/div/div[2]/select"
        option_province = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-right-side/form/app-address-section/form/app-province-selector/div/div[2]/select/option[2]"
        select_option_click(self.driver, select_province, option_province)
        time.sleep(2)

        select_locate = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-right-side/form/app-address-section/form/app-location-selector/div/div[2]/select"
        option_locate = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-right-side/form/app-address-section/form/app-location-selector/div/div[2]/select/option[4]"
        select_option_click(self.driver, select_locate, option_locate)
        time.sleep(2)

        select_branch = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-right-side/form/app-address-section/form/app-branch-office-selector/div/div[2]/select"
        option_branch = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-right-side/form/app-address-section/form/app-branch-office-selector/div/div[2]/select/option[4]"
        select_option_click(self.driver, select_branch, option_branch)
        time.sleep(2)

        insert_email = "#layout-wrapper > div > div > div > app-my-profile > div > div.bg-white.rounded.border.pb-2.container-card > div > app-form-profile-right-side > form > app-contact-section > div > form > div > div.col-9.col-sm-10.f-size-12 > input"
        send_enail = "admingd@silohub.ag"
        find_send_element_selector(self.driver,  insert_email, send_enail )
        time.sleep(2)

        select_rol = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-right-side/form/app-contact-section/div/form/app-role-selector/div/div[2]/select"
        option_rol = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[1]/div/app-form-profile-right-side/form/app-contact-section/div/form/app-role-selector/div/div[2]/select/option[2]"
        select_option_click(self.driver, select_rol, option_rol)
        time.sleep(2)

        
        insert_number = "#layout-wrapper > div > div > div > app-my-profile > div > div.bg-white.rounded.border.pb-2.container-card > div > app-form-profile-right-side > form > app-contact-section > div > form > app-input-phone:nth-child(4) > form > div > div.col-5.col-sm-7.f-size-12 > input"
        send_number = "91136624156"
        find_send_element_selector(self.driver,  insert_number, send_number )
        time.sleep(2)

        select_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-my-profile/div/div[2]/div[2]/button"
        find_elements(self.driver, select_button)
        time.sleep(2)

        print("Perfil guardado con éxito")
        time.sleep(2)


    
    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(Perfil_Usuario)
  runner = xmlrunner.XMLTestRunner(output='reportProfileUser')
  runner.run(test_suite)