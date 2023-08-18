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
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver.exe")
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
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[2]/a"
        )
        select_deliveries.click()
        time.sleep(3)



        #   Validar titulo de la pantalla 

        title_menu = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span")
        title_obtained = title_menu.text
        tille_expected = "MIS ENTREGAS"
        self.assertEqual(title_obtained, tille_expected)

        if title_obtained:
            print("El titulo de la pagina es:", title_menu.text)


        else:
              print("el titulo de la pagina no se enconto ")  


        # selecionar botón del filtro
        selct_filter = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/i")
        selct_filter.click()
        time.sleep(3)
 


        # limpiar  filtro 

        clean_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[1]/button")
        clean_filter.click()
        time.sleep(3)

        # aplicar filtro

        apply_product_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[2]/div/img")
        apply_product_filter.click()
        time.sleep(3)

        apply_Campaign_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[2]/div/div")
        apply_Campaign_filter.click()
        time.sleep(3)

        apply_filter = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button")
        apply_filter.click()
        time.sleep(3)





        # Validar totalizadores 


        tn_bruto = driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[1]/div/div[1]/app-totalizer/div/div/div[2]/div[2]/span[1]')
        tn_bruto_obtained = tn_bruto.text
        tn_bruto_expected = ["209.737,34","20.973,73","20.973.734,00"]
        

        if tn_bruto_obtained in tn_bruto_expected:
            print("El monto de tn brutos es:", tn_bruto_obtained)


        else:
              print("el monto de tn brutos no es correcto ")  


        tn_netos = driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[1]/div/div[2]/app-totalizer/div/div/div[2]/div[2]/span[1]')
        tn_netos_obtained = tn_netos.text
        tn_netos_expected = ["19.737.664,00", "197.376,64", "19.737,66 "]
        
        if tn_netos_obtained in tn_netos_expected:
            print("El monto de tn netos es:", tn_netos_obtained)


        else:
              print("el monto de tn n no es correcto ")  

        # seleccionar varios movimientos del listado 
        
        select_movements1 = driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div/div/div/app-deliveries/app-deliveries-shared/app-responsive-table/div/table/tbody/tr[1]/th/input')
        select_movements1.click()
        time.sleep(3)

        select_movements2 = driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div/div/div/app-deliveries/app-deliveries-shared/app-responsive-table/div/table/tbody/tr[2]/th/input')
        select_movements2.click()
        time.sleep(3)

        select_movements3 = driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div/div/div/app-deliveries/app-deliveries-shared/app-responsive-table/div/table/tbody/tr[3]/th/input')
        select_movements3.click()
        time.sleep(3)

        # selecionar botón de descarga 

        selet_button_download = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]")
        selet_button_download.click()
        time.sleep(3)

        apply_download_excel = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a")
        apply_download_excel.click()
        time.sleep(3)

        selet_button_download = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]")
        selet_button_download.click()
        time.sleep(3)

        apply_download_pdf = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a")
        apply_download_pdf.click()
        time.sleep(3)


        # ingresar al detalle del tercer movimiento

        insert_movemenst = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-responsive-table/div/table/tbody/tr[3]/td[2]/span/span")
        insert_movemenst.click()
        time.sleep(3)

        # validar numero de Tk 

        number_TK = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-header-for-detail/div[1]/div')
        number_TK_obtained = number_TK.text
        number_TK_expected = "Entrega TK 0008 00096336"
        self.assertEqual(number_TK_obtained, number_TK_expected)

        if number_TK_obtained:
            print("El número de la :", number_TK.text)


        else:
              print("El número de la entrega no es correcto ")  



        # validar el total de toneladas de la entrega 

        tn_delivery = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-header-for-detail/div[2]/div/div[2]/div[1]')
        tn_delivery_obtained = tn_delivery.text
        tn_delivery_expected = "30,11 Tn"
        self.assertEqual(tn_delivery_obtained, tn_delivery_expected)

        if tn_delivery_obtained:
            print("Las tn de la entrega son:", tn_delivery.text)


        else:
              print("El monto de tn de la entrega  no es correcto ")  

        # validar producto

        type_product = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-header-for-detail/div[2]/div/div[2]/div[2]')
        type_product_obtained = type_product.text
        type_product_expected = "De Maiz"
        self.assertEqual(type_product_obtained, type_product_expected)

        if type_product_obtained:
            print("El producto es:", type_product.text)


        else:
              print("El producto no es correcto ")  


        # Validar  fecha campaña cuenta campo 

        title_delivery = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-detail-table/div/div/div[1]/div[1]/span')
        title_delivery_obtained = title_delivery.text
        title_delivery_expected = "DATOS DE LA ENTREGA"
        self.assertEqual(title_delivery_obtained, title_delivery_expected)

        if title_delivery_obtained:
            print("El titulo es:", title_delivery.text)


        else:
              print("El titulo no es correcto ")  
        
        date_delivery = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-detail-table/div/div/div[1]/div[2]/div[1]/div[2]')
        date_delivery_obtained = date_delivery.text
        date_delivery_expected = "01/07/2022"
        self.assertEqual(date_delivery_obtained, date_delivery_expected)

        if date_delivery_obtained:
            print("La fecha de la entrega es:", date_delivery.text)


        else:
              print("La feccha de la entrega no es correcta ") 

        campaign_delivery = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-detail-table/div/div/div[1]/div[2]/div[2]/div[2]')
        campaign_delivery_obtained = campaign_delivery.text
        campaign_delivery_expected = "21/22"
        self.assertEqual(campaign_delivery_obtained, campaign_delivery_expected)

        if campaign_delivery_obtained:
            print("La campaña de la entrega es:", campaign_delivery.text)


        else:
              print("La campaña de la entrega no es correcta ") 

        business_name = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-detail-table/div/div/div[1]/div[2]/div[3]/div[2]')
        business_name_obtained = business_name.text
        business_name_expected = "JUAN DEMO"
        self.assertEqual(business_name_obtained, business_name_expected)

        if business_name_obtained:
            print("La razón social del cliente es:", business_name.text)


        else:
              print("La razón social del cliente no es correcta ")  
 
        field_business = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-detail-table/div/div/div[1]/div[2]/div[4]/div[2]')
        field_business_obtained = field_business.text
        field_business_expected = "8012 La Laura"
        self.assertEqual(field_business_obtained, field_business_expected)

        if field_business_obtained:
            print("El campo utilizado en la entrega  es:", field_business.text)


        else:
              print("El campo  localizado no es correcto ") 

        # ingresar al analisis 

        into_analysis = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-detail-table/div/div/div[2]/div[1]/div/button[1]")
        into_analysis.click()
        time.sleep(5)

        # validar titulo del analisis

        title_analysis = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-quality-analisis/app-detail-table-quality-analisis/div/div/div/div[1]/span')
        title_analysis_obtained = title_analysis.text
        title_analysis_expected = "ANÁLISIS"
        self.assertEqual(title_analysis_obtained, title_analysis_expected)

        if title_analysis_obtained:
            print("El titulo es:", title_analysis.text)


        else:
              print("El titulo no es correcto ")  

 
        date_analysis = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-quality-analisis/app-detail-table-quality-analisis/div/div/div/div[2]/div[1]/div[2]')
        date_analysis_obtained = date_analysis.text
        date_analysis_expected = "01/07/2022"
        self.assertEqual(date_analysis_obtained, date_analysis_expected)

        if date_analysis_obtained:
            print("La fecha del analisis es:", date_analysis.text)


        else:
              print("La fecha del analisis no es correcta ") 

        number_letter = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-quality-analisis/app-detail-table-quality-analisis/div/div/div/div[2]/div[3]/div[2]')
        number_letter_obtained = number_letter.text
        number_letter_expected = "10105175954"
        self.assertEqual(number_letter_obtained, number_letter_expected)

        if number_letter_obtained:
            print("El número de la carta porte es:", number_letter.text)


        else:
              print("El número de la carta porte no es correcto ")  


        # salir al listado 

        go_into_detail = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a")
        go_into_detail.click()
        time.sleep(2)

        go_to_list = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a")
        go_to_list.click()
        time.sleep(3)








    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'reporte_entregas'))
   