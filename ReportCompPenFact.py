import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC
import re
import xmlrunner



class comprobantes_Pend_Facturar(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")

    def test_comprobantes_pend_fact(self):
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
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        )
        select_menu_Account.click()


        # ingresar al submenú de reportes 

        select_menu_reports = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[6]/a")
        select_menu_reports.click()

        # seleccionar el filtro 

        select_filter_reports = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-reports/div/app-header-for-responsive-table/div/div/div[2]/div/div/app-filter-button/button/div/span")
        select_filter_reports.click()
        time.sleep(2)

        select_receipts_pending = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-radio-button-list/div/app-radio[1]/div/input")
        select_receipts_pending.click()
        time.sleep(2)

        apply_option_select = driver.find_element_by_xpath("/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button")
        apply_option_select.click()
        time.sleep(2)

        # validar título de la pantalla 

        title_page_receipts = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/div/div/div[1]")
        title_page_receipts_obtained = title_page_receipts.text
        title_page_receipts_expected = "Comprobantes Pendientes de Facturar"
        if title_page_receipts_expected == title_page_receipts_obtained:
            print("El titulo de la pantalla es: ", title_page_receipts_obtained)
        else:
            print("No se encontro el titulo de la pagina")  

        # validar formato de la pagina 

        first_column = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/table/thead/tr/th[2]")
        first_column_obtained = first_column.text
        first_column_expected = "Comprobante"
        if first_column_expected == first_column_obtained:
            print("La primera columna es:  ",first_column_obtained)

        else:
            print("No se encontro la primera columna")

        second_column = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/table/thead/tr/th[3]")
        second_column_obtained = second_column.text
        second_column_expected = "Artículo"
        if second_column_expected == second_column_obtained:
            print("La segunda columna es:  ",second_column_obtained)

        else:
            print("No se encontro la segunda columna")


        third_column = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/table/thead/tr/th[4]")
        third_column_obtained = third_column.text
        third_column_column_expected = "Pendiente"
        if third_column_column_expected == third_column_obtained:
            print("La tercera columna es:  ",third_column_obtained)

        else:
            print("No se encontro la tercera columna")

        quarter_column = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/table/thead/tr/th[5]")
        quarter_column_obtained = quarter_column.text
        quarter_column_expected = "Precio Unit."
        if quarter_column_expected == quarter_column_obtained:
            print("La cuarte columna es: ", quarter_column_obtained)
        else:
            print("No se encontro la cuarta columna")

        fifth_column = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/table/thead/tr/th[6]")
        fifth_column_obtained =  fifth_column.text
        fifth_column_expected = "Moneda"
        if  fifth_column_expected ==  fifth_column_obtained:
            print("La quinta columna es: ",  fifth_column_obtained)
        else:
            print("No se encontro la quinta columna")

        sixth_column = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/table/thead/tr/th[7]")
        sixth_column_obtained = sixth_column.text
        sixth_column_expected = "Total"
        if sixth_column_expected == sixth_column_obtained:
            print("La sexta columna es: ", sixth_column_obtained)
        else:
            print("No se encontro la sexta columna")    

       # validar tipos de caracteres en la descripción de los productos 

        number_voucher = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/table/tbody/tr[1]/td[1]/span/span")
        number_voucher_obtained = number_voucher.text 
        if re.search(r'\d', number_voucher_obtained):  
          print('El numero de comprobante es un carácter numérico.')
        else:
          print('El numero del comprobante no es un carácter numérico.')
        
        article_description = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/table/tbody/tr[1]/td[2]/span/span")
        article_obtaired = article_description.text
        if isinstance(article_obtaired,str):
           print("La descripcion del articulo es un string. ")
        else:
           print("La descripcion del articulo no es un string") 

        # ingresar al detalle 
             
        enter_detail = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-pendient/app-responsive-table/div/table/tbody/tr[1]/td[2]/span/span")
        enter_detail.click()


        # validar titulo del detalle 

        title_detail = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-pendient/div[1]/section/div/h2")
        title_detail_obtained = title_detail.text
        title_detail_expected = "DATOS DEL COMPROBANTE PENDIENTE DE FACTURAR"
        if title_detail_expected == title_detail_obtained:
           print("El titulo de la pantalla del detalle es: ", title_detail_obtained)
        else: 
           print("No se encontro el titulo de la pantalla del detalle")


     # validar descripcion de los campos del detalle 

        field_date =  driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-pendient/div[1]/section/div/div[1]/div[1]/strong/div")
        field_date_obtained = field_date.text
        field_date_expected = "FECHA"
        if field_date_expected == field_date_obtained:
            print("La primera descripcion de los campos en el detalle es:  ",field_date_obtained)
        else:
            print("No se encuentra la descripcion del primer campo del detalle")

        field_article =  driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-pendient/div[1]/section/div/div[1]/div[2]/strong/div")
        field_article_obtained = field_article.text
        field_article_expected = "ARTÍCULO"
        if field_article_expected == field_article_obtained:
            print("La segunda descripcion de los campos en el detalle es:  ",field_article_obtained)
        else:
            print("No se encuentra la descripcion del segundo campo del detalle")

        field_amount =  driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-pendient/div[1]/section/div/div[1]/div[3]/strong/div")
        field_amount_obtained = field_amount.text
        field_amount_expected = "CANTIDAD"
        if field_amount_expected == field_amount_obtained:
            print("La tercera descripcion de los campos en el detalle es:  ",field_amount_obtained)
        else:
            print("No se encuentra la descripcion del tercer campo del detalle")

        pending_amount =  driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-pendient/div[1]/section/div/div[1]/div[4]/strong/div")
        pending_amount_obtained = pending_amount.text
        pending_amount_expected = "CANTIDAD PENDIENTE"
        if pending_amount_expected == pending_amount_obtained:
            print("La cuarta descripcion de los campos en el detalle es:  ",pending_amount_obtained)
        else:
            print("No se encuentra la descripcion del cuarto campo del detalle")

        # validar tipo de caracteres en los datos del detalle 

        date_field = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-pendient/div[1]/section/div/div[1]/div[1]/div")
        date_obtaired = date_field.text
        if isinstance(date_obtaired,str):
           print("La descripcion de la fecha es un string. ")
        else:
           print("La descripcion de la fecha no es un string")

        descrition_article = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-pendient/div[1]/section/div/div[1]/div[2]/div")
        article_obtaired = descrition_article.text
        if isinstance(article_obtaired,str):
           print("La descripcion de la fecha es un string. ")
        else:
           print("La descripcion de la fecha no es un string")  

        # salir del detalle 

        go_out_page = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a")
        go_out_page.click()
        time.sleep(2)

        # salir de la pagina

        go_out_report = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a")
        go_out_report.click()
        time.sleep(2) 










    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(comprobantes_Pend_Facturar)
  runner = xmlrunner.XMLTestRunner(output='reportComproPendFact')
  runner.run(test_suite)
        

 