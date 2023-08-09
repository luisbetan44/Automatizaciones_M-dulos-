import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC





class cuenta_entregas(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")

    def test_cuenta_entregas(self):
        driver = self.driver
        usermane = driver.find_element_by_id("email")
        usermane.send_keys("admingd@silohub.ag")
        usermane.send_keys(Keys.ENTER)
        time.sleep(3)


        passworUser = driver.find_element_by_id("password")
        passworUser.send_keys("G@viglio123")
        passworUser.send_keys(Keys.ENTER)
        time.sleep(3)

        insertButton = driver.find_element_by_xpath("/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button")
        insertButton.click()
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

        # ingresar al menú de cuentas 

        select_menu_Account = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        )
        select_menu_Account.click()

        select_deliveries = driver.find_element_by_xpath(
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[3]/a"
        )
        select_deliveries.click()
        time.sleep(3)



        #   Validar titulo de la pantalla 

        title_menu = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/div/span")
        title_obtained = title_menu.text
        tille_expected = "Mis Ventas"
        self.assertEqual(title_obtained, tille_expected)

        if title_obtained:
            print("El titulo de la pagina es:", title_menu.text)


        else:
              print("el titulo de la pagina no se enconto ")  


        # selecionar botón del filtro
        selct_filter = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/span")
        selct_filter.click()
        time.sleep(2)
 


        # limpiar  filtro 

        clean_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[1]/button")
        clean_filter.click()
        time.sleep(2)

        # aplicar filtro

        apply_product_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[1]/div/img")
        apply_product_filter.click()
        time.sleep(2)

        apply_Campaign_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[3]/div/div")
        apply_Campaign_filter.click()
        time.sleep(2)

        apply_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button")
        apply_filter.click()
        time.sleep(2)

        # seleccionar dos movimientos 

        select_product_list_1 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/table/tbody/tr[1]/th/input")
        select_product_list_1.click()
        time.sleep(1)


        select_product_list_2 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/table/tbody/tr[2]/th/input")
        select_product_list_2.click()
        time.sleep(1)



        select_product_list_3 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/table/tbody/tr[3]/th/input")
        select_product_list_3.click()
        time.sleep(1)

        # selecionar el botón para descargar los movimientos 

        button_download = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]")
        button_download.click()
        time.sleep(1)

        select_format = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a")
        select_format.click()
        time.sleep(3)

        # ingresar al detalle de una venta 
         
        insert_detail = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/table/tbody/tr[3]/td[3]/span/span")
        insert_detail.click()
        time.sleep(3)

        # validar número de venta 

        number_sale = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/app-header-for-detail/div[1]/div")
        number_sale_obtained = number_sale.text
        number_sale_expected = "Venta EP 0001 00111822"
        self.assertEqual(number_sale_obtained, number_sale_expected)

        if number_sale_obtained:
            print("El número de venta es:", number_sale.text)


        else:
              print("El número de venta no es correcto ")  

        # validar cantidad de kilos 

        amount_kilos = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/app-header-for-detail/div[2]/div/div[2]/div[2]")
        amount_kilos_obtained = amount_kilos.text
        amount_kilos_expected = "337.005,00 Kg"
        self.assertEqual(amount_kilos_obtained, amount_kilos_expected)

        if amount_kilos_obtained:
            print("La cantidad de kilos son:", amount_kilos.text)


        else:
              print("La cantidad de kilos no es la correcta ")  

        # validar producto
     
        type_product = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/app-header-for-detail/div[2]/div/div[2]/div[3]")
        type_product_obtained = type_product.text
        type_product_expected = "De Soja"
        self.assertEqual(type_product_obtained, type_product_expected)

        if type_product_obtained:
            print("El tipo de producto es:", type_product.text)


        else:
              print("El tipo de producto no es correcto ")  

       
     # validar datos de la venta 

        title_data = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/section/div/h2[1]")
        title_data_obtained = title_data.text
        title_data_expected = "DATOS DE LA VENTA"
        self.assertEqual(title_data_obtained, title_data_expected)

        if title_data_obtained:
            print("El titulo de la segunda card  es:", title_data.text)



        else:
              print("El tutilo de la segunda card no es correcto ")  

       

      # Validar fecha, campaña, mercado, fecha de vencimiento, numero de contrato  

        date_data = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/section/div/div[1]/div[1]")
        date_data_obtained = date_data.text
        date_data_expected = "07/03/2022"
        self.assertEqual(date_data_obtained, date_data_expected)

        if date_data_obtained:
            print("La fecha de la venta  es:", date_data.text)



        else:
              print("La fecha de la venta no es correcta ")  


        campaign_sale = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/section/div/div[1]/div[2]")
        campaign_sale_obtained = campaign_sale.text
        campaign_sale_expected = "20/21"
        self.assertEqual(campaign_sale_obtained, campaign_sale_expected)

        if campaign_sale_obtained:
            print("La campaña de la venta  es:", campaign_sale.text)



        else:
              print("La campaña de la venta no es correcta ")

        market_sale = driver.find_element_by_css_selector('#layout-wrapper > div > div > div > app-detail-sales > div:nth-child(2) > section > div > div:nth-child(3) > div:nth-child(3)')
        market_sale_obtained = market_sale.text
        market_sale_expected = "RENOVA - Soja  - Timbues"
        self.assertEqual(market_sale_obtained, market_sale_expected)

        if market_sale_obtained:
            print("El mercado  es:", market_sale.text)



        else:
              print("El mercado no es correcto ")  


        date_expiration = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/section/div/div[1]/div[4]")
        date_expiration_obtained = date_expiration.text
        date_expiration_expected = "PRECIOS DE FIJACIÓN"
        self.assertEqual(date_expiration_obtained, date_expiration_expected)

        if date_expiration_obtained:
            print("La fecha de venccimiento es:", date_expiration.text)



        else:
              print("La fecha de vencimiento  no es correcta ")  

  





    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'reporte_ventas'))
