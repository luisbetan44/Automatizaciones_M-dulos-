import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class CUITGenerator:
    @staticmethod
    def generate_random_cuit(driver, input_xpath):
        provincia = random.randint(1, 24)
        dni = random.randint(1000000, 99999999)
        verificador = random.randint(0, 9)
        cuit = '{}-{}-{}'.format(provincia, dni, verificador)

        input_element = driver.find_element(By.XPATH, input_xpath)

        input_element.clear()
        input_element.send_keys(cuit)
        input_element.send_keys(Keys.ENTER)

        return cuit

    @staticmethod
    def is_error_present(driver, css_selector):
        wait = WebDriverWait(driver, 5)

        try:
            error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            return False
        return True

    @staticmethod
    def insert_valid_cuit(driver, input_xpath, error_css_selector):
        cuit_valido = False

        while not cuit_valido:
            cuit = CUITGenerator.generate_random_cuit(driver, input_xpath)

           
         

            try:
                if not CUITGenerator.is_error_present(driver, error_css_selector):
                    cuit_valido = True
                else:
                    print("Error presente. Intentando con otro CUIT.")
            except StaleElementReferenceException:
                continue

        return cuit