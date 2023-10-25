import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.ui import Select


class Fijacion_tipo_cambio(unittest.TestCase):


    def    setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://pwa-portal-staging.silohub.ag/login")


    def test_login_user(self):
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


        select_tenant = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[8]/div/div/img')
        select_tenant.click()
        time.sleep(3)

        select_granos = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span')
        select_granos.click()
        time.sleep(2)



        select_fijaciones = driver.find_element_by_xpath('/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[1]/a')
        select_fijaciones.click()


        ## validar que estamos en la solapa fijaciones habilitadas 
        elemento = driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/ul/li[1]/a')
        valor = elemento.text 
        valor_esperado = "Fijaciones Habilitadas"
        if valor == valor_esperado:
           print("Nos encontramos en la solapa Fijaciones Habilitadas")
        else:
           print("no estamos ubicados en la solapa Fijaciones Habilitadas") 

       ## localiza el input y envia el número de la cuenta 
        input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/div/div[1]/app-bindings-enabled-list/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/div/div/div[2]/input")))
        input_element.send_keys('1023')
      
       #selecciona el elemento oculto y crea un botón para hacer click sobre el 
        element_to_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/div/div[1]/app-bindings-enabled-list/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div/span")))
        driver.execute_script("arguments[0].style.display = 'block';", element_to_click)
        element_to_click.click()
        time.sleep(3)
       

        

        select_button_pinup = driver.find_element_by_css_selector("#current-account-applied > app-bindings-enabled-list > app-responsive-table-multiple-items > div > table > tbody > tr:nth-child(10) > td:nth-child(5) > div > div:nth-child(1) > app-button > button")
        wait = WebDriverWait(driver, 10)
        select_button_pinup = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#current-account-applied > app-bindings-enabled-list > app-responsive-table-multiple-items > div > table > tbody > tr:nth-child(10) > td:nth-child(5) > div > div:nth-child(1) > app-button > button")))
        select_button_pinup.click()

        # validar el título de la pantalla 

        title_pinup_grain = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-exchange/div[1]/div[1]/section/form/div/h2")
        title_pinup_grain_obtained = title_pinup_grain.text
        title_pinup_grain_expected = "Nueva Fijación de Tipo de Cambio"
        if title_pinup_grain_expected == title_pinup_grain_obtained:
           print("El título de la pagina es: ",title_pinup_grain_obtained)
        else:
           print("No se encontro el título de la pagina")

        ## ingresar cantidad a fijar 
        insert_amount_grain = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-exchange/div[1]/div[1]/section/form/div/div/div[6]/div/div/input")
        insert_amount_grain.send_keys("100")
        insert_amount_grain.send_keys(Keys.ENTER)
        time.sleep(2)

        ## selecciona el mercado 

        select_market = Select(driver.find_element_by_css_selector('select[aria-label="Default select example"]'))
        select_market.select_by_value("ROS") 

        selected_option = select_market.first_selected_option
        selected_option.click()

        ## insertar el precio

        insert_price_grain = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-exchange/div[1]/div[1]/section/form/div/div/div[10]/div/div/input")
        insert_price_grain.send_keys("30000")
        insert_price_grain.send_keys(Keys.ENTER)
        time.sleep(2)

        ## seleccionar fecha 

        select_date = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-exchange/div[1]/div[1]/section/form/div/div/div[16]/div/app-date-picker/div/input[2]")
        select_date.click()
        time.sleep(2)

        select_date_day = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/span[37]")
        select_date_day.click()
        time.sleep(2)

        select_nex_button = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div[1]/div[1]/section/form/div/div/div[18]/div/div[2]/app-button/button")
        select_nex_button.click()
        time.sleep(2)







    
    def tearDown(self):
        self.driver.close()







if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'reporte_fijación_tdc'))
        