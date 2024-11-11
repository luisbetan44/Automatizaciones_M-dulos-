import unittest
import xmlrunner
import time
from Constantes import Constantes
from Elements import click_checkbox_xpaht, find_and_click_element, find_and_click_element_selector, find_elements, find_elements_id, find_elements_located, validate_chain_text_xpaht, validate_character_numeric_element, validate_text_by_text, validate_text_visible
from loginhelper import LoginHelper
from startSession import StartSession


date_range_downwards = Constantes.DATE_RANGE_CONTRACT_DOWNWARDS

date_range_backwards = Constantes.DATE_RANGE_CONTRACT_BACKWARDS 

   



class detalle_ctro_entregaVentasV2(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_detail_deriverySales(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("484")

       # ingresar al menú de cuentas 

        select_menu_Account = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/a/span"
        find_elements(self.driver,select_menu_Account )

        

        select_grain = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[5]/div/ul/li[2]/a"
        find_elements(self.driver,select_grain )
        time.sleep(5)

        select_tab_contract = "current-contracts-tab"
        find_elements_id(self.driver, select_tab_contract)


        # Limpiar filtro que viene por default 
        
        select_filter = "//span[text() =' Filtros ']"
        find_elements(self.driver,select_filter )
        time.sleep(3)

        cleam_filter = "//span[text() ='Limpiar']"
        find_elements(self.driver,cleam_filter )
        time.sleep(3)

        # aplicar un nuevo filtro soja cosecha 2223 desde 03/04/2023 hasta 31/05/2023 estado cumplidos

        select_product_filter = "//div[text() = 'Trigo']"
        find_elements(self.driver,select_product_filter )
        time.sleep(3)

        select_campaign = "//div[text() = '23/24']"
        find_elements(self.driver, select_campaign )
        time.sleep(3)

        select_compliments = "Cumplidos"
        find_elements_id(self.driver, select_compliments )
        time.sleep(3)

        select_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-date-filter/div/app-date-picker/div/input[2]"
        find_elements(self.driver, select_filter )
        time.sleep(2)

        arrow_filter1 = "body > div > div.flatpickr-months > div > div > div > span.arrowDown"
        amount_click1 = date_range_downwards
        find_and_click_element_selector(self.driver, arrow_filter1, amount_click1)

        """arrow_filter2 = "/html/body/div/div[1]/span[1]"
        amount_click2 = date_range_backwards
        find_and_click_element(self.driver, arrow_filter2, amount_click2)"""

        select_date1 = "/html/body/div/div[2]/div/div[2]/div/span[17]"
        find_elements(self.driver, select_date1 )

       
        select_date2 = "/html/body/div/div[2]/div/div[2]/div/span[20]"
        find_elements(self.driver, select_date2 )

        apply_filter = "/html/body/ngb-offcanvas-panel/div/ngx-simplebar/div[1]/div[2]/div/div/div/app-filter-content/div[2]/app-filter-buttons/div/app-button[2]/button"
        find_elements(self.driver, apply_filter )
        time.sleep(5)

         # Validar el texto
        element10 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-contracts/app-responsive-table-multiple-items/div/div/span"
        text_expected = "Estado De Mis Contratos"
        validate_text_by_text(self.driver, text_expected)

        select_moviments = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[4]/app-tab-contracts/app-contracts/app-responsive-table-multiple-items/div/table/tbody/tr[1]/th/input"
        find_elements(self.driver, select_moviments )
        time.sleep(2)

        download_button1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[4]/app-tab-contracts/app-contracts/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, download_button1 )
        time.sleep(2)

        select_files_excel = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[4]/app-tab-contracts/app-contracts/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a'
        find_elements_located(self.driver, select_files_excel )
        time.sleep(5)

        download_button2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[4]/app-tab-contracts/app-contracts/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, download_button2 )
        time.sleep(2)

        select_files_pdf = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[4]/app-tab-contracts/app-contracts/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a'
        find_elements_located(self.driver, select_files_pdf )
        time.sleep(5)

        ## ingresa al primer movimiento del listado 
        
        selet_list_contract = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-grains/div/div[4]/app-tab-contracts/app-contracts/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/app-contract/div/div[2]"
        find_elements(self.driver, selet_list_contract )
        time.sleep(3)
       
        

        # validar numero de contrato 
        element1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[1]/div[1]/div/span"
        number_expected = "Contrato 124536"
        validate_text_visible(self.driver, element1, number_expected)

        # validar produto 
        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[1]/div[2]/div[2]/div[2]/span[2]'
        text_expected = "De Trigo"
        validate_text_visible(self.driver, element2, text_expected)
        
       # Validar kilos pactados 
        
        amount_kilos = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/div/div[2]/div/span"
        amount_kilos_expected = ["De 439,85 Tn Pactados", "De 4.398,53 QQ Pactados", "De 439.853,00 Kg Pactados"]
        validate_chain_text_xpaht(self.driver, amount_kilos, amount_kilos_expected)

        
        # scrollear hasta las solapas 
        
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(2)

        
      
        # validar Mis entregas 

        element3 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[1]/span'
        text_expected = "Mis Entregas"
        validate_text_visible(self.driver, element3, text_expected)

        self.driver.execute_script("window.scrollTo(0, 900);")
        

        element4 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/thead/tr/th[2]'
        text_expected = "Producto"
        validate_text_visible(self.driver, element4, text_expected)

        element5 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[1]/span/div/span'
        text_expected = "Trigo"
        validate_text_visible(self.driver, element5, text_expected)

        element6 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/thead/tr/th[3]'
        text_expected = "Fecha"
        validate_text_visible(self.driver, element6, text_expected)

        date_delivery = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[2]/span/div/span"
        strt_expected = "22/12/2023"
        validate_text_visible(self.driver,date_delivery, strt_expected)

        element7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/thead/tr/th[4]'
        text_expected = ["Kg Brutos","Tn Brutos", "QQ Brutos" ]
        validate_chain_text_xpaht(self.driver, element7, text_expected)

        gross_kilos = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[3]/span/div/span"
        validate_character_numeric_element(self.driver,gross_kilos)


        element8 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/thead/tr/th[5]'
        text_expected = "Humedad"
        validate_text_visible(self.driver, element8, text_expected)

        
        humidity = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[4]/span/div/span"
        validate_character_numeric_element(self.driver,humidity)

        element9 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/thead/tr/th[6]'
        text_expected = "Zaranda"
        validate_text_visible(self.driver, element9, text_expected)

        Zaranda = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[5]/span/div/span"
        validate_character_numeric_element(self.driver,Zaranda)


        element10 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/thead/tr/th[7]'
        text_expected = "Volátil"
        validate_text_visible(self.driver, element10, text_expected)

        volatile = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[6]/span/div/span"
        validate_character_numeric_element(self.driver,volatile)


        element11 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/thead/tr/th[8]"
        text_expected = "Factor/Grado"
        validate_text_visible(self.driver, element11, text_expected)

        degree_factor = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[7]/span/div/span"
        validate_character_numeric_element(self.driver,degree_factor)


        element12 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/thead/tr/th[9]'
        text_expected = ["Kg Netos","Tn Netos","QQ Netos"]
        validate_chain_text_xpaht(self.driver, element12, text_expected)

        net_kilos = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[8]/span/div/span"
        validate_character_numeric_element(self.driver,net_kilos)

        element13 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/thead/tr/th[10]'
        text_expected = "CTG/CRT"
        validate_text_visible(self.driver, element13, text_expected)

        number_ctgctr = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[1]/td[9]/span/div/span"
        validate_character_numeric_element(self.driver, number_ctgctr)
        time.sleep(2)


        select_moviments = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-responsive-table/div/div[2]/table/tbody/tr[1]/th/input"
        click_checkbox_xpaht(self.driver, select_moviments )
        time.sleep(2)

        download_button1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, download_button1 )
        time.sleep(2)

        select_files_excel = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[1]/a'
        find_elements(self.driver, select_files_excel )
        time.sleep(5)

        download_button2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-contract/app-contract-detail-tabs/div/div[1]/app-deliveries-applied/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/button[2]"
        find_elements(self.driver, download_button2 )
        time.sleep(2)

        select_files_pdf = '//*[@id="deliveries"]/app-deliveries-applied/app-deliveries-shared/app-header-for-responsive-table/div/div/div[2]/div/div[1]/app-download-button/div/ul/li[2]/a'
        find_elements_located(self.driver, select_files_pdf )
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0, -1200);")
        time.sleep(2)
        
        go_out_pag = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
        find_elements_located(self.driver, go_out_pag )
        time.sleep(5)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(detalle_ctro_entregaVentasV2)
  runner = xmlrunner.XMLTestRunner(output='reportCuentaContratosV2')
  runner.run(test_suite)
   