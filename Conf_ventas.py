import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xmlrunner

class Conf_ventas_test_tenant(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver.exe"
        )
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")

    def test_conf_venta(self):
        driver = self.driver
        username = driver.find_element_by_id("email")
        username.send_keys("admingd@silohub.ag")
        username.send_keys(Keys.ENTER)
        time.sleep(3)

        passwordUser = driver.find_element_by_id("password")
        passwordUser.send_keys("G@viglio123")
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

        select_Granos = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span"
        )
        select_Granos.click()
        time.sleep(1)

        select_conf_ventas = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[2]/a"
        )
        select_conf_ventas.click()
        time.sleep(1)

        # validar titulo de la pantalla
        
        texto_deseado = "CONTRATOS"
        elemento = driver.find_element_by_xpath(f"//*[contains(text(), '{texto_deseado}')]")

       # Realizar validación del texto 
        texto_optenido = elemento.text
        texto_esperado = "CONTRATOS"
        assert texto_optenido == texto_esperado

        if texto_optenido:
           print("El titulo  fue validado correctamente", texto_optenido)

        else:
            print("No se pudo validar el titulo")


        # cargar opción de tipo de confirmación
        wait = WebDriverWait(driver, 10)
        boton_desplegable = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[2]/div[2]/select",
                )
            )
        )
        boton_desplegable.click()

        opcion_deseada = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[2]/div[2]/select/option[10]",
                )
            )
        )
        opcion_deseada.click()

        elemento_texto_1 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[2]/div[2]/select/option[10]"
        )
        texto_obtenido_1 = elemento_texto_1.text
        texto_esperado_1 = "Confirmación De Venta"
        if texto_obtenido_1 == texto_esperado_1:
            print(
                "La opción ingresada en el campo tipo de confirmación  fue Confirmación de venta."
            )
        else:
            print(
                "La validación falló. no se visualiza ninguna opción cargada en el campo tipo de confirmación."
            )

        time.sleep(2)

        # insertar numero de cunta del productor

        insert_account = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[3]/div[2]/div/app-customer-searcher/ng-select/div/div/div[2]/input"
        )
        insert_account.send_keys("1023")
        insert_account.send_keys(Keys.ENTER)
        time.sleep(2)

        select_account = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[3]/div[2]/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        )
        select_account.click()

        # selecionar especie

        wait = WebDriverWait(driver, 10)
        boton_desplegable = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[4]/div[2]/select",
                )
            )
        )
        boton_desplegable.click()

        opcion_deseada = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[4]/div[2]/select/option[15]",
                )
            )
        )
        opcion_deseada.click()

        elemento_texto_2 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[4]/div[2]/select/option[15]"
        )
        texto_obtenido_2 = elemento_texto_2.text
        texto_esperado_2 = "Soja"
        if texto_obtenido_2 == texto_esperado_2:
            print("La opción ingresada en el campo especie fue  Soja.")
        else:
            print(
                "La validación falló. no se visualiza ninguna opción cargada en el campo especie."
            )

        # Cargar coseha
        wait = WebDriverWait(driver, 10)
        boton_desplegable = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[5]/div[2]/select",
                )
            )
        )
        boton_desplegable.click()

        opcion_deseada = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[5]/div[2]/select/option[3]",
                )
            )
        )
        opcion_deseada.click()

        elemento_texto_3 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[5]/div[2]/select/option[3]"
        )
        texto_obtenido_3 = elemento_texto_3.text
        texto_esperado_3 = "22/23"
        if texto_obtenido_3 == texto_esperado_3:
            print("La opción ingresada en el campo cosecha fue   22/23 .")
        else:
            print(
                "La validación falló. no se visualiza ninguna opción cargada en el campo cosecha."
            )
        time.sleep(2)

        # ingresar cantidad
        insert_amount = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/app-input-for-long-form[1]/div/div[2]/div/input"
        )
        insert_amount.send_keys("300")
        insert_amount.send_keys(Keys.ENTER)

        # seleccionar modena

        wait = WebDriverWait(driver, 10)
        boton_desplegable = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[6]/div[2]/select",
                )
            )
        )
        boton_desplegable.click()

        opcion_deseada = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[6]/div[2]/select/option[2]",
                )
            )
        )
        opcion_deseada.click()

        elemento_texto_4 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[6]/div[2]/select/option[2]"
        )
        texto_obtenido_4 = elemento_texto_4.text
        texto_esperado_4 = "ARS"
        if texto_obtenido_4 == texto_esperado_4:
            print("La opción ingresada en el campo moneda fue   ARS .")
        else:
            print(
                "La validación falló. no se visualiza ninguna opción cargada en el campo moneda."
            )
        time.sleep(2)

        # ingresar precio

        insert_price = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/app-input-for-long-form[2]/div/div[2]/div/input"
        )
        insert_price.send_keys("3000")
        insert_price.send_keys(Keys.ENTER)

        # seleccionar pizarra

        wait = WebDriverWait(driver, 10)
        boton_desplegable = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[7]/div[2]/select",
                )
            )
        )
        boton_desplegable.click()

        opcion_deseada = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[7]/div[2]/select/option[7]",
                )
            )
        )
        opcion_deseada.click()

        elemento_texto_5 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[7]/div[2]/select/option[7]"
        )
        texto_obtenido_5 = elemento_texto_5.text
        texto_esperado_5 = "Rosario"
        if texto_obtenido_5 == texto_esperado_5:
            print("La opción ingresada en el campo pizarra fue Rosario.")
        else:
            print(
                "La validación falló. no se visualiza ninguna opción cargada en el campo pizarra."
            )

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # condiciones de compras

        #wait = WebDriverWait(driver, 10)
        #boton_desplegable = wait.until(
            #EC.presence_of_element_located(
                #(
                    #By.XPATH,
                    #"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[8]/div[2]/select",
                #)
            #)
        #)
        #boton_desplegable.click()

        #opcion_deseada = wait.until(
            #EC.presence_of_element_located(
               # (
                   # By.XPATH,
                    #"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[8]/div[2]/select/option[5]",
               # )
            #)
       # )
        #opcion_deseada.click()

        #elemento_texto_6 = driver.find_element_by_xpath(
           # "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[8]/div[2]/select/option[5]"
        #)
        #texto_obtenido_6 = elemento_texto_6.text
        #texto_esperado_6 = "A - Cuenta 10 días Hábiles"
        #if texto_obtenido_6 == texto_esperado_6:
          #  print(
               # "La opción ingresada en el campo condiciones de compra fue  A - Cuenta 10 días Hábiles   ."
           # )
        #else:
          #  print(
              #  "La validación falló. no se visualiza ninguna opción cargada en el campo condiciones de compra."
            #)

    

        # seleccionar fecha de pago

        select_date = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[8]/div[2]/app-date-picker/div/input[2]")
        select_date.click()

        select_arrow = driver.find_element_by_xpath("/html/body/div[1]/div[1]/span[2]")
        select_arrow.click()

        insert_date = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/span[32]")
        insert_date.click()
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # ingrear código estándar

        wait = WebDriverWait(driver, 5)
        boton_desplegable = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[9]/div[2]/select",
                )
            )
        )
        boton_desplegable.click()

        opcion_deseada = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[9]/div[2]/select/option[2]",
                )
            )
        )
        opcion_deseada.click()

        elemento_texto_7 = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[9]/div[2]/select/option[2]"
        )
        texto_obtenido_7 = elemento_texto_7.text
        texto_esperado_7 = "General"
        if texto_obtenido_7 == texto_esperado_7:
            print("La opción ingresada en el campo código estándar fue  General  .")
        else:
            print(
                "La validación falló. no se visualiza ninguna opción cargada en el campo código estándar."
            )
        time.sleep(2)

        # seleeccionar la fecha

        select_date = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[1]/div[2]/app-date-picker/div/input[2]"
        )
        select_date.click()
        time.sleep(2)

        select_arrow2 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/span[2]")
        select_arrow2.click() 

        select_calendar = driver.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/div[2]/div/span[3]"
        )
        select_calendar.click()
        time.sleep(1)

        select_calendar = driver.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/div[2]/div/span[31]"
        )
        select_calendar.click()

        # insertar campo plata
        wait = WebDriverWait(driver, 10)
        boton_desplegable = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/app-search-selector/ng-select/div/span",
                )
            )
        )
        boton_desplegable.click()

        opcion_deseada = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[2]/span",
                )
            )
        )
        opcion_deseada.click()

        ##elemento_texto_8 = driver.find_element_by_xpath(
           # "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[2]/span"
        #)
        #texto_obtenido_8 = elemento_texto_8.text
        #texto_esperado_8 = "Carlos Pellegrini"
        #if texto_obtenido_8 == texto_esperado_8:
          #  print("La opción ingresada en el campo planta fue   Carlos Pellegrini   .")
        #else:
           # print(
            #    "La validación falló. no se visualiza ninguna opción cargada en el campo planta."
            #)

        # insertar procedenia
        wait = WebDriverWait(driver, 5)
        boton_desplegable = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/app-search-selector/ng-select/div/div/div[2]/input',
                )
            )
        )
        boton_desplegable.click()

        opcion_deseada = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[3]/span",
                )
            )
        )
        opcion_deseada.click()

       # elemento_texto_9 = driver.find_element_by_xpath(
        #    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[3]/span"
        #)
        #texto_obtenido_9 = elemento_texto_9.text
        #texto_esperado_9 = "03 Playa S. Miguel (T6 y M. Pampa)"
        #if texto_obtenido_9 == texto_esperado_9:
          #  print(
           #     "La opción ingresada en el campo procedencia fue   03 Playa S. Miguel (T6 Y M. Pampa)   ."
            #)
        #else:
           # print(
            #    "La validación falló. no se visualiza ninguna opción cargada en el campo procedencia."
            #)

        # insertar destino
        wait = WebDriverWait(driver, 10)
        boton_desplegable = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/app-search-selector/ng-select/div/span",
                )
            )
        )
        boton_desplegable.click()

        opcion_deseada = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[6]/span",
                )
            )
        )
        opcion_deseada.click()

        #elemento_texto_10 = driver.find_element_by_xpath(
         #   "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[6]/span"
        #)
        #texto_obtenido_10 = elemento_texto_10.text
        #texto_esperado_10 = "06 SECADA BONIFICADA"
        #if texto_obtenido_10 == texto_esperado_10:
         #   print("La opción ingresada en el campo destino es: ", texto_esperado_10)
        #else:
          #  print(
         #       "La validación falló. no se visualiza ninguna opción cargada en el campo código estándar."
          #  )
     

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # seleccionar el botón de continuar

        select_button_continue = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[2]/app-button[2]/button"
        )
        select_button_continue.click()
        time.sleep(2)

        select_button_confirmar = driver.find_element_by_xpath(
            "/html/body/div[5]/div/div[6]/button[3]"
        )
        select_button_confirmar.click()
        time.sleep(2)

        # validar el mensaje de respuesta

        wait = WebDriverWait(driver, 10)
        elemento_texto_11 = driver.find_element_by_xpath("/html/body/div[5]/div/h2")
        texto_obtenido_11 = elemento_texto_11.text
        texto_esperado_11 = "Confirmación de venta generada con éxito."
        if texto_obtenido_11 == texto_esperado_11:
            print("Confirmación de venta generada con éxito.")
        else:
            print(
                "No se pudo generar la confirmación de venta El Código de Cosecha no existe."
            )
        time.sleep(2)

        select_finish = driver.find_element_by_xpath(
            "/html/body/div/div/div[6]/button[1]"
        )
        select_finish.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(Conf_ventas_test_tenant)
  runner = xmlrunner.XMLTestRunner(output='reportGranosContratos')
  runner.run(test_suite)