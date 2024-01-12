import re
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xmlrunner

from loginhelper import LoginHelper
from startSession import StartSession

class HomeTenant(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_inicio_tenant(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

        ##seleccionar el botón filtro 
        Filtro_campaña = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[1]/div[2]/app-filter-button/button/div/span")
        Filtro_campaña.click()
      

   

        
        ## seleccionar filtro 

        delete_campaign = self.driver.find_element(By.XPATH,"/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-tag-container/div/div/div[7]/app-tag/div/div/i")
        delete_campaign.click()
     

        select_campaña = self.driver.find_element(By.XPATH,'/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[2]/div/div')
        select_campaña.click()
       

        selecct_button_aplicar = self.driver.find_element(By.XPATH,'/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button')
        selecct_button_aplicar.click()
        
       
       ## validar si el texto es visible para el usuario 
        element = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/app-welcome-home/div/div[1]/div/p')

        is_visible = element.is_displayed()

        if is_visible:
           print("El texto es visible para el usuario")
        else:
           print("El texto no es visible para el usuario")

       # Encontrar el elemento por su texto utilizando XPath
        texto_deseado = " Buen día JUAN DEMO!"
        elemento = self.driver.find_element(By.XPATH,f"//*[contains(text(), '{texto_deseado}')]")

       # Realizar validación del texto 
        texto_optenido = elemento.text
        texto_esperado = "Buen día JUAN DEMO!"
        assert texto_optenido == texto_esperado

        if texto_optenido:
           print("El texto del saludo fue validado correctamente", texto_optenido)

        else:
            print("No se pudo validar el texto del saludo")


     ##validar totalizadores vencidos a hoy 

        elemento = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[1]/app-number-values-card/div/div/div/div[3]/div/h4/span')
        valor_1 = elemento.text 
        if re.search(r'\d', valor_1):  
          print('El saldo vencido a hoy en ARS  es un carácter numérico.', valor_1)
        else:
          print('El saldo vencido a hoy en ARS no es un carácter numérico.')
   
        elemento = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[2]/app-number-values-card/div/div/div/div[3]/div/h4/span')
        valor_2 = elemento.text 
        if re.search(r'\d', valor_2):  
          print('El saldo vencido a hoy en USD  es un carácter numérico.', valor_2)
        else:
          print('El saldo vencido a hoy en USD no es un carácter numérico.')

        ##validar totalizadores  a vencer  

        elemento = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[3]/app-number-values-card/div/div/div/div[3]/div/h4/span')
        valor_3 = elemento.text 
        if re.search(r'\d', valor_3):  
          print('El saldo a vencer en ARS  es un carácter numérico.', valor_3)
        else:
          print('El saldo a vencer en ARS no es un carácter numérico.')


        elemento = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div/swiper/div/div[1]/div[4]/app-number-values-card/div/div/div/div[3]/div/h4/span')
        valor_4 = elemento.text 
        if re.search(r'\d', valor_4):  
          print('El saldo a vencer en USD  es un carácter numérico.', valor_4)
        else:
          print('El saldo a vencer en USD no es un carácter numérico.')
         
         ## Seleccionar el elemento que contiene el texto 

        elemento = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[1]/div[1]/div/p")
        texto_obtenido = elemento.text
        texto_esperado = "Resumen de Mis Negocios de Granos"
        self.assertEqual(texto_obtenido, texto_esperado)

      
        print("El texto obtenido es:", texto_obtenido)

        # Seleccionar el elemento de la imagen
        
        imagen_1 = self.driver.find_element(By.CSS_SELECTOR,'img[src="assets/images/grains/soja.svg"]')
     
        # Obtener la URL de la imagen
        url_imagen_obtenida = imagen_1.get_attribute('src')

        imagen_1_esperadas = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]

        # Validar si la URL obtenida está en la lista de URLs esperadas
        if url_imagen_obtenida in imagen_1_esperadas:
      
            print("La imagen es visible para el usuario. URL:", url_imagen_obtenida)
        else:
            print("No se puede localizar la imagen")

        # Seleccionar el elemento de la imagen

        imagen_2 = self.driver.find_element(By.CSS_SELECTOR,'img[src="assets/images/grains/maiz.svg"]')
     
        # Obtener la URL de la imagen
        url_imagen_obtenida = imagen_2.get_attribute('src')

        imagen_2_esperadas = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]

        # Validar si la URL obtenida está en la lista de URLs esperadas
        if url_imagen_obtenida in imagen_2_esperadas:
      
            print("La imagen es visible para el usuario. URL:", url_imagen_obtenida)
        else:
            print("No se puede localizar la imagen")

        # Seleccionar el elemento de la imagen
        
        imagen_3 = self.driver.find_element(By.CSS_SELECTOR,'img[src="assets/images/grains/trigo.svg"]')
        
        # Obtener la URL de la imagen
        
        url_imagen_3 = imagen_3.get_attribute("src")
    
        url_esperada_3 = "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg"
        self.assertEqual(url_imagen_3, url_esperada_3)

        print("la url de la imagen de trigo  es la siguente", url_imagen_3)

        ## validar los campor del resumen de mis negocios 
    
       ## entregado
       
        elemento_1 = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[2]/app-indicator-card/div/div[2]/div[1]/div[2]")
        valor_5 = elemento_1.text 
        if re.search(r'\d', valor_5):  
          print('El saldo entregado  es un carácter numérico.', valor_5)
        else:
          print('El saldo entregado no es un carácter numérico.')

        ## fijado 

        elemento_2 = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[3]/app-indicator-card/div/div[2]/div[1]/div[2]')
        valor_6 = elemento_2.text 
        if re.search(r'\d', valor_6):  
          print('El saldo fijado es un carácter numérico.', valor_6)
        else:
          print('El saldo fijado no es un carácter numérico.')

         ## pesificado

        elemento_3 = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[4]/app-indicator-card/div/div[2]/div[1]/div[2]')
        valor_7 = elemento_3.text 
        if re.search(r'\d', valor_7):  
          print('El saldo pesificado es un carácter numérico.', valor_7)
        else:
          print('El saldo pesificado no es un carácter numérico.')

        ## liquidado

        elemento_4 = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[5]/app-indicator-card/div/div[2]/div[1]/div[2]')
        valor_8 = elemento_4.text 
        if re.search(r'\d', valor_8):  
          print('El saldo liquidado es un carácter numérico.', valor_8)
        else:
          print('El saldo liquidado no es un carácter numérico.')

          ## pagado

        elemento_5 = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[6]/app-indicator-card/div/div[2]/div[1]/div[2]')
        valor_9 = elemento_5.text 
        if re.search(r'\d', valor_9):  
          print('El saldo pagado  es un carácter numérico.', valor_9)
        else:
          print('El saldo pagado no es un carácter numérico.')

        # validar entregas recientes 

        elemento = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/p')

        # Obtener el texto del elemento
        texto_obtenido = elemento.text
        
        # Validar el texto
        texto_esperado = "Entregas y Ventas Recientes"
        self.assertEqual(texto_obtenido, texto_esperado)

        ##Imprimir la respuesta en consola
        print("El texto obtenido es:", texto_obtenido)

        # validar la imagen del producto 


    

        imagen_4 = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[1]/img")
     
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
            print("No se puede localizar la imagen")


       

        #validar el numero de comprobante del movimiento 

        elemento_6 = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span')
        valor_10 = elemento_6.text 
        if re.search(r'\d', valor_10):  
          print('El comprobante CTG/CRT  es un carácter numérico.', valor_10)
        else:
          print('El comprobante CTG/CRT no es un carácter numérico.')

       # validar los Kilos netos 
        elemento_7 = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span')
        valor_11 = elemento_7.text 
        if re.search(r'\d', valor_11):  
          print('Los montos netos son  un carácter numérico.', valor_11)
        else:
          print('Los montos netos no es un carácter numérico.')
        
         # validar ventas recientes 

        elemento = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/div/span[1]')

        # Obtener el texto del elemento
        texto_obtenido = elemento.text
        
        # Validar el texto
        texto_esperado = "Ventas Recientes"
        self.assertEqual(texto_obtenido, texto_esperado)

        ##Imprimir la respuesta en consola
        print("El texto obtenido es:", texto_obtenido)

        
        # validar la imagen del producto 


        imagen_5 = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[1]/img")
     
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

        elemento_6 = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span')
        valor_12 = elemento_6.text 
        if re.search(r'\d', valor_12):  
          print('El saldo de la cantidad netos es un carácter numérico.', valor_12)
        else:
          print('El saldo de la  cantidad netos no es un carácter numérico.')

       # validar precio de la venta 
        elemento_7 = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span[2]')
        valor_13 = elemento_7.text 
        if re.search(r'\d', valor_13):  
          print('El precio es un carácter numérico.', valor_13)
        else:
          print('El precio no es un carácter numérico.')

      

    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(HomeTenant)
  runner = xmlrunner.XMLTestRunner(output='reportHomeTenat')
  runner.run(test_suite)
        
   
