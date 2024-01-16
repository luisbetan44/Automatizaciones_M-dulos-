import unittest
import xmlrunner
import time
from Elements import find_and_click_element, find_elements, validate_chain_text_xpaht, validate_text, validate_text_visible, validate_text_visible_selector
from loginhelper import LoginHelper
from startSession import StartSession




class cuenta_entregas(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_cuenta_entregas(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

        # ingresar al menú de cuentas 

        select_menu_Account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver,select_menu_Account )

        select_deliveries = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[2]/a"
        find_elements(self.driver,select_deliveries )
        time.sleep(3)


        #   Validar titulo de la pantalla 

        title_menu = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        tille_expected = "MIS ENTREGAS"
        validate_text(self.driver, title_menu, tille_expected )

        # selecionar botón del filtro
        selct_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[2]/app-filter-button/button/div/i"
        find_elements(self.driver, selct_filter )
        time.sleep(3)
 
        # limpiar  filtro 

        clean_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[1]/button"
        find_elements(self.driver, clean_filter )
        time.sleep(3)

        # aplicar filtro

        apply_product_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-grain-container/div/app-grain-button[2]/div/img"
        find_elements(self.driver, apply_product_filter )
        time.sleep(3)

        apply_Campaign_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-season-container/div/app-season-button[2]/div/div"
        find_elements(self.driver, apply_Campaign_filter )
        time.sleep(3)
       
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
        find_elements(self.driver, apply_filter )
        time.sleep(3)




        # Validar totalizadores 


        tn_bruto = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[1]/div/div[1]/app-totalizer/div/div/div[2]/div[2]/span[1]'
        tn_bruto_expected = ["231,36","2.313,60","231.360,00"]
        validate_chain_text_xpaht(self.driver, tn_bruto, tn_bruto_expected )  


        tn_netos = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[1]/div/div[2]/app-totalizer/div/div/div[2]/div[2]/span[1]'
        tn_netos_expected = ["391,06", "3.910,60", "391.060,00"]
        validate_chain_text_xpaht(self.driver, tn_netos, tn_netos_expected )  

        # seleccionar varios movimientos del listado 
        
        select_movements1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[1]/th/input'
        find_elements(self.driver, select_movements1 )
        time.sleep(3)

        select_movements2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[2]/th/input'
        find_elements(self.driver, select_movements2 )
        time.sleep(3)

        select_movements3 ='/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[3]/th/input'
        find_elements(self.driver, select_movements3 )
        time.sleep(3)

        # selecionar botón de descarga 

        selet_button_download = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, selet_button_download )
        time.sleep(3)

        apply_download_excel = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a"
        find_elements(self.driver, apply_download_excel )
        time.sleep(3)

        selet_button_download = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, selet_button_download )
        time.sleep(3)

        apply_download_pdf = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a"
        find_elements(self.driver, apply_download_pdf )
        time.sleep(3)


        # ingresar al detalle del tercer movimiento

        insert_movemenst = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-deliveries/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[3]/td[2]/span/span"
        find_elements(self.driver, insert_movemenst )
        time.sleep(3)

        # validar numero de Tk 

        number_TK = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-header-for-detail/div[1]/div'
        number_TK_expected = "Entrega TK 0001 00124125"
        validate_text_visible(self.driver, number_TK, number_TK_expected )

        # validar el total de toneladas de la entrega 

        tn_delivery = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-header-for-detail/div[2]/div/div[2]/div[1]'
        tn_delivery_expected = ["37,04 Tn", "370,40 QQ", "37.040,00 Kg"]
        validate_chain_text_xpaht(self.driver, tn_delivery, tn_delivery_expected ) 

        # validar producto

        type_product = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-header-for-detail/div[2]/div/div[2]/div[2]'
        type_product_expected = "De Maiz"
        validate_text_visible(self.driver, type_product, type_product_expected  )  


        # Validar  fecha campaña cuenta campo 

        title_delivery = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-detail-table/div/div/div[1]/div[1]/span'
        title_delivery_expected = "DATOS DE LA ENTREGA"
        validate_text_visible(self.driver, title_delivery, title_delivery_expected  )
        
        date_delivery = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-detail-table/div/div/div[1]/div[2]/div[1]/div[2]'
        date_delivery_expected = "27/04/2023"
        validate_text_visible(self.driver, date_delivery, date_delivery_expected  ) 

        campaign_delivery = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-detail-table/div/div/div[1]/div[2]/div[2]/div[2]'
        campaign_delivery_expected = "22/23"
        validate_text_visible(self.driver, campaign_delivery, campaign_delivery_expected  ) 

        business_name = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-detail-table/div/div/div[1]/div[2]/div[3]/div[2]'
        business_name_expected = "JUAN DEMO"
        validate_text_visible(self.driver, business_name, business_name_expected  )  
 
        field_business = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-detail-table/div/div/div[1]/div[2]/div[4]/div[2]'
        field_business_expected = "1399 LA MORENITA"
        validate_text_visible(self.driver, field_business,  field_business_expected  ) 

        # ingresar al analisis 

        into_analysis = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-deliveries/div/app-detail-table/div/div/div[2]/div[1]/div/button[1]"
        find_elements(self.driver, into_analysis )
        time.sleep(5)

        # validar titulo del analisis

        title_analysis = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-quality-analisis/app-detail-table-quality-analisis/div/div/div/div[1]/span'
        title_analysis_expected = "ANÁLISIS"
        validate_text_visible(self.driver, title_analysis,  title_analysis_expected  ) 
  

        data_analysis = '#layout-wrapper > div > div > div > app-quality-analisis > app-responsive-table > div > div.table-responsive > table > tbody > tr:nth-child(9) > td.text-nowrap.align-middle.f-size-12.ellipsis-cell.fw-bold > span > span'
        data_analysis_expected = "Peso Hectolítrico"
        validate_text_visible_selector(self.driver, data_analysis,  data_analysis_expected  )  

        foreign_matter = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-quality-analisis/app-responsive-table/div/div[2]/table/tbody/tr[9]/td[2]/span/span'
        foreign_matter_expected = "72%"
        validate_text_visible(self.driver, foreign_matter,  foreign_matter_expected  ) 


        # salir al listado 

        go_into_detail = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver, go_into_detail )
        time.sleep(2)

        go_to_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements(self.driver, go_to_list )
        time.sleep(3)








    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(cuenta_entregas)
  runner = xmlrunner.XMLTestRunner(output='reportCuentaEtregas')
  runner.run(test_suite)
   
   