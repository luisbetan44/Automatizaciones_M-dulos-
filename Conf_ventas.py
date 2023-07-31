import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Conf_ventas_test_tenant(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe"  )
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")

    def test_login_user(self):
        driver = self.driver
        username = driver.find_element_by_id("email")
        username.send_keys("soporte.tecnico@silohub.ag")
        username.send_keys(Keys.ENTER)
        time.sleep(3)

        passwordUser = driver.find_element_by_id("password")
        passwordUser.send_keys("123456Aa+")
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
        elemento_1 = self.driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        )

        # Obtener el texto del elemento
        texto_obtenido = elemento_1.text

        # Validar el texto
        texto_esperado = "CONFIRMACIÓN DE VENTA"
        self.assertEqual(texto_obtenido, texto_esperado)

        ##Imprimir la respuesta en consola
        print("El texto obtenido es:", texto_obtenido)
      

       # cargar opción de tipo de confirmación
        wait = WebDriverWait(driver, 10)  
        boton_desplegable = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[2]/div[2]/select')))
        boton_desplegable.click()

        opcion_deseada = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[2]/div[2]/select/option[11]')))
        opcion_deseada.click()

        elemento_texto = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[2]/div[2]/select/option[11]')
        texto_obtenido = elemento_texto.text
        texto_esperado = 'Confirmación De Venta'
        if texto_obtenido == texto_esperado:
              print('La opción ingresada en el campo tipo de confirmación  fue Confirmación de venta.')
        else:
              print('La validación falló. no se visualiza ninguna opción cargada en el campo tipo de confirmación.')
        
        time.sleep(2)

        #insertar numero de cunta del productor 

        insert_account = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[3]/div[2]/div/app-customer-searcher/ng-select/div/div/div[2]/input")
        insert_account.send_keys("1023")
        insert_account.send_keys(Keys.ENTER)
        time.sleep(2)

        select_account = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[3]/div[2]/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span")
        select_account.click()
     

       # selecionar especie  

        wait = WebDriverWait(driver, 10)  
        boton_desplegable = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[4]/div[2]/select')))
        boton_desplegable.click()

        opcion_deseada = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[4]/div[2]/select/option[15]')))
        opcion_deseada.click()

        elemento_texto = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[4]/div[2]/select/option[15]')
        texto_obtenido = elemento_texto.text
        texto_esperado = 'Soja'
        if texto_obtenido == texto_esperado:
              print('La opción ingresada en el campo especie fue  Soja.')
        else:
              print('La validación falló. no se visualiza ninguna opción cargada en el campo especie.')
      

        # Cargar coseha 
        wait = WebDriverWait(driver, 10)  
        boton_desplegable = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[5]/div[2]/select')))
        boton_desplegable.click()

        opcion_deseada = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[5]/div[2]/select/option[3]')))
        opcion_deseada.click()

        elemento_texto = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[5]/div[2]/select/option[3]')
        texto_obtenido = elemento_texto.text
        texto_esperado = '22/23'
        if texto_obtenido == texto_esperado:
              print('La opción ingresada en el campo cosecha fue   22/23 .')
        else:
              print('La validación falló. no se visualiza ninguna opción cargada en el campo cosecha.')
        time.sleep(2)
       

        # ingresar cantidad
        insert_amount = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/app-input-for-long-form[1]/div/div[2]/div/input")
        insert_amount.send_keys("300")
        insert_amount.send_keys(Keys.ENTER)

        # seleccionar modena 

        wait = WebDriverWait(driver, 10)  
        boton_desplegable = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[6]/div[2]/select')))
        boton_desplegable.click()

        opcion_deseada = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[6]/div[2]/select/option[2]')))
        opcion_deseada.click()

        elemento_texto = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[6]/div[2]/select/option[2]')
        texto_obtenido = elemento_texto.text
        texto_esperado = 'ARS'
        if texto_obtenido == texto_esperado:
              print('La opción ingresada en el campo moneda fue   ARS .')
        else:
              print('La validación falló. no se visualiza ninguna opción cargada en el campo moneda.')
        time.sleep(2)
       

        # ingresar precio 

        insert_price = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/app-input-for-long-form[2]/div/div[2]/div/input")
        insert_price.send_keys("3000")
        insert_price.send_keys(Keys.ENTER)

        # seleccionar pizarra

        wait = WebDriverWait(driver, 10)  
        boton_desplegable = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[7]/div[2]/select')))
        boton_desplegable.click()

        opcion_deseada = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[7]/div[2]/select/option[7]')))
        opcion_deseada.click()

        elemento_texto = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[7]/div[2]/select/option[7]')
        texto_obtenido = elemento_texto.text
        texto_esperado = 'Rosario'
        if texto_obtenido == texto_esperado:
              print('La opción ingresada en el campo pizarra fue    Rosario  .')
        else:
              print('La validación falló. no se visualiza ninguna opción cargada en el campo pizarra.')
     

        # condiciones de compras 
        
        wait = WebDriverWait(driver, 10)  
        boton_desplegable = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[8]/div[2]/select')))
        boton_desplegable.click()

        opcion_deseada = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[8]/div[2]/select/option[5]')))
        opcion_deseada.click()

        elemento_texto = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[8]/div[2]/select/option[5]')
        texto_obtenido = elemento_texto.text
        texto_esperado = 'A - Cuenta 10 días Hábiles'
        if texto_obtenido == texto_esperado:
              print('La opción ingresada en el campo condiciones de compra fue  A - Cuenta 10 días Hábiles   .')
        else:
              print('La validación falló. no se visualiza ninguna opción cargada en el campo condiciones de compra.')
        

        wait = WebDriverWait(driver, 10)
        # Hacer scroll hasta la sección de "Código estándar"
        elemento_codigo_estandar = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[9]/div[2]/select')))
        driver.execute_script("arguments[0].scrollIntoView(true);", elemento_codigo_estandar)


      # ingrear código estándar
        
        wait = WebDriverWait(driver, 10)  
        boton_desplegable = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[9]/div[2]/select')))
        boton_desplegable.click()

        opcion_deseada = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[9]/div[2]/select/option[2]')))
        opcion_deseada.click()

        elemento_texto = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[9]/div[2]/select/option[2]')
        texto_obtenido = elemento_texto.text
        texto_esperado = 'General'
        if texto_obtenido == texto_esperado:
              print('La opción ingresada en el campo código estándar fue  General  .')
        else:
              print('La validación falló. no se visualiza ninguna opción cargada en el campo código estándar.')
        time.sleep(2)

        # seleecccionar la fecha 

        select_date = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[1]/div[2]/app-date-picker/div/input[2]")
        select_date.click()
        time.sleep(1)

        select_calendar = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div/span[25]")
        select_calendar.click()
        time.sleep(1)

        select_calendar = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div/span[36]")
        select_calendar.click()
      


        # insertar campo plata
        wait = WebDriverWait(driver, 10)  
        boton_desplegable = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/select')))
        boton_desplegable.click()

        opcion_deseada = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/select/option[3]')))
        opcion_deseada.click()

        elemento_texto = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/select/option[3]')
        texto_obtenido = elemento_texto.text
        texto_esperado = 'Carlos Pellegrini'
        if texto_obtenido == texto_esperado:
              print('La opción ingresada en el campo planta fue   Carlos Pellegrini   .')
        else:
              print('La validación falló. no se visualiza ninguna opción cargada en el campo planta.')
    


        # insertar procedenia
        wait = WebDriverWait(driver, 10)  
        boton_desplegable = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/select')))
        boton_desplegable.click()

        opcion_deseada = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/select/option[2]')))
        opcion_deseada.click()

        elemento_texto = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/select/option[2]')
        texto_obtenido = elemento_texto.text
        texto_esperado = '03 Playa S. Miguel (T6 Y M. Pampa)'
        if texto_obtenido == texto_esperado:
              print('La opción ingresada en el campo procedencia fue   03 Playa S. Miguel (T6 Y M. Pampa)   .')
        else:
              print('La validación falló. no se visualiza ninguna opción cargada en el campo procedencia.')
     


        # insertar destino
        wait = WebDriverWait(driver, 10)  
        boton_desplegable = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/select/option[2]')))
        boton_desplegable.click()

        opcion_deseada = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/select/option[2]')))
        opcion_deseada.click()

        elemento_texto = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/select/option[2]')
        texto_obtenido = elemento_texto.text
        texto_esperado = '03 Playa S. Miguel (T6 Y M. Pampa)'
        if texto_obtenido == texto_esperado:
              print('La opción ingresada en el campo código estándar fue  General  .')
        else:
              print('La validación falló. no se visualiza ninguna opción cargada en el campo código estándar.')
        time.sleep(2)


        # seleccionar el botón de continuar 

        select_button_continue = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[2]/app-button[2]/button")
        select_button_continue.click()

        select_button_confirmar = driver.find_element_by_xpath("/html/body/div[4]/div/div[6]/button[3]")
        select_button_confirmar.click()


        # validar el mensaje de respuesta 

        wait = WebDriverWait(driver,10)
        elemento_texto = driver.find_element_by_xpath('/html/body/div/div/h2')
        texto_obtenido = elemento_texto.text
        texto_esperado = 'Confirmación de venta generada con éxito.'
        if texto_obtenido == texto_esperado:
              print('Confirmación de venta generada con éxito. .')
        else:
              print('No se pudo generar la confirmación de venta El Código de Cosecha no existe.')
        time.sleep(2)

        select_finish = driver.find_element_by_xpath("/html/body/div/div/div[6]/button[1]")
        select_finish.click()
        time.sleep(3)

        
              


    
    def tearDown(self):
        self.driver.close()

   

if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(output="reportes", report_name="reporte_conf_ventas"),
    )



