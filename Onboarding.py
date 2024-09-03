

import unittest
from  GeneradorDNI import generar_dni
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from faker import Faker
import xmlrunner
from selenium.common.exceptions import StaleElementReferenceException
from Elements import click_checkbox_xpaht, find_elements, find_elements_id,  upload_file_after_click, upload_file_after_click_selector, validate_text_visible
from GeneradorCuit import CUITGenerator
from LoginSample import LoginSample
from startSession import StartSession 


class Onboarding_test_tenant(unittest.TestCase):
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_Sample = LoginSample(self.driver)
   
   
    def test_tenat_onboarding(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_Sample.login("luismiguel@alternativasinteligentes.com", "Bet$123456")
        self.login_Sample.select_tenant()
        
      
        select_popup = "/html/body/div/div/div[6]/button[1]"
        find_elements(self.driver,select_popup)

        select_config = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span"
        find_elements(self.driver,select_config)

        select_document = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[8]/a"
        find_elements(self.driver, select_document)
        time.sleep(3)

        

        # validar el titulo de la pantalle documentación

        element_1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        text_expected = "DOCUMENTACIÓN"
        validate_text_visible(self.driver, element_1, text_expected)

        select_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-main/div/div[3]/app-button/button"
        find_elements(self.driver, select_button)

        agregar_onboarding = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-docket-list/div/div[1]/div/div/div/app-button/button"
        find_elements(self.driver, agregar_onboarding)


        # validar mensaje de la pantalla
        element_2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[1]/div/span"
        text_expected2 = "Para poder continuar al siguiente paso, será obligatorio completar los campos que se muestran a continuación."
        validate_text_visible(self.driver, element_2, text_expected2)

        # llenar formulario

       
        input_xpath = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[2]/div[1]/app-input-for-long-form[1]/div[1]/div[2]/div/input'
        error_css_selector = '#layout-wrapper > div > div > div > app-documentation-process > div > div > aw-wizard > div > app-account-type > div > div.form-container.bg-white.p-3.mt-3.col-12 > div.row.justify-content-center > app-input-for-long-form:nth-child(1) > div.row.align-items-center.mb-2.f-size-12 > app-alerts > div > span'
        cuit = CUITGenerator.insert_valid_cuit(self.driver, input_xpath, error_css_selector)
        print(f"CUIT válido insertado: {cuit}")
        
        
        insert_razon_social = self.driver.find_element(By.XPATH,
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[2]/div[1]/app-input-for-long-form[2]/div/div[2]/div/input"
        )

        fake = Faker()
        nombre = fake.name()

        insert_razon_social.send_keys(nombre)
        insert_razon_social.send_keys(Keys.ENTER)

        select_radio = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[2]/div[2]/div[1]/app-radio[1]/div/input"
        find_elements(self.driver, select_radio)
        time.sleep(2)

        selecct_sucesion = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[2]/div[2]/div[2]/div/input"
        find_elements(self.driver, selecct_sucesion)
        time.sleep(2)

        # cargar archivos

        select_field = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[2]/div[4]/app-acordion-for-upload/div/div/h2/button'
        element_archive_1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[2]/div[4]/app-acordion-for-upload/div/div/h2/button/app-upload-input/div/div[2]/input'
        archive = 'C:/Users/luist/OneDrive/Escritorio/Facturas/Contratos-1023-JUAN DEMO.xls'
        upload_file_after_click(self.driver,select_field, element_archive_1, archive)
        time.sleep(3)

    
        check_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[3]/app-checks/div/input"
        click_checkbox_xpaht(self.driver, check_button)
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)


        continue_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[3]/div/div/app-button/button" 
        find_elements(self.driver, continue_button)
        time.sleep(5)

        insert_document = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-identity-validation/div/div[3]/app-button/button"
        find_elements(self.driver, insert_document)
        time.sleep(2)

        

        photo_person1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-identity-front/app-identification-upload-manager/div/div[3]/div/app-button[1]/button"
        find_elements(self.driver, photo_person1)
        time.sleep(3)

        

        take_photo = "Icon:_Take_photo"
        find_elements_id(self.driver, take_photo)
        time.sleep(3)

        continue1_button = "/html/body/ngb-modal-window/div/div/app-webcam/div[2]/div/app-picture-preview/div/div[2]/app-button[2]/button"
        find_elements(self.driver, continue1_button)
        time.sleep(3)

        photo_person2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-identity-back/app-identification-upload-manager/div/div[3]/div/app-button[1]/button"
        find_elements(self.driver, photo_person2)
        time.sleep(3)

        take_photo2 = "Icon:_Take_photo"
        find_elements_id(self.driver, take_photo2)
        time.sleep(3)

        continue2_button = "/html/body/ngb-modal-window/div/div/app-webcam/div[2]/div/app-picture-preview/div/div[2]/app-button[2]/button"
        find_elements(self.driver, continue2_button)
        time.sleep(3)

        photo_person3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-selfie/app-identification-upload-manager/div/div[3]/div/app-button[1]/button"
        find_elements(self.driver,  photo_person3)
        time.sleep(3)

        take_photo3 = "Icon:_Take_photo"
        find_elements_id(self.driver, take_photo3)
        time.sleep(3)

        continue3_button = "/html/body/ngb-modal-window/div/div/app-webcam/div[2]/div/app-picture-preview/div/div[2]/app-button[2]/button"
        find_elements(self.driver, continue3_button)
        time.sleep(3)

        finally_button = "/html/body/div/div/div[6]/button[1]"
        find_elements(self.driver, finally_button)
        time.sleep(3)

        continue_pass3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/aw-wizard-navigation-bar/ul/li[3]/a/div[2]"
        find_elements(self.driver, continue_pass3)
        time.sleep(3)

        # Validar titulo de la pantalla 
        element_3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-tax-status/div/div[1]/div[1]/div/div/p"
        text_expected3 = "Estado Impositivo"
        validate_text_visible(self.driver, element_3, text_expected3)

        select_option1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-tax-status/div/div[1]/div[2]/div/div/div[1]/div/input"
        find_elements(self.driver, select_option1)

        select_option2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-tax-status/div/div[1]/div[2]/div/div/div[2]/div/input"
        find_elements(self.driver, select_option2)

        button_continue = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-tax-status/div/div[2]/div/app-button/button"
        find_elements(self.driver, button_continue)
        time.sleep(2)

        # Validar titulo apertura de legajo 
        element_4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/h1"
        text_expected4 = "Apertura de legajo"
        validate_text_visible(self.driver, element_4, text_expected4)


         # cargar archivos

         #contancia de CBU

        select_field2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[1]/div/div/h2/button'
        element_archive_3 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[1]/div/div/h2/button/app-upload-input/div/div[2]/input'
        archive2 = "C:/Users/luist/OneDrive/Escritorio/Facturas/fractura Bezatbeth_files/factura Bezatbeth.pdf"
        upload_file_after_click(self.driver, select_field2, element_archive_3, archive2)
        time.sleep(5)

        # Exenión de IIBB

        select_field3 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[2]/div/div/h2/button'
        element_archive_4 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[2]/div/div/h2/button/app-upload-input/div/div[2]/input'
        archive3 = "C:/Users/luist/OneDrive/Escritorio/Facturas/fractura Bezatbeth_files/factura Bezatbeth.pdf"
        upload_file_after_click(self.driver, select_field3, element_archive_4, archive3)
        time.sleep(5)

        select_field4 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[3]/div/div/h2/button'
        element_archive_5 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[3]/div/div/h2/button/app-upload-input/div/div[2]/input'
        archive4 = "C:/Users/luist/OneDrive/Escritorio/Facturas/fractura Bezatbeth_files/factura Bezatbeth.pdf"
        upload_file_after_click(self.driver, select_field4, element_archive_5, archive4)
        time.sleep(3)


        # Formulario F1276 WEB
        select_field5 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[3]/div/div/h2/button'
        element_archive_6 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[3]/div/div/h2/button/app-upload-input/div/div[2]/input'
        archive5 = "C:/Users/luist/OneDrive/Escritorio/Facturas/fractura Bezatbeth_files/factura Bezatbeth.pdf"
        upload_file_after_click(self.driver, select_field5, element_archive_6, archive5)
        time.sleep(3)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # validar titulo Gestión de lineas de credito

        element_5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/h1"
        text_expected5 = "Gestión de Lineas de Crédito"
        validate_text_visible(self.driver, element_5, text_expected5)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # manifestación de bienes 
        select_field6 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/div/div/app-acordion-for-upload[1]/div/div/h2/button'
        element_archive_7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/div/div/app-acordion-for-upload[1]/div/div/h2/button/app-upload-input/div/div[2]/input'
        archive6 = "C:/Users/luist/OneDrive/Escritorio/Facturas/fractura Bezatbeth_files/factura Bezatbeth.pdf"
        upload_file_after_click(self.driver, select_field6, element_archive_7, archive6)
        time.sleep(3)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # libro de Iva venta ultomos 12 meses 
        select_field7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/div/div/app-acordion-for-upload[2]/div/div/h2/button'
        element_archive_8 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/div/div/app-acordion-for-upload[2]/div/div/h2/button/app-upload-input/div/div[2]/input'
        archive7 = "C:/Users/luist/OneDrive/Escritorio/Facturas/fractura Bezatbeth_files/factura Bezatbeth.pdf"
        upload_file_after_click(self.driver, select_field7, element_archive_8, archive7)
        time.sleep(3)

        # Ultimo balance 
        select_field8 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/div/div/app-acordion-for-upload[3]/div/div/h2/button'
        element_archive_9 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/div/div/app-acordion-for-upload[3]/div/div/h2/button/app-upload-input/div/div[2]/input'
        archive8 = "C:/Users/luist/OneDrive/Escritorio/Facturas/fractura Bezatbeth_files/factura Bezatbeth.pdf"
        upload_file_after_click(self.driver, select_field8, element_archive_9, archive8)
        time.sleep(3)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # validación título Terceros autorizados a retirar insumos 
        element_6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-authorized-third-parties/div/h1"
        text_expected6 = "Terceros autorizados a retirar insumos"
        validate_text_visible(self.driver, element_6, text_expected6)
        time.sleep(3)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # insertar nombre y DNI
        insert_razon_social_2 = self.driver.find_element(By.XPATH,
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-authorized-third-parties/div/div/div[1]/div/input"
        )

        fake = Faker()
        nombre = fake.name()

        insert_razon_social_2.send_keys(nombre)
        insert_razon_social_2.send_keys(Keys.ENTER)
        time.sleep(3)

        campo_input = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-authorized-third-parties/div/div/div[1]/app-input-for-long-form/div/div/div/input'
        generar_dni(self.driver, campo_input)
        time.sleep(2)

        #Finalizar 

        select_finalizar = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/div/app-button/button"
        find_elements(self.driver, select_finalizar)



    def tearDown(self):
        self.driver.quit()

   

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Onboarding_test_tenant)
    runner = xmlrunner.XMLTestRunner(output='reportOnboarding')
    runner.run(test_suite)