import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_and_click_element_selector, find_elements, find_elements_css_selector, validate_character_numeric_element, validate_chart_value, validate_text
from loginhelper import LoginHelper
from startSession import StartSession


class Metricas(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_metricas(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")


        

        ##seleccionar menu de metricas 
        select_menu_metrics = "#navbar-nav > li:nth-child(9) > a > span"
        find_elements_css_selector(self.driver, select_menu_metrics)
    

        ## validar el titulo 
        title_page = '/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span'
        text_expected = "MÉTRICAS"
        validate_text(self.driver, title_page, text_expected  )
 
        ## seleccionar filtro 01/01/2024 al 15/03/2024

        select_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/div/div/app-date-picker/div/input[2]"
        find_elements(self.driver, select_filter)
     
        select_arrow_1 = "body > div > div.flatpickr-months > span.flatpickr-prev-month"
        clicks = 6
        find_and_click_element_selector(self.driver, select_arrow_1, clicks)
        time.sleep(2)

        select_date1 = "/html/body/div/div[2]/div/div[2]/div/span[1]"
        find_elements(self.driver, select_date1)

        select_arrow_2 = "body > div > div.flatpickr-months > span.flatpickr-next-month"
        clicks = 2
        find_and_click_element_selector(self.driver, select_arrow_2, clicks)
        time.sleep(2)
        
        select_date2 = "/html/body/div/div[2]/div/div[2]/div/span[19]"
        find_elements(self.driver, select_date2)


        
     ##validar los cuadrantes de la pantalla verificando los que vienen de la base de datos si son caracteres numericos 
        
        element1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[1]/app-metric-indicator/div/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element1  )
       
        titlle_value1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[1]/app-metric-indicator/div/div[2]/div[3]"
        value_expected1 = "Total Cuentas ERP"
        validate_text(self.driver, titlle_value1, value_expected1)
     
   
        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[2]/app-metric-indicator/div/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element2  )

        ##validar totalizadores  a vencer
        titlle_value2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[2]/app-metric-indicator/div/div[2]/div[3]"
        value_expected2 = "Total Cuentas Vinculadas"
        validate_text(self.driver, titlle_value2, value_expected2)

        element3 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[3]/app-metric-indicator/div/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element3  )
        
        titlle_value3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[3]/app-metric-indicator/div/div[2]/div[3]"
        value_expected3 = "Cuentas Pend. de Vincular"
        validate_text(self.driver,titlle_value3, value_expected3)

        
        element4 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[4]/app-metric-indicator/div/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element4  )

        titlle_value4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[4]/app-metric-indicator/div/div[2]/div[3]"
        value_expected4 = "Porc. Vinculado"
        validate_text(self.driver, titlle_value4, value_expected4)



       
         ## validar cuadrantes que vienen desde google analitycs
        
        element5 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[5]/app-metric-indicator-news-clients/app-metric-indicator/div/div[3]/div[2]'
        validate_character_numeric_element(self.driver, element5  )

        titlle_value5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[5]/app-metric-indicator-news-clients/app-metric-indicator/div/div[3]/div[3]"
        text_expected = "Productores Nuevos"
        validate_text(self.driver,titlle_value5 , text_expected)

        element6 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[6]/app-metric-indicator-total-logins/app-metric-indicator/div/div[3]/div[2]'
        validate_character_numeric_element(self.driver, element6  )

        titlle_value6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[6]/app-metric-indicator-total-logins/app-metric-indicator/div/div[3]/div[3]"
        text_expected = "Total Logins (Visitas)"
        validate_text(self.driver,titlle_value6 , text_expected)

        element7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[7]/app-metric-indicator-unique-logins/app-metric-indicator/div/div[3]/div[2]'
        validate_character_numeric_element(self.driver, element7  )

        titlle_value7 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[7]/app-metric-indicator-unique-logins/app-metric-indicator/div/div[3]/div[3]"
        text_expected = "Usuarios Logueados"
        validate_text(self.driver,titlle_value7 , text_expected)

        element8 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[8]/app-metric-indicator-session-avg/app-metric-indicator/div/div[3]/div[2]'
        validate_character_numeric_element(self.driver, element8  )

        titlle_value8 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[8]/app-metric-indicator-session-avg/app-metric-indicator/div/div[3]/div[3]"
        text_expected = "Tiempo Prom. Sesión"
        validate_text(self.driver,titlle_value8 , text_expected)

        # validar cuadrantes inferiores pantallas mas vistas 
        
        titlle_module1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[1]/app-metric-page-ranking/div/div[2]/div"
        text_expected = "Pantallas Más Visitadas"
        validate_text(self.driver,titlle_module1 , text_expected)

        titlle_value9 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[1]/app-metric-page-ranking/div/div[3]/div[1]/div[2]"
        text_expected = "Inicio"
        validate_text(self.driver,titlle_value9 , text_expected)

        element9 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[1]/app-metric-page-ranking/div/div[3]/div[1]/div[3]'
        validate_character_numeric_element(self.driver, element9  )

        titlle_value10 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[1]/app-metric-page-ranking/div/div[3]/div[2]/div[2]"
        text_expected = "Otros"
        validate_text(self.driver,titlle_value10 , text_expected)

        element10 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[1]/app-metric-page-ranking/div/div[3]/div[2]/div[3]'
        validate_character_numeric_element(self.driver, element10  )

        titlle_value11 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[1]/app-metric-page-ranking/div/div[3]/div[3]/div[2]"
        text_expected = "Granos"
        validate_text(self.driver,titlle_value11 , text_expected)

        element11 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[1]/app-metric-page-ranking/div/div[3]/div[3]/div[3]'
        validate_character_numeric_element(self.driver, element11  )

        titlle_value12 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[1]/app-metric-page-ranking/div/div[3]/div[4]/div[2]"
        text_expected = "Contratos"
        validate_text(self.driver,titlle_value12 , text_expected)

        element12 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[1]/app-metric-page-ranking/div/div[3]/div[4]/div[3]'
        validate_character_numeric_element(self.driver, element12  )

        titlle_value13 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[1]/app-metric-page-ranking/div/div[3]/div[5]/div[2]"
        text_expected = "Configuraciones"
        validate_text(self.driver,titlle_value13 , text_expected)

        element13 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[1]/app-metric-page-ranking/div/div[3]/div[5]/div[3]'
        validate_character_numeric_element(self.driver, element13  )
        

        # pantallas menos vistas 

        titlle_module2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[2]/app-metric-page-ranking/div/div[2]/div"
        text_expected = "Pantallas Menos Visitadas"
        validate_text(self.driver,titlle_module2 , text_expected)

        titlle_value14 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[2]/app-metric-page-ranking/div/div[3]/div[1]/div[2]"
        text_expected = "Ventas"
        validate_text(self.driver,titlle_value14 , text_expected)

        element14 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[2]/app-metric-page-ranking/div/div[3]/div[1]/div[3]'
        validate_character_numeric_element(self.driver, element14  )

        titlle_value15 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[2]/app-metric-page-ranking/div/div[3]/div[2]/div[2]"
        text_expected = "Comprobantes"
        validate_text(self.driver,titlle_value15 , text_expected)

        element15 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[2]/app-metric-page-ranking/div/div[3]/div[2]/div[3]'
        validate_character_numeric_element(self.driver, element15  )

        titlle_value16 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[2]/app-metric-page-ranking/div/div[3]/div[3]/div[2]"
        text_expected = "Entregas"
        validate_text(self.driver,titlle_value16 , text_expected)

        element16 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[2]/app-metric-page-ranking/div/div[3]/div[3]/div[3]'
        validate_character_numeric_element(self.driver, element16  )

        titlle_value17 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[2]/app-metric-page-ranking/div/div[3]/div[4]/div[2]"
        text_expected = "Cuenta Corriente"
        validate_text(self.driver,titlle_value17 , text_expected)

        element17 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[2]/app-metric-page-ranking/div/div[3]/div[4]/div[3]'
        validate_character_numeric_element(self.driver, element17  )

        titlle_value18 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[2]/app-metric-page-ranking/div/div[3]/div[5]/div[2]"
        text_expected = "Acceso a Terceros"
        validate_text(self.driver,titlle_value18 , text_expected)

        element18 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-ranking/div/div[2]/app-metric-page-ranking/div/div[3]/div[5]/div[3]'
        validate_character_numeric_element(self.driver, element18  )


       # Validar el grafico 
        
        graphic_desktop = '<path id="SvgjsPath1443" d="M 87.5 1.8292682926829258 A 73.17073170731707 73.17073170731707 0 1 1 71.04016675532694 3.7046294059584 L 81.27598838908095 48.04084386603974 A 27.668292682926833 27.668292682926833 0 1 0 87.5 47.33170731707317 L 87.5 1.8292682926829258 z" fill="rgba(2,99,255,1)" fill-opacity="1" stroke-opacity="1" stroke-linecap="butt" stroke-width="0" stroke-dasharray="0" class="apexcharts-pie-area apexcharts-donut-slice-0" index="0" j="0" selected="true" data:angle="347.58620689655174" data:startAngle="0" data:strokeWidth="0" data:value="56" data:pathOrig="M 87.5 5.829268292682926 A 69.17073170731707 69.17073170731707 0 1 1 72.63033735515945 7.446441561126676 L 81.55213494206377 47.97857662445067 A 27.668292682926833 27.668292682926833 0 1 0 87.5 47.33170731707317 L 87.5 5.829268292682926 z" data:pieClicked="true" filter="url(#SvgjsFilter1639)"></path>'
        text_expected = "56"
        validate_chart_value(self.driver, graphic_desktop, text_expected)

        graphic_mobile = '<path id="SvgjsPath1463" d="M 72.63033735515945 7.446441561126676 A 69.17073170731707 69.17073170731707 0 0 1 87.48792742991822 5.829269346213408 L 87.49517097196728 47.33170773848536 A 27.668292682926833 27.668292682926833 0 0 0 81.55213494206377 47.97857662445067 L 72.63033735515945 7.446441561126676 z" fill="rgba(255,119,35,1)" fill-opacity="1" stroke-opacity="1" stroke-linecap="butt" stroke-width="0" stroke-dasharray="0" class="apexcharts-pie-area apexcharts-donut-slice-1" index="0" j="1" data:angle="12.413793103448256" data:startAngle="347.58620689655174" data:strokeWidth="0" data:value="2" data:pathOrig="M 72.63033735515945 7.446441561126676 A 69.17073170731707 69.17073170731707 0 0 1 87.48792742991822 5.829269346213408 L 87.49517097196728 47.33170773848536 A 27.668292682926833 27.668292682926833 0 0 0 81.55213494206377 47.97857662445067 L 72.63033735515945 7.446441561126676 z" selected="true" filter="url(#SvgjsFilter1663)"></path>'
        text_expected = "2"
        validate_chart_value(self.driver, graphic_mobile, text_expected)

       
    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(Metricas)
  runner = xmlrunner.XMLTestRunner(output='reportMetricas')
  runner.run(test_suite)
        
   