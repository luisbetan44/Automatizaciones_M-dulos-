import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import xmlrunner




class inicio_tenat(unittest.TestCase):

    def    setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")

    

    def test_login_user_1(self):
        driver = self.driver
        username = driver.find_element_by_id("email")
        username.send_keys("admingd@silohub.ag")
        username.send_keys(Keys.ENTER)
        time.sleep(3)


        passwordUser = driver.find_element_by_id("password")
        passwordUser.send_keys("G@viglio123")
        passwordUser.send_keys(Keys.ENTER)
        time.sleep(3)

        insertButton = driver.find_element_by_xpath("/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button")
        insertButton.send_keys(Keys.ENTER) 
        time.sleep(3)

      ## seleccionar el tenant 
        selectTenant = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[8]/div/div/img")
        selectTenant.click()
        time.sleep(3)

     # localiza el input y envia el número de la cuenta 
        input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-options")))
        input_element.send_keys('1023')
      
       #selecciona el elemento oculto y crea un botón para hacer click sobre el 
        element_to_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search-dropdown > app-accounts-list > ngx-simplebar > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div.dropdown-sub-item.accounts-numbers")))
        driver.execute_script("arguments[0].style.display = 'block';", element_to_click)
        element_to_click.click()
        time.sleep(3)


        
       
       ##seleccionar el botón filtro 
        Filtro_campaña = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[1]/div[2]/app-filter-button/button/div/span")
        Filtro_campaña.click()
        time.sleep(3)

   

        
        ## seleccionar filtro 

        delete_campaign = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-tag-container/div/div/div[7]/app-tag/div/div/i")
        delete_campaign.click()
        time.sleep(2)

        select_campaña = driver.find_element_by_xpath('/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[2]/div/div')
        select_campaña.click()
        time.sleep(3)

        selecct_button_aplicar = driver.find_element_by_xpath('/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button')
        selecct_button_aplicar.click()
        time.sleep(6)
       
       ## validar si el texto es visible para el usuario 
        element = driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/app-welcome-home/div/div[1]/div/p')

        is_visible = element.is_displayed()

        if is_visible:
           print("El texto es visible para el usuario")
        else:
           print("El texto no es visible para el usuario")

       # Encontrar el elemento por su texto utilizando XPath
        texto_deseado = " Buen día JUAN DEMO!"
        elemento = driver.find_element_by_xpath(f"//*[contains(text(), '{texto_deseado}')]")

       # Realizar validación del texto 
        texto_optenido = elemento.text
        texto_esperado = "Buen día JUAN DEMO!"
        assert texto_optenido == texto_esperado

        if texto_optenido:
           print("El texto del saludo fue validado correctamente", texto_optenido)

        else:
            print("No se pudo validar el texto del saludo")


     ##validar totalizadores vencidos a hoy 

        elemento = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[1]/app-number-values-card/div/div/div/div[3]/div/h4/span')
        valor_1 = elemento.text 
        if re.search(r'\d', valor_1):  
          print('El saldo vencido a hoy en ARS  es un carácter numérico.', valor_1)
        else:
          print('El saldo vencido a hoy en ARS no es un carácter numérico.')
   
        elemento = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[2]/app-number-values-card/div/div/div/div[3]/div/h4/span')
        valor_2 = elemento.text 
        if re.search(r'\d', valor_2):  
          print('El saldo vencido a hoy en USD  es un carácter numérico.', valor_2)
        else:
          print('El saldo vencido a hoy en USD no es un carácter numérico.')

        ##validar totalizadores  a vencer  

        elemento = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[3]/app-number-values-card/div/div/div/div[3]/div/h4/span')
        valor_3 = elemento.text 
        if re.search(r'\d', valor_3):  
          print('El saldo a vencer en ARS  es un carácter numérico.', valor_3)
        else:
          print('El saldo a vencer en ARS no es un carácter numérico.')


        elemento = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[4]/app-number-values-card/div/div/div/div[3]/div/h4/span')
        valor_4 = elemento.text 
        if re.search(r'\d', valor_4):  
          print('El saldo a vencer en USD  es un carácter numérico.', valor_4)
        else:
          print('El saldo a vencer en USD no es un carácter numérico.')
         
         ## Seleccionar el elemento que contiene el texto 

        elemento = self.driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[1]/div[1]/div/p")
        texto_obtenido = elemento.text
        texto_esperado = "Resumen de Mis Negocios de Granos"
        self.assertEqual(texto_obtenido, texto_esperado)

      
        print("El texto obtenido es:", texto_obtenido)

        # Seleccionar el elemento de la imagen
        
        imagen_1 = self.driver.find_element_by_css_selector('img[src="assets/images/grains/soja.svg"]')
        
        # Obtener la URL de la imagen
        
        url_imagen_1 = imagen_1.get_attribute("src")
        
        # Validar la URL de la imagenes
        
        url_esperada_1 = "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        self.assertEqual(url_imagen_1, url_esperada_1)

        print("la url de la imagen de soja es la siguente", url_imagen_1)

        # Seleccionar el elemento de la imagen

        imagen_2 = self.driver.find_element_by_css_selector('img[src="assets/images/grains/maiz.svg"]')
        
        # Obtener la URL de la imagen
        
        url_imagen_2 = imagen_2.get_attribute("src")
    
        url_esperada_2 = "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg"
        self.assertEqual(url_imagen_2, url_esperada_2)

        print("la url de la imagen de maiz es la siguente", url_imagen_2)

        # Seleccionar el elemento de la imagen
        
        imagen_3 = self.driver.find_element_by_css_selector('img[src="assets/images/grains/trigo.svg"]')
        
        # Obtener la URL de la imagen
        
        url_imagen_3 = imagen_3.get_attribute("src")
    
        url_esperada_3 = "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg"
        self.assertEqual(url_imagen_3, url_esperada_3)

        print("la url de la imagen de trigo  es la siguente", url_imagen_3)

        ## validar los campor del resumen de mis negocios 
    
       ## entregado
       
        elemento_1 = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[2]/app-indicator-card/div/div[2]/div[1]/div[2]")
        valor_5 = elemento_1.text 
        if re.search(r'\d', valor_5):  
          print('El saldo entregado  es un carácter numérico.', valor_5)
        else:
          print('El saldo entregado no es un carácter numérico.')

        ## fijado 

        elemento_2 = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[3]/app-indicator-card/div/div[2]/div[1]/div[2]')
        valor_6 = elemento_2.text 
        if re.search(r'\d', valor_6):  
          print('El saldo fijado es un carácter numérico.', valor_6)
        else:
          print('El saldo fijado no es un carácter numérico.')

         ## pesificado

        elemento_3 = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[4]/app-indicator-card/div/div[2]/div[1]/div[2]')
        valor_7 = elemento_3.text 
        if re.search(r'\d', valor_7):  
          print('El saldo pesificado es un carácter numérico.', valor_7)
        else:
          print('El saldo pesificado no es un carácter numérico.')

        ## liquidado

        elemento_4 = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[5]/app-indicator-card/div/div[2]/div[1]/div[2]')
        valor_8 = elemento_4.text 
        if re.search(r'\d', valor_8):  
          print('El saldo liquidado es un carácter numérico.', valor_8)
        else:
          print('El saldo liquidado no es un carácter numérico.')

          ## pagado

        elemento_5 = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[6]/app-indicator-card/div/div[2]/div[1]/div[2]')
        valor_9 = elemento_5.text 
        if re.search(r'\d', valor_9):  
          print('El saldo pagado  es un carácter numérico.', valor_9)
        else:
          print('El saldo pagado no es un carácter numérico.')

        # validar entregas recientes 

        elemento = self.driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/p')

        # Obtener el texto del elemento
        texto_obtenido = elemento.text
        
        # Validar el texto
        texto_esperado = "Entregas y Ventas Recientes"
        self.assertEqual(texto_obtenido, texto_esperado)

        ##Imprimir la respuesta en consola
        print("El texto obtenido es:", texto_obtenido)

        # validar la imagen del producto 


    

        imagen_4 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[1]/img")
     
        # Obtener la URL de la imagen
        url_imagen_obtenida = imagen_4.get_attribute('src')

        imagen_4_esperadas = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]

        # Validar si la URL obtenida está en la lista de URLs esperadas
        if url_imagen_obtenida in imagen_4_esperadas:
      
            print("La imagen es visible para el usuario. URL:", url_imagen_obtenida)
        else:
            print("La imagen no es visible para el usuario. URL:", url_imagen_obtenida)


       

        #validar el numero de comprobante del movimiento 

        elemento_6 = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span')
        valor_10 = elemento_6.text 
        if re.search(r'\d', valor_10):  
          print('El comprobante CTG/CRT  es un carácter numérico.', valor_10)
        else:
          print('El comprobante CTG/CRT no es un carácter numérico.')

       # validar los Kilos netos 
        elemento_7 = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span')
        valor_11 = elemento_7.text 
        if re.search(r'\d', valor_11):  
          print('Los montos netos son  un carácter numérico.', valor_11)
        else:
          print('Los montos netos no es un carácter numérico.')
        
         # validar ventas recientes 

        elemento = self.driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/div/span[1]')

        # Obtener el texto del elemento
        texto_obtenido = elemento.text
        
        # Validar el texto
        texto_esperado = "Ventas Recientes"
        self.assertEqual(texto_obtenido, texto_esperado)

        ##Imprimir la respuesta en consola
        print("El texto obtenido es:", texto_obtenido)

        
        # validar la imagen del producto 


        imagen_5 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[1]/img")
     
        # Obtener la URL de la imagen
        url_imagen_obtenida = imagen_5.get_attribute('src')

        imagen_5_esperadas = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]

        # Validar si la URL obtenida está en la lista de URLs esperadas
        if url_imagen_obtenida in imagen_5_esperadas:
      
            print("La imagen es visible para el usuario. URL:", url_imagen_obtenida)
        else:
            print("La imagen no es visible para el usuario. URL:", url_imagen_obtenida)

       
        #validar la cantidad neta de la venta 

        elemento_6 = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span')
        valor_12 = elemento_6.text 
        if re.search(r'\d', valor_12):  
          print('El saldo de la cantidad netos es un carácter numérico.', valor_12)
        else:
          print('El saldo de la  cantidad netos no es un carácter numérico.')

       # validar precio de la venta 
        elemento_7 = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span[2]')
        valor_13 = elemento_7.text 
        if re.search(r'\d', valor_13):  
          print('El precio es un carácter numérico.', valor_13)
        else:
          print('El precio no es un carácter numérico.')

      

    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(inicio_tenat)
  runner = xmlrunner.XMLTestRunner(output='reportInicioTenat')
  runner.run(test_suite)
        
   
