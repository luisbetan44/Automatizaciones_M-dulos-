import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
import random
from faker import Faker


class Onboarding_test_tenant(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")

    def test_login_user(self):
        driver = self.driver
        username = driver.find_element_by_id("email")
        username.send_keys("luis.tacourt@gmail.com")
        username.send_keys(Keys.ENTER)
        time.sleep(3)

        passwordUser = driver.find_element_by_id("password")
        passwordUser.send_keys("Bet$123456")
        passwordUser.send_keys(Keys.ENTER)
        time.sleep(3)

        insertButton = driver.find_element_by_xpath(
            "/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button"
        )
        insertButton.send_keys(Keys.ENTER)
        time.sleep(3)

        select_tenant = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[8]/div/div/img"
        )
        select_tenant.click()

        select_config = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span"
        )
        select_config.click()

        select_documento = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[8]/a"
        )
        select_documento.click()
        time.sleep(3)

        # validar el titulode la pantalle documentación

        elemento_1 = self.driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        )

        # Obtener el texto del elemento
        texto_obtenido = elemento_1.text

        # Validar el texto
        texto_esperado = "DOCUMENTACIÓN"
        self.assertEqual(texto_obtenido, texto_esperado)

        ##Imprimir la respuesta en consola
        print("El texto obtenido es:", texto_obtenido)

        select_button = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-main/div/div[3]/app-button/button"
        )
        select_button.click()

        agregar_onboarding = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-docket-list/div/div[1]/div/div/div/app-button/button"
        )
        agregar_onboarding.click()

        # validar mensaje de la pantalla
        elemento_2 = self.driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[1]/div/span"
        )

        # Obtener el texto del elemento
        texto_obtenido = elemento_2.text

        # Validar el texto
        texto_esperado = "Para poder continuar al siguiente paso, será obligatorio completar los campos que se muestran a continuación."
        self.assertEqual(texto_obtenido, texto_esperado)

        ##Imprimir la respuesta en consola
        print("El texto obtenido es:", texto_obtenido)

        # llenar formulario

        
        cuit_valido = False
        while not cuit_valido:
    # Generar números aleatorios para los componentes del CUIT
            provincia = random.randint(1, 24)
            dni = random.randint(1000000, 99999999)
            verificador = random.randint(0, 9)
            cuit = '{}-{}-{}'.format(provincia, dni, verificador)

    # Calcular el dígito verificador del CUIT
            input_element = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[2]/div[1]/app-input-for-long-form[1]/div[1]/div[2]/div/input')

        # Insertar el CUIT en el campo de entrada
            input_element.clear()
            input_element.send_keys(cuit)
            input_element.send_keys(Keys.ENTER)

            driver.implicitly_wait(2)

    # Combinar los componentes del CUIT en una cadena
            error_message = driver.find_elements_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[2]/div[1]/app-input-for-long-form[1]/div[2]/app-alerts/div/span')
            if len(error_message) == 0:
            # No hay mensaje de error, se ha ingresado un CUIT válido
                cuit_valido = True
            else:
            # Hay mensaje de error, se genera un nuevo CUIT en la próxima iteración
               continue

        

# Insertar el CUIT en el campo de entrada
        
        insert_razon_social = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[2]/div[1]/app-input-for-long-form[2]/div/div[2]/div/input"
        )

        fake = Faker()
        nombre = fake.name()

        insert_razon_social.send_keys(nombre)
        insert_razon_social.send_keys(Keys.ENTER)

        select_radio = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[2]/div[2]/div/app-radio[1]/div/input"
        )
        select_radio.click()

        selecct_sucesion = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[2]/div[2]/div[2]/div/input"
        )
        selecct_sucesion.click()

        # cargar archivos

        select_campo = driver.find_element_by_xpath(
            '//*[@id="flush-headingOne"]/button'
        )
        select_campo.click()
        time.sleep(3)

        archivo = "C:/Users/luist/OneDrive/Escritorio/Facturas/fractura Bezatbeth_files/factura Bezatbeth.pdf"

        elemento_archivo_1 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[2]/div[4]/app-acordion-for-upload/div/div/h2/button/app-upload-input/div/div[2]/input'
        )
        elemento_archivo_1.send_keys(archivo)
        time.sleep(3)

    
        check_button = driver.find_element(
            By.XPATH,
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[3]/app-checks/div/input",
        )
        check_button.click()
        time.sleep(3)

        continue_button = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-account-type/div/div[3]/div/div/app-button/button" )
        continue_button.click()
        time.sleep(2)

        insert_document = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-identity-validation/div/div[3]/app-button/button"
        )

        insert_document.click()
        time.sleep(2)

        photo_person1 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-identity-front/app-identification-upload-manager/div/div[3]/div/app-button[1]/button"
        ) 

        photo_person1.click()
        time.sleep(2)

        take_photo = driver.find_element_by_id(
            "Icon:_Take_photo"
        )
        take_photo.click()
        time.sleep(2)

        continue1_button = driver.find_element_by_xpath(
            "/html/body/ngb-modal-window/div/div/app-webcam/div[2]/div/app-picture-preview/div/div[2]/app-button[2]/button"
            )
        continue1_button.click()
        time.sleep(3)

        photo_person2 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-identity-back/app-identification-upload-manager/div/div[3]/div/app-button[1]/button"
        ) 

        photo_person2.click()
        time.sleep(2)

        take_photo2 = driver.find_element_by_id(
            "Icon:_Take_photo"
        )
        take_photo2.click()
        time.sleep(2)

        continue2_button = driver.find_element_by_xpath(
            "/html/body/ngb-modal-window/div/div/app-webcam/div[2]/div/app-picture-preview/div/div[2]/app-button[2]/button"
            )
        continue2_button.click()
        time.sleep(2)

        photo_person3 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-selfie/app-identification-upload-manager/div/div[3]/div/app-button[1]/button"
        ) 

        photo_person3.click()
        time.sleep(2)

        take_photo3 = driver.find_element_by_id(
            "Icon:_Take_photo"
        )
        take_photo3.click()
        time.sleep(2)

        continue3_button = driver.find_element_by_xpath(
            "/html/body/ngb-modal-window/div/div/app-webcam/div[2]/div/app-picture-preview/div/div[2]/app-button[2]/button"
            )
        continue3_button.click()
        time.sleep(3)

        finally_button = driver.find_element_by_xpath(
            "/html/body/div/div/div[6]/button[1]"
        )
        finally_button.click()
        time.sleep(3)

        continue_pass3 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/aw-wizard-navigation-bar/ul/li[3]/a/div[2]"
        )
        continue_pass3.click()
        time.sleep(3)

        # Validar titulo de la pantalla 
        elemento_3 = self.driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-tax-status/div/div[1]/div[1]/div/div/p"
        )

        # Obtener el texto del elemento
        texto_obtenido = elemento_3.text

        # Validar el texto
        texto_esperado = "Estado Impositivo"
        self.assertEqual(texto_obtenido, texto_esperado)

        ##Imprimir la respuesta en consola
        print("El texto obtenido es:", texto_obtenido)

        select_option1 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-tax-status/div/div[1]/div[2]/div/div/div[1]/div/input"
        ) 

        select_option1.click()

        select_option2 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-tax-status/div/div[1]/div[2]/div/div/div[2]/div/input"
        ) 

        select_option2.click()

        button_continue = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-tax-status/div/div[2]/div/app-button/button"
        )
        button_continue.click()
        time.sleep(2)

        # Validar titulo apertura de legajo 
        elemento_4 = self.driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/h1"
        )

        # Obtener el texto del elemento
        texto_obtenido = elemento_4.text

        # Validar el texto
        texto_esperado = "Apertura de legajo"
        self.assertEqual(texto_obtenido, texto_esperado)

        ##Imprimir la respuesta en consola
        print("El texto obtenido es:", texto_obtenido)

         # cargar archivos

         #contancia de CBU

        select_campo_1 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[1]/div/div/h2/button'
        )
        select_campo_1.click()
        time.sleep(3)

        archivo = "C:/Users/luist/OneDrive/Escritorio/Facturas/fractura Bezatbeth_files/factura Bezatbeth.pdf"

        elemento_archivo_2 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[1]/div/div/h2/button/app-upload-input/div/div[2]/input"
        )
        elemento_archivo_2.send_keys(archivo)
        time.sleep(3)

        # Exenión de IIBB

        select_campo_2 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[2]/div/div/h2/button'
        )
        select_campo_2.click()
        time.sleep(3)

        archivo = "C:/Users/luist/OneDrive/Escritorio/Capturas de pantalla/2022-02-14 (5).png"

        elemento_archivo_3 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[2]/div/div/h2/button/app-upload-input/div/div[2]/input'
        )
        elemento_archivo_3.send_keys(archivo)
        time.sleep(3)

        select_campo_3 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[2]/div/div/h2/button'
        )
        select_campo_3.click()
        time.sleep(3)

        archivo = "C:/Users/luist/OneDrive/Escritorio/Capturas de pantalla/2022-02-14 (5).png"

        elemento_archivo_4 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[2]/div/div/h2/button/app-upload-input/div/div[2]/input'
        )
        elemento_archivo_4.send_keys(archivo)
        time.sleep(3)


        # Formulario F1276 WEB
        select_campo_4 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[3]/div/div/h2/button'
        )
        select_campo_4.click()
        time.sleep(3)

        archivo = "C:/Users/luist/OneDrive/Escritorio/Capturas de pantalla/2022-02-14 (5).png"

        elemento_archivo_5 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-legacy-opening/div/div/app-acordion-for-upload[3]/div/div/h2/button/app-upload-input/div/div[2]/input'
        )
        elemento_archivo_5.send_keys(archivo)
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # validar titulo Gestión de lineas de credito

        elemento_5 = self.driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/h1"
        )

        # Obtener el texto del elemento
        texto_obtenido = elemento_5.text

        # Validar el texto
        texto_esperado = "Gestión de Lineas de Crédito"
        self.assertEqual(texto_obtenido, texto_esperado)

        ##Imprimir la respuesta en consola
        print("El texto obtenido es:", texto_obtenido)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # manifestación de bienes 
        select_campo_5 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/div/div/app-acordion-for-upload[1]/div/div/h2/button'
        )
        select_campo_5.click()
        time.sleep(3)

        archivo = "C:/Users/luist/OneDrive/Escritorio/Capturas de pantalla/2022-02-14 (5).png"

        elemento_archivo_6 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/div/div/app-acordion-for-upload[1]/div/div/h2/button/app-upload-input/div/div[2]/input'
        )
        elemento_archivo_6.send_keys(archivo)
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # libro de Iva venta ultomos 12 meses 
        select_campo_6 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/div/div/app-acordion-for-upload[2]/div/div/h2/button'
        )
        select_campo_6.click()
        time.sleep(3)

        archivo = "C:/Users/luist/Downloads/Reportes-de-Usuarios_18_6_2023 (1).xls"

        elemento_archivo_7 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/div/div/app-acordion-for-upload[2]/div/div/h2/button/app-upload-input/div/div[2]/input'
        )
        elemento_archivo_7.send_keys(archivo)
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


        # Ultimo balance 
        select_campo_7 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/div/div/app-acordion-for-upload[3]/div/div/h2/button'
        )
        select_campo_7.click()
        time.sleep(3)

        archivo = "C:/Users/luist/OneDrive/Escritorio/Capturas de pantalla/2022-02-14 (5).png"

        elemento_archivo_8 = driver.find_element_by_xpath(
            '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-management-credit-lines/div/div/app-acordion-for-upload[3]/div/div/h2/button/app-upload-input/div/div[2]/input'
        )
        elemento_archivo_8.send_keys(archivo)
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # validación título Terceros autorizados a retirar insumos 
        elemento_6 = self.driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-authorized-third-parties/div/h1"
        )

        # Obtener el texto del elemento
        texto_obtenido = elemento_6.text

        # Validar el texto
        texto_esperado = "Terceros autorizados a retirar insumos"
        self.assertEqual(texto_obtenido, texto_esperado)

        ##Imprimir la respuesta en consola
        print("El texto obtenido es:", texto_obtenido)
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # insertar nombre y DNI
        insert_razon_social_2 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-authorized-third-parties/div/div/div[1]/app-input-for-long-form[1]/div/div/div/input"
        )

        fake = Faker()
        nombre = fake.name()

        insert_razon_social_2.send_keys(nombre)
        insert_razon_social_2.send_keys(Keys.ENTER)
        time.sleep(3)


        def generar_dni():
            dni = random.randint(10000000, 99999999)
            return str(dni) + str(calcular_digito_verificador(dni))

        def calcular_digito_verificador(dni):
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            return tabla[dni % 23]
       
        campo_input = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/app-authorized-third-parties/div/div/div[1]/app-input-for-long-form[2]/div/div/div/input')

# Genera un número de DNI
        dni_generado = generar_dni()

# Envía el valor generado al campo de entrada
        campo_input.send_keys(dni_generado)
        time.sleep(2)

        #Finalizar 

        select_finalizar = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-documentation-process/div/div/aw-wizard/div/app-legacy-documentation/div/div/div/app-button/button"
        )

        select_finalizar.click()




    def tearDown(self):
        self.driver.close()

   

if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(output="reportes", report_name="reporte_onboarding"),
    )