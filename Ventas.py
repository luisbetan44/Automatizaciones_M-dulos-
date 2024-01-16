import unittest
import xmlrunner
import time
from Elements import find_and_click_element, find_elements, validate_chain_text_xpaht, validate_text, validate_text_by_text, validate_text_visible, validate_text_visible_selector
from loginhelper import LoginHelper
from startSession import StartSession




class cuenta_ventas(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_cuenta_ventas(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

        # ingresar al menú de cuentas 

        select_menu_Account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver,select_menu_Account )


        select_sales = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[3]/a"
        find_elements(self.driver, select_sales )
        time.sleep(3)



        #   Validar titulo de la pantalla 

        title_menu = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/div/span"
        tille_expected = "Mis Ventas"
        validate_text_visible(self.driver, title_menu, tille_expected )  


        # selecionar botón del filtro
        selct_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/span"
        find_elements(self.driver,selct_filter )
        time.sleep(2)
 


        # limpiar  filtro 

        clean_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[1]/button"
        find_elements(self.driver,clean_filter )
        time.sleep(2)

        # aplicar filtro

        apply_product_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[1]/div/img"
        find_elements(self.driver,apply_product_filter )
        time.sleep(2)

        apply_Campaign_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[3]/div/div"
        find_elements(self.driver,apply_Campaign_filter )
        time.sleep(2)

        select_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        find_elements(self.driver, select_filter )
        time.sleep(2)

        arrow_filter1 = "/html/body/div/div[1]/span[1]"
        amount_click1 = 10
        find_and_click_element(self.driver, arrow_filter1, amount_click1)

        select_date1 = "/html/body/div/div[2]/div/div[2]/div/span[3]"
        find_elements(self.driver, select_date1 )

        arrow_filter2 = "/html/body/div/div[1]/span[2]"
        amount_click2 = 1
        find_and_click_element(self.driver, arrow_filter2, amount_click2)

        select_date2 = "/html/body/div/div[2]/div/div[2]/div/span[35]"
        find_elements(self.driver, select_date2 )

        apply_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver,apply_filter )
        time.sleep(2)

        # seleccionar dos movimientos 

        select_product_list_1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[1]/th/input"
        find_elements(self.driver, select_product_list_1 )
        time.sleep(1)


        select_product_list_2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[2]/th/input"
        find_elements(self.driver, select_product_list_2 )
        time.sleep(1)



        select_product_list_3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[3]/th/input"
        find_elements(self.driver, select_product_list_3 )
        time.sleep(1)

        # selecionar el botón para descargar los movimientos 

        button_download = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, button_download )
        time.sleep(1)

        select_format = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, select_format )
        time.sleep(3)

        # ingresar al detalle de la tercera venta 
         
        insert_detail = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sales/app-sales-shared/app-responsive-table/div/div/table/tbody/tr[3]/td[1]"
        find_elements(self.driver, insert_detail )
        time.sleep(3)

        # validar número de venta 

        number_sale = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/app-header-for-detail/div[1]/div"
        number_sale_expected = "Venta F 0001 00118245"
        validate_text_visible(self.driver, number_sale, number_sale_expected ) 

        # validar cantidad de kilos 

        amount_kilos = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/app-header-for-detail/div[2]/div/div[2]/div[2]"
        amount_kilos_expected = ["150.000,00 Kg", "150,00 Tn", "1.500,00 QQ"]
        validate_chain_text_xpaht(self.driver, amount_kilos, amount_kilos_expected)
        
        # validar producto
     
        type_product = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/app-header-for-detail/div[2]/div/div[2]/div[3]"
        type_product_expected = "De Soja"
        validate_text_visible(self.driver,type_product, type_product_expected ) 
     # validar datos de la venta 

        title_data = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/section/div/h2[1]"
        title_data_expected = "DATOS DE LA VENTA"
        validate_text_visible(self.driver,title_data, title_data_expected )   

    # Validar fecha, campaña, mercado, fecha de vencimiento, numero de contrato  

        date_data = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/section/div/div[1]/div[1]"
        date_data_expected = "29/03/2023"
        validate_text_visible(self.driver, date_data, date_data_expected )

        campaign_sale = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/section/div/div[1]/div[2]"
        campaign_sale_expected = "21/22"
        validate_text_visible(self.driver, campaign_sale, campaign_sale_expected )



        expected_text = "03 Playa S. Miguel (T6 y M. Pampa)"
        validate_text_by_text(self.driver, expected_text)
       

        

        date_expiration = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-sales/div[1]/section/div/div[1]/div[4]"
        date_expiration_expected = "24/08/2022"
        validate_text_visible(self.driver, date_expiration, date_expiration_expected )  

        
        go_out_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver, go_out_list )
        time.sleep(2)

        



  





    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(cuenta_ventas)
  runner = xmlrunner.XMLTestRunner(output='reportCuentaVentas')
  runner.run(test_suite)
   
