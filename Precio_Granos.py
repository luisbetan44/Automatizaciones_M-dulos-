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

     # localiza el input y envia el número de la cuenta 
        input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-options")))
        input_element.send_keys('1023')
      
       #selecciona el elemento oculto y crea un botón para hacer click sobre el 
        element_to_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search-dropdown > app-accounts-list > ngx-simplebar > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div.dropdown-sub-item.accounts-numbers")))
        driver.execute_script("arguments[0].style.display = 'block';", element_to_click)
        element_to_click.click()
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

        select_date = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[11]/div[2]/div/div[2]/div/span[31]")))
        select_date.click()
        time.sleep(2)






    
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= 'reportes', report_name='reporte_precioGranos'))
        


