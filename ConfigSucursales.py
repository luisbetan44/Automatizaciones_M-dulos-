import unittest
import time
import xmlrunner
from Elements import display_and_do_click, find_elements, find_elements_css_selector, validate_text
from LoginSample import LoginSample
from startSession import StartSession


class config_Sucursales(unittest.TestCase):


    def    setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_settings_branch_offices(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()
        

       

        select_settings = '#navbar-nav > li:nth-child(10) > a > span'
        find_elements_css_selector(self.driver,select_settings )
        time.sleep(2)

        
        select_branch_offices = '/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[10]/div/ul/li[7]/a'
        display_and_do_click(self.driver,select_branch_offices )
        time.sleep(2)


        ## validar titulo 
        title_page = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
        value_expected = "SUCURSALES"
        validate_text(self.driver, title_page, value_expected  )
        

        title_branch_offices = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[1]/app-branch/app-responsive-table/div/div/table/thead/tr/th[1]"
        value_expected = "Nombre Sucursal"
        validate_text(self.driver,title_branch_offices, value_expected  )

        name_branch_offices = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[1]/app-branch/app-responsive-table/div/div/table/tbody/tr[1]/td[1]/div/span"
        value_expected = "Angellica - Casa Central"
        validate_text(self.driver,name_branch_offices, value_expected  )

        deposits_name = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[1]/app-branch/app-responsive-table/div/div/table/thead/tr/th[2]"
        value_expected = "Depositos"
        validate_text(self.driver,deposits_name, value_expected  )
      

        
        select_edit = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[1]/app-branch/app-responsive-table/div/div/table/tbody/tr[1]/td[3]/div/button'
        find_elements(self.driver,select_edit )
        time.sleep(2)


        #seleccionar checkbox y volver a seleccionarlos para desactivar y activar  

        select_option1 = '/html/body/ngb-modal-window/div/div/app-edit-branch-office/div/div[2]/div/div[2]/div[1]/div/input'
        find_elements(self.driver,select_option1 )
        time.sleep(2)

        select_option2 = '/html/body/ngb-modal-window/div/div/app-edit-branch-office/div/div[2]/div/div[2]/div[2]/div/input'
        find_elements(self.driver,select_option2 )
        time.sleep(2)

        select_option3 = '/html/body/ngb-modal-window/div/div/app-edit-branch-office/div/div[2]/div/div[2]/div[3]/div/input'
        find_elements(self.driver,select_option3 )
        time.sleep(2)

        select_option4 = '/html/body/ngb-modal-window/div/div/app-edit-branch-office/div/div[2]/div/div[2]/div[1]/div/input'
        find_elements(self.driver,select_option4 )
        time.sleep(2)

        select_option5 = '/html/body/ngb-modal-window/div/div/app-edit-branch-office/div/div[2]/div/div[2]/div[2]/div/input'
        find_elements(self.driver,select_option5 )
        time.sleep(2)

        select_option6 = '/html/body/ngb-modal-window/div/div/app-edit-branch-office/div/div[2]/div/div[2]/div[3]/div/input'
        find_elements(self.driver,select_option6 )
        time.sleep(2)
      
       

        # salir de popup

         

        select_exit = '/html/body/ngb-modal-window/div/div/app-edit-branch-office/div/div[1]/button'
        find_elements(self.driver,select_exit )
        time.sleep(5)
      
      
        # ingresar a la solapa centro de distribucion 

        enter_tab_distribution = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/ul/li[2]/a'
        find_elements(self.driver,enter_tab_distribution )
        time.sleep(2)

        title_tab = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[2]/app-deposits/app-responsive-table/div/div/table/thead/tr/th[2]"
        value_expected = "Centro de Distribución"
        validate_text(self.driver,title_tab, value_expected  )

        title_deposits = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[2]/app-deposits/app-responsive-table/div/div/table/thead/tr/th[1]"
        value_expected = "Depósito"
        validate_text(self.driver, title_deposits, value_expected  )

        deposits_name = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[2]/app-deposits/app-responsive-table/div/div/table/tbody/tr[1]/td[1]/div/span"
        value_expected = "Deposito Angelica - Bancchio"
        validate_text(self.driver,deposits_name, value_expected  )

        select_option7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[2]/app-deposits/app-responsive-table/div/div/table/tbody/tr[1]/td[2]/div/div/app-switch/div/input'
        find_elements(self.driver,select_option7 )
        time.sleep(2)

        select_option8 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[2]/app-deposits/app-responsive-table/div/div/table/tbody/tr[2]/td[2]/div/div/app-switch/div/input'
        find_elements(self.driver,select_option8 )
        time.sleep(2)

        select_option9 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[2]/app-deposits/app-responsive-table/div/div/table/tbody/tr[3]/td[2]/div/div/app-switch/div/input'
        find_elements(self.driver,select_option9 )
        time.sleep(2)

        select_option10 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[2]/app-deposits/app-responsive-table/div/div/table/tbody/tr[1]/td[2]/div/div/app-switch/div/input'
        find_elements(self.driver,select_option10 )
        time.sleep(2)

        select_option11 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[2]/app-deposits/app-responsive-table/div/div/table/tbody/tr[2]/td[2]/div/div/app-switch/div/input'
        find_elements(self.driver,select_option11 )
        time.sleep(2)

        select_option12 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/div/div[2]/app-deposits/app-responsive-table/div/div/table/tbody/tr[3]/td[2]/div/div/app-switch/div/input'
        find_elements(self.driver,select_option12 )
        time.sleep(2)
      
        enter_tab_branch_offices = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-branch-offices/div/ul/li[1]/a'
        find_elements(self.driver,enter_tab_branch_offices )
        time.sleep(2)


        print("Test finalizado con éxito")


       

    
    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(config_Sucursales)
  runner = xmlrunner.XMLTestRunner(output='reportconfi_config_Sucursales')
  runner.run(test_suite)