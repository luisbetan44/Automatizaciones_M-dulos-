import re
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xmlrunner
import time
from loginhelper import LoginHelper
from startSession import StartSession

class Entregas_Tenant(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_entregas_tenant(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

        insertButton = self.driver.find_element(By.XPATH,"/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button")
        insertButton.click()
        time.sleep(3)
        
        ## seleccionar el tenant 
        selectTenant = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[8]/div/div/img")
        selectTenant.click()
        time.sleep(3)

     # localiza el input y envia el número de la cuenta 
        input_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "search-options")))
        input_element.send_keys('1023')
      
       #selecciona el elemento oculto y crea un botón para hacer click sobre el 
        element_to_click = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search-dropdown > app-accounts-list > ngx-simplebar > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div.dropdown-sub-item.accounts-numbers")))
        self.driver.execute_script("arguments[0].style.display = 'block';", element_to_click)
        element_to_click.click()
        time.sleep(3)

        # ingresar al menú de cuentas 

        select_menu_Account = self.driver.find_element(By.XPATH,
            "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        )
        select_menu_Account.click()


        # ingresar al submenú de reportes 

        select_menu_reports = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[6]/a")
        select_menu_reports.click()

        # seleccionar el filtro 

        select_filter_reports = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-reports/div/app-header-for-responsive-table/div/div/div[2]/div/div/app-filter-button/button/div/span")
        select_filter_reports.click()
        time.sleep(2)

        select_deliveries_sales = self.driver.find_element(By.XPATH,"/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-radio-button-list/div/app-radio[2]/div/input")
        select_deliveries_sales.click()
        time.sleep(2)

        select_filter_deliveries = self.driver.find_element(By.XPATH,"/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[2]/div/img")
        select_filter_deliveries.click()

        select_date_filter = self.driver.find_element(By.XPATH,"/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[3]/div/div")
        select_date_filter.click()

        apply_filter_button = self.driver.find_element(By.XPATH,"/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button")
        apply_filter_button.click()
        time.sleep(3)

        # validar formatos de reportes de entregas y ventas 

        title_deliveries_sales = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div/span")
        title_deliveries_sales_obtained = title_deliveries_sales.text
        title_deliveries_sales_expected = "Entregas y Ventas"
        if title_deliveries_sales_expected == title_deliveries_sales_obtained:
            print("El titulo de la pagina es: ",title_deliveries_sales_obtained)
        else:
            print("No se encontro el titulo de la pagina ")

        selected_grain = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div/div[1]/span")
        selected_grain_obtained = selected_grain.text
        selected_grain_expected = "Maiz"
        if selected_grain_expected == selected_grain_obtained:
            print("El producto seleccionado es: ",selected_grain_obtained)
        else:
            print("No se encontro el producto seleccionado")

        selected_campaign = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/div/div[2]/span")
        selected_campaign_obtained = selected_campaign.text
        selected_campaign_expected = "21/22"
        if selected_campaign_expected == selected_campaign_obtained:
            print("La campaña seleccionada es: ", selected_campaign_obtained)
        else:
            print("No se encontro la campaña seleccionada")

        kilos_delivered = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/table/tbody/tr[1]/td[2]/span/span")
        kilos_delivered_obtained = kilos_delivered.text
        kilos_delivered_expected = "20.782.982"
        if kilos_delivered_expected == kilos_delivered_obtained:
            print("Los kilos entregados son: ", kilos_delivered_obtained)
        else:
            print("No se encontraron los kilos entregados")


        other_movenment = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/table/tbody/tr[2]/td[2]/span/span')
        other_movenment_obtained = other_movenment.text
        other_movenment_expected = "-471.076"
        if other_movenment_expected == other_movenment_obtained:
            print("El saldo de otros movimientos es: ", other_movenment_obtained)
        else:
            print("No se encontro el saldo de otros movimientos")
     

        kilos_sales = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/table/tbody/tr[3]/td[2]/span/span") 
        kilos_sales_obtained = kilos_sales.text
        kilos_sales_expected = "20.484.508"
        if kilos_sales_expected == kilos_sales_obtained:
            print("Los kilos vendidos son:  ",kilos_sales_obtained)
        else:
            print("No se encontro los kilos vendidos")

        

        movement_balance = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-responsive-table/div/table/tbody/tr[6]/td[2]/span/span")
        movement_balance_obtained = movement_balance.text
        movement_balance_expected = "-172.602"
        if movement_balance_expected == movement_balance_obtained:
            print("El saldo es: ",movement_balance_obtained)
        else:
            print("No se encontro el saldo")

        

        trade_balance  = "-172.602"
        elemento = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{ trade_balance}')]")

       # Realizar validación del texto 
        trade_balance_obtained = elemento.text
        trade_balance_expected = "-172.602"
        assert trade_balance_obtained == trade_balance_expected

        if trade_balance_obtained:
           print("El saldo comercial es: ",trade_balance_obtained)

        else:
            print("No se encontro el saldo comercial")



        # descargar movimientos 

        select_button_downloads1 = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]")
        select_button_downloads1.click()
        time.sleep(2)

        select_option_excel = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a")
        select_option_excel.click()
        time.sleep(10)

        select_button_downloads2 = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]")
        select_button_downloads2.click()
        time.sleep(2)

        select_option_pdf = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/sales-deliveries/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a")
        select_option_pdf.click()
        time.sleep(10)

        go_out_reports = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a")
        go_out_reports.click()
        time.sleep(3)







    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(Entregas_Tenant)
  runner = xmlrunner.XMLTestRunner(output='reportEntregasVentas')
  runner.run(test_suite)
        

 