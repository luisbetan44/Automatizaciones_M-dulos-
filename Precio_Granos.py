from selenium  import webdriver
import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import Select


class precio_granos(unittest.TestCase):

    def     setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")


    def test_precio_granos(self):
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

    

        ## seleccionar el menú de granos 

        select_menu_grain = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span")
        select_menu_grain.click()
        time.sleep(2)

        # seleccionar submenú de precio de granos 

        price_grain = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[3]/a")
        price_grain.click()
        time.sleep(2)

        # validar titulo de la pantalla de precio de granos 

        title_international_market = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-international-market/app-market-table/app-market-header/app-market-header-info/div/div[1]/h4")
        title_international_expected = title_international_market.text
        title_international_obtained = "Mercado Internacional"

        if title_international_expected == title_international_obtained:
            print("El titulo de la pantalla es: ", title_international_obtained)

        else:
            print("El titulo de la pantalla no es el correcto")

       # validar el tipo de cambio y el banco 

        type_change = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-international-market/app-market-table/app-market-header/app-market-header-controls/div/app-market-currency/div[1]")
        type_change_expected = type_change.text
        type_change_obtained = "ARS 130.48"

        if type_change_expected == type_change_obtained:
            print("El tipo de cambio para el dia de hoy es :", type_change_obtained)

        else:
            print("El tipo de cambio no es correcto")

        # seleccionar un tipo de mercado 

 
        dropdown_element = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-international-market/app-market-table/app-market-header/app-market-header-controls/div/div/div/div[1]/select")

        # Crear un objeto Select para interactuar con el dropdown
        dropdown = Select(dropdown_element)

       # Seleccionar una opción por su valor
        dropdown.select_by_value("2")  

       # Obtener el elemento seleccionado en el dropdown
        option_seleccted = dropdown.first_selected_option

       # Hacer clic en el elemento seleccionado (en este caso, el <option> del dropdown)
        option_seleccted.click()
        time.sleep(2)

        # seleccionar fecha 

        date_market = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-international-market/app-market-table/app-market-header/app-market-header-controls/div/div/div/div[2]/app-date-picker/div/input[2]")))
        date_market.click()

        select_moth = driver.find_element_by_xpath("/html/body/div[1]/div[1]/span[2]")
        select_moth.click()

       
        target_date_xpath = f"/html/body/div[1]/div[2]/div/div[2]/div/span[18]"
        target_date_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, target_date_xpath)))
        target_date_element.click()
        time.sleep(2)

        ## agregar mercado internacional

        
        selct_button_add = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-international-market/app-market-table/app-market-header/app-market-header-controls/div/div/div/div[3]/app-add-and-clean/div/div[2]/app-button/button")
        selct_button_add.click()
        time.sleep(2)

        select_switch = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-international-market/app-market-table/div/table/tbody/tr[2]/td[1]/app-switch/div/input")
        select_switch.click()
        time.sleep(3)
       
        insert_product = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-international-market/app-market-table/div/table/tbody/tr[2]/td[2]/input")
        insert_product.send_keys("SOJA")
        insert_product.send_keys(Keys.ENTER)
        time.sleep(2)
       

        
        element_to_select = driver.find_element_by_css_selector('input[type="number"]')
        element_to_select.send_keys("300")
        element_to_select.send_keys(Keys.ENTER)
        time.sleep(2)

        # validar titulo de preccio de cereales 


        titel_price_cereal = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[1]/app-grain-price-header/app-grain-price-header-release/div/div[1]/h4")
        titel_price_cereal_expected = titel_price_cereal.text
        titel_price_cereal_obtained = "Precio de Cereales"

        if titel_price_cereal_expected == titel_price_cereal_obtained:
            print("El titulo del formulario es :", titel_price_cereal_obtained)

        else:
            print("El titulo del formulario no es correcto")

        

        titel_price_available = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/app-grain-price-table-header/div/div[1]")
        titel_price_available_expected = titel_price_available.text
        titel_price_available_obtained = "Disponible"

        if titel_price_available_expected == titel_price_available_obtained:
            print("El titulo del formulario es :", titel_price_available_obtained)

        else:
            print("El titulo del formulario no es correcto")


        add_comment = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[1]/app-grain-price-header/app-grain-price-header-observations/div/div[2]/div/div[2]/input")
        add_comment.send_keys("El cereal esta cargado")
        add_comment.send_keys(Keys.ENTER)
        time.sleep(2)

        

        # Agregar cerial 

        add_cereal_available = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/app-grain-price-table-header/div/div[2]/app-add-and-clean/div/div[1]/app-button/button')
        add_cereal_available.click()
        time.sleep(5)

        select_switch2 = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[1]/app-switch/div/input")
        select_switch2.click()
        time.sleep(3)

        select_grain = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[2]/app-select/select")
        select_grain.click()

        select_grain_dropdown = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[2]/app-select/select/option[8]")
        select_grain_dropdown.click()
        
        select_Campaign = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[3]/app-select/select")
        select_Campaign.click()

        select_Campaign_dropdown = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-market-main/app-grain-price/div[2]/app-grain-price-table[1]/div/div/table/tbody/tr/td[3]/app-select/select/option[2]")
        select_Campaign_dropdown.click()



        








        


    
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= 'reportes', report_name='reporte_precioGranos'))
        


