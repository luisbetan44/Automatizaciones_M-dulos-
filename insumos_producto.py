import unittest
import time
import xmlrunner
from Elements import displace_element,find_elements,find_elements_id, find_send_element, search_and_select_option, select_option_click, send_element, validate_text, validate_text_by_text
from LoginSample import LoginSample
from startSession import StartSession


class insumosProductos(unittest.TestCase):


    def    setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_supplies_products(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("comercialgd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()
        time.sleep(2)
        ## seleccionar menú de insumos 

        select_supplies = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[4]/a"
        displace_element(self.driver,select_supplies )
        time.sleep(3)

        select_menu_product = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[4]/div/ul/li[1]/a"
        find_elements(self.driver,select_menu_product )
        time.sleep(2)

        ## validar titulo de la pagina 

       
        title_page_product_obtained = "PRODUCTOS"
        validate_text_by_text(self.driver, title_page_product_obtained)

        ## agregar producto

        add_product = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[1]/input"
        send_product = "herbicida"
        find_send_element(self.driver, add_product, send_product )
        time.sleep(2)

        ## seleccionar condicion 

        select_condition = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[2]/app-supplies-price-list-selector/button"
        find_elements(self.driver,select_condition )
        
        
        xpath_search_input = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[2]/app-supplies-price-list-selector/ul/input"
        xpath_search_result = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[2]/app-supplies-price-list-selector/ul/div/div[10]/input"
        value_to_search = "30 días"
        search_and_select_option(self.driver, xpath_search_input, xpath_search_result, value_to_search)

        button_search = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[3]/button/div"
        find_elements(self.driver, button_search )
        time.sleep(3)

        ## seleccionar el segunfo de los productos del listado 
        
        select_price_product = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-product-price-list/div/app-supplies-product-price-list-item[2]/div/div/div/div[2]/button[2]/strong"
        find_elements(self.driver, select_price_product )
        time.sleep(3)

        ## agregar producto al carro 

        select_product_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-product-price-list/div/app-supplies-product-price-list-item[2]/div/div/app-supplies-product-price-list-item-price/div[2]/app-supplies-product-price-list-item-price-item/div/div[1]/input"
        find_elements(self.driver, select_product_list )
        time.sleep(3)

        add_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-product-price-list/div/app-supplies-product-price-list-item[2]/div/div/app-supplies-product-price-list-item-price/app-supplies-product-price-list-item-price-add-share-buttons/div/button[2]"
        find_elements(self.driver,  add_button )
        time.sleep(3)

        ## ingresar al carrito 

        select_car = "shipment"
        find_elements_id(self.driver,select_car )
        time.sleep(3)

        ## validar titulo pantalla 

        title_page_car = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/span"
        title_page_car_obtained = "Productos Seleccionados"
        validate_text(self.driver,title_page_car, title_page_car_obtained )

       ## validar descripcion del producto

        description_product = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/div/app-supplies-selected-products/app-supplies-selected-products-item/div/div/div/div[1]/div/div[2]/div/div[1]"
        description_product_expected = "Herbicida 2-4 DB 96% Rainwon x 20 lts RAINWON AGRO"
        validate_text(self.driver,description_product, description_product_expected )

        ## seleccionar cuenta 

        select_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[2]/app-supplies-customer-info/div/div[1]/div/div[2]/app-customer-searcher/ng-select/div/div/div[2]/input"
        send_account = "1023"
        find_send_element(self.driver, select_account, send_account )
       

        select_account_tenant = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[2]/app-supplies-customer-info/div/div[1]/div/div[2]/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[2]/span"
        find_elements(self.driver,  select_account_tenant)
        time.sleep(7)
        ## cambiar cantidad 

        inser_new_amount = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/div/app-supplies-selected-products/app-supplies-selected-products-item/div/div/app-supplies-selected-products-item-price-item/div/div[2]/div/div[2]/input"
        send_new_amount = "3"
        send_element(self.driver, inser_new_amount,  send_new_amount)
        time.sleep(2)
        ## insertar comentario


        insert_comentary = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[2]/app-supplies-customer-info/div/div[2]/div/textarea"
        send_comentary = "Test de prueba automatizada"
        find_send_element(self.driver, insert_comentary, send_comentary )

        ## hacer boton continuar

        continue_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[2]/app-supplies-customer-info/div/app-supplies-customer-info-share-continuous/div/div[2]/button"
        find_elements(self.driver, continue_button )
        ## seleccionar sucursal 

        
        select_branch = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/app-supplies-customer-info-branch-office/div/div/div/div[1]/select"
        select_option = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/app-supplies-customer-info-branch-office/div/div/div/div[1]/select/option[4]"
        select_option_click(self.driver, select_branch, select_option )


        create_order = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[2]/app-supplies-customer-info/div/app-supplies-customer-info-share-continuous/div/div[2]/button"
        find_elements(self.driver, create_order )

        ## confirmar la orden

        confirm_order = "/html/body/div/div/div[6]/button[3]"
        find_elements(self.driver, confirm_order )
        time.sleep(2)

        ## validar que la orden se creo con exito


        order_successful = "/html/body/div/div/h2"
        order_successful_obtained = "Tu orden fue enviada al sistema"
        validate_text(self.driver,order_successful, order_successful_obtained )

        ## seleccionar boton aceptar 

        accept_button = "/html/body/div/div/div[6]/button[3]"
        find_elements(self.driver, accept_button )
        time.sleep(2)


    def tearDown(self):
        self.driver.close()




if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(insumosProductos)
  runner = xmlrunner.XMLTestRunner(output='reportInsumosProductos')
  runner.run(test_suite)
        
   