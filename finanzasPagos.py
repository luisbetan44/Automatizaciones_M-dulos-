import unittest
import xmlrunner
import time
from Elements import delete_element,  find_elements, find_elements_css_selector, select_option_click, send_element, validate_text
from Elements2 import verify_todate
from loginhelper import LoginHelper
from startSession import StartSession




class finanzaspagos(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_finance_payment(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")



        # ingresar al menú de finanza 

        select_menu_finance = "//span[text() = ' Finanzas']"
        find_elements(self.driver, select_menu_finance)
        time.sleep(2)

        select_menu_payment = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[7]/div/ul/li[1]/a"
        find_elements(self.driver, select_menu_payment)
        time.sleep(2)

        # validar el título de la pagina 

        title_vouchers = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-charges/div[2]/div/div[1]"
        title_vouchers_expected = "Listado de Comprobantes"
        validate_text(self.driver, title_vouchers, title_vouchers_expected)
        time.sleep(2)

       ## seleccionar el primer movimiento del listado

        select_movements_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-charges/app-responsive-table/div/div/table/tbody/tr[1]/th/input"
        find_elements(self.driver, select_movements_list)
        time.sleep(2)
       
       # selecciona el botón de cobrar
       
        select_button_payment = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-charges/div[1]/div[2]/div/button'
        find_elements(self.driver, select_button_payment)
        time.sleep(2)

       ## editar monto 
        
        select_icon_pencil = "#layout-wrapper > div > div > div > app-forecast-main > div > app-selected-voucher > app-responsive-table > div > div.table-responsive > table > tbody > tr > td:nth-child(5) > app-row-for-finance-forecast > td > div > svg-icon:nth-child(2) > svg"
        find_elements_css_selector(self.driver, select_icon_pencil)
        time.sleep(2)

        cleam_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/app-selected-voucher/app-responsive-table/div/div[2]/table/tbody/tr/td[5]/app-row-for-finance-forecast/td/div/input"
        delete_element(self.driver, cleam_account)
        time.sleep(2)

        
        select_input_amount = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/app-selected-voucher/app-responsive-table/div/div[2]/table/tbody/tr/td[5]/app-row-for-finance-forecast/td/div/input'
        send_account = '10000'
        send_element(self.driver, select_input_amount,send_account )

        select_out_click = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/app-selected-voucher/app-responsive-table/div/div[2]/table/tbody/tr/td[3]/app-row-for-finance-forecast/td/div/span"
        find_elements(self.driver, select_out_click)

        select_button_confirm = "/html/body/div[2]/div/div[6]/button[3]"
        find_elements(self.driver, select_button_confirm)
        
        

        select_button_add = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/app-means-of-payment-table/div/div/div/app-button/button"
        find_elements(self.driver, select_button_add)
        time.sleep(2)

        button_dopdown1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/app-means-of-payment-table/div/table/tbody/tr/td[1]/app-select/select"
        option_desired1 =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/app-means-of-payment-table/div/table/tbody/tr/td[1]/app-select/select/option[1]"
        select_option_click(self.driver, button_dopdown1, option_desired1, )
        time.sleep(2)
 

        button_dopdown2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/app-means-of-payment-table/div/table/tbody/tr/td[2]/app-select/select"
        option_desired2 =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/app-means-of-payment-table/div/table/tbody/tr/td[2]/app-select/select/option[3]"
        select_option_click(self.driver, button_dopdown2, option_desired2, )
        time.sleep(2)
 

        select_button_confirm2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/div[2]/app-button[2]/button"
        find_elements(self.driver, select_button_confirm2)
        time.sleep(2)

        select_button_continue = "/html/body/div[2]/div/div[6]/button[3]"
        find_elements(self.driver, select_button_continue)
        time.sleep(5)

        select_button_accept = "/html/body/ngb-modal-window/div/div/app-preview-created-forecast/div/div[4]/app-button/button"
        find_elements(self.driver, select_button_accept)
        time.sleep(5)

        # ingresar al menú de mis solicitudes

        select_menu_requests = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[7]/div/ul/li[2]/a"
        find_elements(self.driver, select_menu_requests)
        time.sleep(2)

        # ingresar al detalle del movimiento 

        select_icon_eyes = "#layout-wrapper > div > div > div > app-charge-request-main > div.mt-4 > app-responsive-table > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(7) > app-row-for-finance-charge-request > td > svg-icon > svg"
        find_elements_css_selector(self.driver, select_icon_eyes)
        time.sleep(2)

        select_todate = "#layout-wrapper > div > div > div > app-payment-collection-detail-main > div > div > div:nth-child(2) > app-totalizer-forecast > div > div > div.col-9.row.totalizer-values > div:nth-child(2) > span"
        verify_todate(self.driver,select_todate)
        time.sleep(2)

        canceled_amount = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-payment-collection-detail-main/div/app-selected-voucher-detail/app-responsive-table/div/div[2]/table/tbody/tr/td[5]/span/div/span"
        value_amount = "ARS 100,00"
        validate_text(self.driver, canceled_amount, value_amount)

        got_to_page = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver, got_to_page)
        time.sleep(3)



        




    

    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(finanzaspagos)
  runner = xmlrunner.XMLTestRunner(output='reportfinanzaspago')
  runner.run(test_suite)
        
