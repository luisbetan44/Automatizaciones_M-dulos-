import unittest
import xmlrunner
import time
from Elements import displace_element, displace_validate_element, find_and_click_element, find_elements, find_send_element, search_and_select_account, select_option_dropdown, select_option_dropdown_css_selector, validate_text, validate_text_by_text
from LoginSample import LoginSample
from startSession import StartSession




class granos_contratos(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_granos_contratos(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()

        select_grain = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span"
        find_elements(self.driver,select_grain)
        time.sleep(2)

        select_confir_sales = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[2]/a"
        find_elements(self.driver,select_confir_sales)
        time.sleep(2)

        # validar titulo de la pantalla
        
        
        text_expected = "CONTRATOS"
        validate_text_by_text(self.driver, text_expected)


        # cargar opción de tipo de confirmación
      
        button_dopdown = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[2]/div[2]/select"
        option_desired = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[2]/div[2]/select/option[9]"
        value_to_search = "Confirmación De Venta"
        select_option_dropdown(self.driver, button_dopdown, option_desired,value_to_search )

        element_text_2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[2]/div[2]/select/option[9]"
        text_expected_2 = "(VT) Confirmación De Venta"
        validate_text(self.driver, element_text_2, text_expected_2 )
        time.sleep(2)

        # insertar numero de cunta del productor
        
        numbert_the_account = "1023"  
        search_and_select_account(self.driver, numbert_the_account)
        
        # selecionar especie

        button_dopdown2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[4]/div[2]/select"
        option_desired2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[4]/div[2]/select/option[15]"
        value_to_search2 = "Soja"
        select_option_dropdown(self.driver, button_dopdown2, option_desired2, value_to_search2  )

        element_text_3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[4]/div[2]/select/option[15]"
        text_expected_3 = "Soja"
        validate_text(self.driver, element_text_3, text_expected_3 )

        # Cargar coseha
       
        button_dopdown3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[5]/div[2]/select"
        option_desired3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[5]/div[2]/select/option[3]"
        value_to_search3 = "22/23"
        select_option_dropdown(self.driver, button_dopdown3, option_desired3, value_to_search3 )

        element_text_4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[5]/div[2]/select/option[3]"
        text_expected_4 = "22/23"
        validate_text(self.driver, element_text_4, text_expected_4 )
        time.sleep(2)

        # ingresar cantidad
        
        insert_amount = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/app-input-for-long-form[1]/div/div[2]/div/input"
        send_amount = "300"
        find_send_element(self.driver,insert_amount,send_amount )

        # seleccionar modena

        button_dopdown4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[6]/div[2]/select"
        option_desired4 =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[6]/div[2]/select/option[2]"
        value_to_search4 = "ARS"
        select_option_dropdown(self.driver, button_dopdown4, option_desired4, value_to_search4) 

        element_text_5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[6]/div[2]/select/option[2]"
        text_expected_5 = "ARS"
        validate_text(self.driver, element_text_5, text_expected_5 )
        time.sleep(2)

        # ingresar precio

        insert_price = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/app-input-for-long-form[2]/div/div[2]/div/input"
        send_price = "3000"
        find_send_element(self.driver, insert_price, send_price )

        # seleccionar pizarra

        button_dopdown4 ="/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[7]/div[2]/select"
        option_desired4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[7]/div[2]/select/option[7]"
        value_to_search4 = "Rosario"
        select_option_dropdown(self.driver, button_dopdown4, option_desired4, value_to_search4 )

        element_text_6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[7]/div[2]/select/option[7]"
        text_expected_6 = "Rosario"
        validate_text(self.driver, element_text_6, text_expected_6 )

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

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

        select_date = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/div[8]/div[2]/app-date-picker/div/input[2]"
        find_elements(self.driver,select_date)

        
        select_arrow = "/html/body/div[1]/div[1]/span[2]"
        clicks = 1
        find_and_click_element(self.driver, select_arrow, clicks)

        insert_date = "/html/body/div[1]/div[2]/div/div[2]/div/span[32]"
        find_elements(self.driver, insert_date)
        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # ingrear código estándar

     
        button_dopdown5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[8]/div[2]/select"
        option_desired5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[8]/div[2]/select/option[2]"
        value_to_search5 = "General"
        select_option_dropdown(self.driver, button_dopdown5, option_desired5, value_to_search5)

        element_text_7 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[8]/div[2]/select/option[2]"
        text_expected_7 = "General"
        validate_text(self.driver, element_text_7, text_expected_7 )
        time.sleep(2)

        # seleccionar la fecha de pago

        select_date = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[2]/div[2]/app-date-picker/div/input[2]"
        find_elements(self.driver, select_date)
        time.sleep(2)

        select_arrow2 = "/html/body/div[1]/div[1]/span[2]"
        clicks = 1
        find_and_click_element(self.driver, select_arrow2, clicks) 

        select_calendar = "/html/body/div[1]/div[2]/div/div[2]/div/span[31]"
        find_elements(self.driver, select_calendar)
        time.sleep(1)

        #insertar rango de fecha 

        select_date = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[1]/div[2]/app-date-picker/div/input[2]"
        find_elements(self.driver, select_date)
        time.sleep(2)

        select_arrow3 = "/html/body/div[4]/div[1]/span[2]"
        clicks = 1
        find_and_click_element(self.driver, select_arrow3, clicks)
        
        select_calendar1 = "/html/body/div[4]/div[2]/div/div[2]/div/span[4]"
        find_elements(self.driver, select_calendar1)
        time.sleep(1)

        select_calendar2 = "/html/body/div[4]/div[2]/div/div[2]/div/span[31]"
        find_elements(self.driver, select_calendar2)
        time.sleep(1)


        
        # insertar campo plata
       
        button_dopdown6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/app-search-selector/ng-select/div/span"
        displace_element(self.driver, button_dopdown6)

        option_desired6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[2]"
        find_elements(self.driver, option_desired6)

        element_text_8 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[2]"
        text_expected_8 = "Carlos Pellegrini"
        displace_validate_element(self.driver, element_text_8, text_expected_8 )

        # insertar procedenia
        
        button_dopdown7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/app-search-selector/ng-select/div/span'
        displace_element(self.driver, button_dopdown7)

        option_desired7 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[3]/span"
        find_elements(self.driver, option_desired7)

        element_text_9 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[3]/span"
        text_expected_9 = "03 Playa S. Miguel (T6 y M. Pampa)"
        displace_validate_element(self.driver, element_text_9, text_expected_9 )

        # insertar destino
      
        button_dopdown8 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/app-search-selector/ng-select/div/span"
        displace_element(self.driver, button_dopdown8)

        option_desired8 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[6]/span"
        find_elements(self.driver, option_desired8)


        element_text_10 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[6]/span"
        text_expected_10 = "06 SECADA BONIFICADA"
        displace_validate_element(self.driver, element_text_10, text_expected_10 )
     

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # seleccionar el botón de continuar

        select_button_continue = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[2]/app-button[2]/button"
        find_elements(self.driver, select_button_continue)
        time.sleep(2)

        select_button_confirm = "/html/body/div[5]/div/div[6]/button[3]"
        find_elements(self.driver, select_button_confirm)
        time.sleep(2)

        # validar el mensaje de respuesta

      
        element_text_8 = "/html/body/div[5]/div/h2"
        text_expected_8 = "Confirmación de venta generada con éxito."
        validate_text(self.driver, element_text_8, text_expected_8 )
        time.sleep(2)

        select_finish = "/html/body/div/div/div[6]/button[1]"
        find_elements(self.driver, select_finish)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(granos_contratos)
  runner = xmlrunner.XMLTestRunner(output='reportGranosContratos')
  runner.run(test_suite)