import datetime
import time
import random
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException,StaleElementReferenceException, InvalidSelectorException
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains




def find_elements(driver, xpath):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        select_nex_button.click()
        
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")

def find_elements_css_selector(driver, css_selector):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        select_nex_button.click()
        

        # Devolver el elemento encontrado
        return select_nex_button
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")
        return None


def find_elements_id(driver, id):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, id))
        )
        select_nex_button.click()
        
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")

def find_elements_name(driver, class_name):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, class_name))
        )
        select_nex_button.click()
        
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")

def find_elements_link_text(driver, link_text):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, link_text))
        )
        select_nex_button.click()
        
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")


def find_elements_located(driver, xpath):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        select_nex_button.click()
        
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")


def find_elements_cleam(driver, xpath):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        select_nex_button.clear
        
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es limpiar.")

def click_clear_and_send_keys_xpath(driver, xpath, new_amount):
    try:
        # Esperar hasta que el elemento sea clickeable
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

        # Hacer clic en el campo para activarlo
        element.click()

        # Limpiar la cantidad
        element.clear()

        # Enviar la nueva cantidad
        element.send_keys(new_amount)

        print(f"Clic realizado, cantidad limpiada y nuevo valor '{new_amount}' ingresado con éxito!")

    except StaleElementReferenceException:
        print(f"Elemento obsoleto. Volviendo a buscar el elemento y reintentar...")
        click_clear_and_send_keys_xpath(driver, xpath, new_amount)

    except TimeoutException:
        print(f"Tiempo de espera agotado. El elemento '{xpath}' no está presente o no es clickeable.")

def click_clear_and_send_keys_selector(driver, css_selector, new_amount):
    try:
        # Esperar hasta que el elemento sea clickeable
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )

        # Hacer clic en el campo para activarlo
        element.click()

        # Limpiar la cantidad
        element.clear()

        # Enviar la nueva cantidad
        element.send_keys(new_amount)

        print(f"Clic realizado, cantidad limpiada y nuevo valor '{new_amount}' ingresado con éxito!")

    except StaleElementReferenceException:
        print(f"Elemento obsoleto. Volviendo a buscar el elemento y reintentar...")
        click_clear_and_send_keys_xpath(driver, css_selector, new_amount)

    except TimeoutException:
        print(f"Tiempo de espera agotado. El elemento '{css_selector}' no está presente o no es clickeable.")




def wait_and_click(driver, xpath):
    try:
        # Esperar a que el elemento sea visible
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        # Hacer clic una vez que el elemento sea visible
        element.click()
        
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está visible o no es clickeable.")



def find_and_click_element_with_style_ID(driver, id):
    try:
        # Esperar a que el elemento sea visible
        element_to_click = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, id))
        )

        # Hacer visible el elemento utilizando JavaScript
        driver.execute_script("arguments[0].style.display = 'block';", element_to_click)

        # Hacer clic en el elemento
        element_to_click.click()

        
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es visible o clickeable.")

def find_and_click_element_with_style(driver, xpath):
    try:
        # Esperar a que el elemento sea visible
        element_to_click = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

        # Hacer visible el elemento utilizando JavaScript
        driver.execute_script("arguments[0].style.display = 'block';", element_to_click)

        # Hacer clic en el elemento
        element_to_click.click()

        
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es visible o clickeable.")

def send_display_element_id(driver, id, input_data):
    try:
        # Desplazarse hasta el elemento
        input_element = driver.find_element_by_id(id)
        driver.execute_script("arguments[0].scrollIntoView(true);", input_element)

        # Esperar a que el elemento sea clickeable
        input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, id))
        )

        # Si hay datos para ingresar, establecer el valor
        # Limpiar el input
        input_element.clear()  # Limpiar el input antes de ingresar datos
        input_element.send_keys(input_data)  # Ingresar los datos

        
    except TimeoutException:
        print("Tiempo de espera agotado. El input no está presente o no es clickeable.")

def send_display_element_xpaht(driver, xpaht, input_data):
    try:
        # Desplazarse hasta el elemento
        input_element = driver.find_element_by_id(xpaht)
        driver.execute_script("arguments[0].scrollIntoView(true);", input_element)

        # Esperar a que el elemento sea clickeable
        input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpaht))
        )

        # Si hay datos para ingresar, establecer el valor
        # Limpiar el input
        input_element.clear()  # Limpiar el input antes de ingresar datos
        input_element.send_keys(input_data)  # Ingresar los datos

        
    except TimeoutException:
        print("Tiempo de espera agotado. El input no está presente o no es clickeable.")


def display_and_do_click(driver, xpath):
    try:
        # Esperar a que el elemento esté presente en la página
        elemento = driver.find_element(By.XPATH, xpath)
        
        # Desplazar el elemento al área visible utilizando JavaScript
        driver.execute_script("arguments[0].scrollIntoView(true);", elemento)
        
        # Hacer clic en el elemento
        elemento.click()
        
        return True  # Indica que se pudo realizar el desplazamiento y clic correctamente
    except Exception as e:
        print("Error al desplazar y hacer clic:", e)
        return False




def find_and_send_element(driver, xpath, input_data=None):
    try:
        # Esperar a que el elemento sea clickeable
        select_next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

        # Si hay datos para ingresar, encontrar el input y establecer el valor
        if input_data is not None:
            input_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath))  # Corregir aquí
            )
            input_element.clear()  # Limpiar el input
            input_element.send_keys(input_data)  # Ingresar los datos

        # Hacer clic en el elemento encontrado
        select_next_button.click()
        print("¡Elemento encontrado y enviado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")

def find_send_element_id(driver, id, input_data=None):
    try:
        # Esperar a que el elemento sea clickeable
        input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, id))
        )

        # Si hay datos para ingresar, establecer el valor
        if input_data is not None:
            input_element.clear()  # Limpiar el input
            input_element.send_keys(input_data)  # Ingresar los datos

        print("¡Input encontrado y enviado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El input no está presente o no es clickeable.")

def find_send_element(driver, xpaht, input_data=None):
    try:
        # Esperar a que el elemento sea clickeable
        input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpaht))
        )

        # Si hay datos para ingresar, establecer el valor
        if input_data is not None:
            input_element.clear()  # Limpiar el input
            input_element.send_keys(input_data)  # Ingresar los datos

        print("¡Input encontrado y enviado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El input no está presente o no es clickeable.")


def send_element(driver, xpath, input_data):
    try:
        # Esperar a que el elemento sea clickeable
        input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

        # Si hay datos para ingresar, establecer el valor
        # Limpiar el input
        input_element.send_keys(input_data)  # Ingresar los datos

        print("¡Input encontrado y enviado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El input no está presente o no es clickeable.")

def send_element_xpaht(driver, xpath, input_data):
    try:
        # Esperar a que el elemento sea clickeable
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

        # Si hay datos para ingresar, establecer el valor
        # Limpiar el input
        input_element.send_keys(input_data)  # Ingresar los datos

        print("¡Input encontrado y enviado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El input no está presente o no es clickeable.")

def send_element_id(driver, id, input_data):
    try:
        # Esperar a que el elemento sea clickeable
        input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, id))
        )

        # Si hay datos para ingresar, establecer el valor
        # Limpiar el input
        input_element.send_keys(input_data)  # Ingresar los datos

        print("¡Input encontrado y enviado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El input no está presente o no es clickeable.")

def find_send_element_selector(driver, css_selector, input_data=None):
    try:
        # Esperar a que el elemento sea clickeable
        input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )

        # Si hay datos para ingresar, establecer el valor
        if input_data is not None:
            input_element.clear()  # Limpiar el input
            input_element.send_keys(input_data)  # Ingresar los datos

        print("¡Input encontrado y enviado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El input no está presente o no es clickeable.")



def find_and_click_element(driver, xpath, clicks=1):
    try:
        # Esperar a que el elemento sea clickeable
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

        # Hacer clic en el elemento la cantidad de veces especificada
        for _ in range(clicks):
            element.click()
        
        print(f"¡Elemento encontrado y clickeado {clicks} veces con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")


def find_and_click_element_selector(driver, css_selector, clicks=1):
    try:
        # Esperar a que el elemento sea clickeable
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )

        # Hacer clic en el elemento la cantidad de veces especificada
        for _ in range(clicks):
            element.click()
        
        print(f"¡Elemento encontrado y clickeado {clicks} veces con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")


def find_duo_xpath_element(driver, xpath1, xpath2):
    
    element = None
    
    # Intenta encontrar el primer elemento por XPath
    try:
        element = element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath1))
        )
        print("Elemento encontrado usando el primer XPath")
    except NoSuchElementException:
        print("Primer XPath no encontrado, intentando el segundo XPath")
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath2))
        )
            print("Elemento encontrado usando el segundo XPath")
        except NoSuchElementException:
            print("Segundo XPath tampoco encontrado")
    
    # Haz clic en el elemento si fue encontrado
    if element:
        element.click()
        return True
    return False



def click_checkbox(driver, checkbox_id):
    try:
        # Espera hasta que el checkbox sea clickeable
        checkbox_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, checkbox_id))
        )

        # Hacer clic en el checkbox
        checkbox_element.click()

        print(f"Checkbox con ID '{checkbox_id}' seleccionado con éxito!")

    except TimeoutException:
        print(f"Tiempo de espera agotado. El checkbox con ID '{checkbox_id}' no está presente o no es clickeable.")


def click_checkbox_xpaht(driver, checkbox_xpaht):
    try:
        # Espera hasta que el checkbox sea clickeable
        checkbox_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, checkbox_xpaht))
        )

        # Hacer clic en el checkbox
        checkbox_element.click()

        print(f"Checkbox con XPAHT '{checkbox_xpaht}' seleccionado con éxito!")

    except TimeoutException:
        print(f"Tiempo de espera agotado. El checkbox con XPAHT '{checkbox_xpaht}' no está presente o no es clickeable.")

def click_radioButton_xpaht(driver, checkbox_xpaht):
    try:
        # Espera hasta que el checkbox sea clickeable
        xpaht_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, checkbox_xpaht))
        )

        # Hacer clic en el checkbox
        xpaht_element.click()

        print(f"El elemento con xpaht '{checkbox_xpaht}' seleccionado con éxito!")

    except TimeoutException:
        print(f"Tiempo de espera agotado. El elemento con xpaht '{checkbox_xpaht}' no está presente o no es clickeable.")




# Otra función útil si deseas manipular la visibilidad de un elemento antes de interactuar con él
def make_visible(driver, xpath):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        driver.execute_script("arguments[0].style.display = 'block';", elemento)
    except TimeoutException:
        print(f"Tiempo de espera agotado. El elemento no está presente o no es visible.")


def make_send_visible_id(driver, id, new_amount ):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, id))
        )
        driver.execute_script("arguments[0].style.display = 'block';", elemento)
        try:
            # Esperar hasta que el elemento esté nuevamente presente después de desplazarse
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, id))
            )
        except TimeoutException:
            print(f"Tiempo de espera agotado. El elemento '{id}' no está presente después de desplazarse.")

        # Limpiar la cantidad
        element.clear()

        # Enviar la nueva cantidad
        element.send_keys(new_amount)

        print(f"Elemento desplazado, cantidad limpiada y nuevo valor '{new_amount}' ingresado con éxito!")

    except TimeoutException:
        print(f"Tiempo de espera agotado. El elemento '{id}' no está presente o no es visible.")
    except StaleElementReferenceException:
        print(f"Elemento obsoleto después de desplazarse. Intentando recuperarlo y reintentar...")
        displace_element_clear_send_keys(driver, id, new_amount)


def displace_element(driver, xpath):
    try:

        search_input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
# Desplazarse al elemento
        driver.execute_script("arguments[0].scrollIntoView();", search_input_element)
 
# Ahora puedes interactuar con el elemento
        search_input_element.click()
    except TimeoutException:
        print(f"Tiempo de espera agotado. El elemento no está presente o no es visible.")


def displace_element_clear_send_keys(driver, xpath, new_amount):
    try:
        # Esperar hasta que el elemento sea visible
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

        # Desplazarse al elemento
        driver.execute_script("arguments[0].scrollIntoView();", element)

        try:
            # Esperar hasta que el elemento esté nuevamente presente después de desplazarse
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except TimeoutException:
            print(f"Tiempo de espera agotado. El elemento '{xpath}' no está presente después de desplazarse.")

        # Limpiar la cantidad
        element.clear()

        # Enviar la nueva cantidad
        element.send_keys(new_amount)

        print(f"Elemento desplazado, cantidad limpiada y nuevo valor '{new_amount}' ingresado con éxito!")

    except TimeoutException:
        print(f"Tiempo de espera agotado. El elemento '{xpath}' no está presente o no es visible.")
    except StaleElementReferenceException:
        print(f"Elemento obsoleto después de desplazarse. Intentando recuperarlo y reintentar...")
        displace_element_clear_send_keys(driver, xpath, new_amount)



def displace_element_clear_send_keys_selector(driver, css_selector, new_amount):
    try:
        # Esperar hasta que el elemento sea visible
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
        )

        # Desplazarse al elemento
        driver.execute_script("arguments[0].scrollIntoView();", element)

        try:
            # Esperar hasta que el elemento esté nuevamente presente después de desplazarse
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
            )
        except TimeoutException:
            print(f"Tiempo de espera agotado. El elemento '{css_selector}' no está presente después de desplazarse.")

        # Limpiar la cantidad
        element.clear()

        # Enviar la nueva cantidad
        element.send_keys(new_amount)

        print(f"Elemento desplazado, cantidad limpiada y nuevo valor '{new_amount}' ingresado con éxito!")

    except TimeoutException:
        print(f"Tiempo de espera agotado. El elemento '{css_selector}' no está presente o no es visible.")
    except StaleElementReferenceException:
        print(f"Elemento obsoleto después de desplazarse. Intentando recuperarlo y reintentar...")
        displace_element_clear_send_keys_selector(driver, css_selector, new_amount)
    except InvalidSelectorException:
        print(f"Selector CSS '{css_selector}' no es válido.")


def displace_element_clear_send_keys_id(driver, id, new_amount):
    try:
        # Esperar hasta que el elemento sea visible
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, id))
        )

        # Desplazarse al elemento
        driver.execute_script("arguments[0].scrollIntoView();", element)

        try:
            # Esperar hasta que el elemento esté nuevamente presente después de desplazarse
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, id))
            )
        except TimeoutException:
            print(f"Tiempo de espera agotado. El elemento '{id}' no está presente después de desplazarse.")

        # Limpiar la cantidad
        element.clear()

        # Enviar la nueva cantidad
        element.send_keys(new_amount)

        print(f"Elemento desplazado, cantidad limpiada y nuevo valor '{new_amount}' ingresado con éxito!")

    except TimeoutException:
        print(f"Tiempo de espera agotado. El elemento '{id}' no está presente o no es visible.")
    except StaleElementReferenceException:
        print(f"Elemento obsoleto después de desplazarse. Intentando recuperarlo y reintentar...")
        displace_element_clear_send_keys_selector(driver, id, new_amount)
    except InvalidSelectorException:
        print(f"Selector CSS '{id}' no es válido.")

def displace_validate_element(driver, xpath, valor_esperado ):
    try:

        search_input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
# Desplazarse al elemento
        driver.execute_script("arguments[0].scrollIntoView();", search_input_element)
 

        valor = search_input_element.text
        if valor == valor_esperado:
            print(f"El texto encontrado es  {valor_esperado}")
        else:
            print(f"El texto no fue encontrado {valor_esperado}")
    except TimeoutException:
        print(f"Tiempo de espera agotado. El elemento no está presente o no es visible.")





def search_and_select_option(driver, xpath_search_input, xpath_search_result, value_to_search):
    try:
        # Esperar hasta que el campo de búsqueda sea clickeable
        search_input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_search_input))
        )

        # Limpiar el campo de búsqueda antes de realizar la búsqueda
        search_input_element.clear()

        # Ingresar el valor a buscar en el campo de búsqueda
        search_input_element.send_keys(value_to_search)

        # Esperar a que aparezcan las opciones de búsqueda después de ingresar el valor
        search_result_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_search_result))
        )

        # Hacer clic en la opción de búsqueda deseada
        search_result_element.click()

        print(f"¡Valor '{value_to_search}' ingresado y opción seleccionada con éxito!")

    except TimeoutException:
        print("Tiempo de espera agotado. El campo de búsqueda, las opciones de búsqueda, o ambos, no están presentes o no son clickeables.")



def search_for_selector_option(driver, selector_search_input, selector_search_result, value_to_search, send_input_element):
    try:
        # Esperar hasta que el campo de búsqueda sea clickeable
        search_input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector_search_input))
        )
        
        search_input_element.click()
        
        send_input_element.send_keys(value_to_search)
        time.sleep(1)

        # Esperar a que aparezcan las opciones de búsqueda después de ingresar el valor
        search_result_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector_search_result))
        )

        # Hacer clic en la opción de búsqueda deseada
        search_result_element.click()

        print(f"¡Valor '{value_to_search}' ingresado y opción seleccionada con éxito!")

    except TimeoutException:
        print("Tiempo de espera agotado. El campo de búsqueda, las opciones de búsqueda, o ambos, no están presentes o no son clickeables.")








def clear_and_send_keys(driver, xpath_field, value_to_send):
    try:
        # Esperar hasta que el campo sea clickeable
        field_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_field))
        )

        # Limpiar el campo antes de enviar las teclas
        field_element.clear()

        # Enviar las teclas al campo
        field_element.send_keys(value_to_send)

        print(f"Campo limpiado y valor '{value_to_send}' ingresado con éxito!")

    except StaleElementReferenceException:
        # Si se detecta una excepción de elemento obsoleto, intentar recuperar el elemento
        print("Elemento obsoleto, intentando recuperarlo y reintentar...")
        field_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_field))
        )
        field_element.clear()
        field_element.send_keys(value_to_send)

        print(f"Campo limpiado y valor '{value_to_send}' ingresado con éxito después de recuperación!")

    except TimeoutException:
        print(f"Tiempo de espera agotado. El campo '{xpath_field}' no está presente o no es clickeable.")


def select_and_set_payment_condition(driver, main_field_xpath, subfield_xpath, checkbox_xpath, payment_option):
    try:
        # Seleccionar el campo principal
        main_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, main_field_xpath))
        )
        main_field.click()

        # Esperar a que aparezca el subcampo después de hacer clic en el campo principal
        subfield_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, subfield_xpath))
        )

        # Limpiar el subcampo antes de ingresar las condiciones de pago
        subfield_element.clear()

        # Esperar a que el campo de búsqueda esté listo antes de ingresar las condiciones de pago
        WebDriverWait(driver, 10).until(
            EC.staleness_of(subfield_element)
        )

        # Ingresar las condiciones de pago en el subcampo
        subfield_element.send_keys(payment_option)

        # Esperar a que aparezcan todas las opciones después de ingresar las condiciones de pago
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, f"{subfield_xpath}/opciones"))
        )

        # Marcar el checkbox correspondiente a la opción "30 días"
        checkbox_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, checkbox_xpath))
        )
        checkbox_element.click()

        print(f"Condiciones de pago '{payment_option}' ingresadas y opción '30 días' seleccionada con éxito!")

    except TimeoutException:
        print(f"Tiempo de espera agotado. No se pudo realizar la selección para '{payment_option}'.")


def search_and_select_producer(driver, xpath_search_input, xpath_search_results, account_number):
    try:
        # Encontrar el campo de búsqueda por XPath
        search_input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_search_input))
        )

        # Limpiar el campo de búsqueda antes de realizar la búsqueda
        search_input_element.clear()

        # Ingresar el número de cuenta en el campo de búsqueda
        search_input_element.send_keys(account_number)

        # Esperar a que aparezcan las opciones de búsqueda después de ingresar el valor
        search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath_search_results))
        )
 
        # Seleccionar la primera opción (puedes ajustar esto según tus necesidades)
        if search_results:
            search_results[0].click()
            print(f"Número de cuenta '{account_number}' ingresado y opción seleccionada con éxito!")
        else:
            print(f"No se encontraron opciones para el número de cuenta '{account_number}'.")

    except TimeoutException:
        print("Tiempo de espera agotado. El campo de búsqueda, las opciones de búsqueda, o ambos, no están presentes o no son clickeables.")

def select_option_dropdown(driver, xpath_search_input, xpath_search_result, value_to_search):
    try:
        # Esperar hasta que el campo de búsqueda sea clickeable
        search_input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_search_input))
        )

        
        # Ingresar el valor a buscar en el campo de búsqueda
        search_input_element.send_keys(value_to_search)

        # Esperar a que aparezcan las opciones de búsqueda después de ingresar el valor
        search_result_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_search_result))
        )

        # Hacer clic en la opción de búsqueda deseada
        search_result_element.click()

        print(f"¡Valor '{value_to_search}' ingresado y opción seleccionada con éxito!")

    except TimeoutException:
        print("Tiempo de espera agotado. El campo de búsqueda, las opciones de búsqueda, o ambos, no están presentes o no son clickeables.")

def select_option_dropdown_css_selector(driver, selector_search_input, selector_search_result, value_to_search):
    try:
        # Esperar hasta que el campo de búsqueda sea clickeable
        search_input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector_search_input))
        )

        
        # Ingresar el valor a buscar en el campo de búsqueda
        search_input_element.send_keys(value_to_search)

        # Esperar a que aparezcan las opciones de búsqueda después de ingresar el valor
        search_result_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector_search_result))
        )

        # Hacer clic en la opción de búsqueda deseada
        search_result_element.click()

        print(f"¡Valor '{value_to_search}' ingresado y opción seleccionada con éxito!")

    except TimeoutException:
        print("Tiempo de espera agotado. El campo de búsqueda, las opciones de búsqueda, o ambos, no están presentes o no son clickeables.")


def search_and_select_account(driver, account_number):
    try:
        # Encontrar el elemento de entrada por ID
        input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#current-account-applied > app-contract-form > div.container-form.bg-white > form > div > div:nth-child(1) > div.f-size-12 > div:nth-child(3) > div.col-8 > div > app-customer-searcher > ng-select > div > div > div.ng-input > input[type=text]"))
        )
        
        # Limpiar el campo de búsqueda antes de realizar la búsqueda
        input_element.clear()

        # Ingresar el número de cuenta en el campo de búsqueda
        input_element.send_keys(account_number)

        # Encontrar el elemento para hacer clic por CSS selector
        element_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[3]/div[2]/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"))
        )

        # Hacer clic en el elemento deseado
        element_to_click.click()

        print(f"Número de cuenta '{account_number}' ingresado y opción seleccionada con éxito!")

    except TimeoutException:
        print("Tiempo de espera agotado. El campo de búsqueda, las opciones de búsqueda, o ambos, no están presentes o no son clickeables.")

def upload_file_after_click(driver, xpath_chevron, xpath_upload_field, file_path):
    try:
        # Esperar hasta que el chevron sea clickeable
        chevron_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_chevron))
        )

        # Hacer clic en el chevron para desplegar el campo de carga de archivo
        chevron_element.click()

        # Encontrar el campo de carga de archivo después de desplegar el chevron
        upload_input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_upload_field))
        )

        # Adjuntar el archivo al campo de carga de archivo
        upload_input_element.send_keys(file_path)

        print(f"Archivo '{file_path}' cargado con éxito después de hacer clic en el chevron!")

    except TimeoutException:
        print("Tiempo de espera agotado. El chevron o el campo de carga de archivo no están presentes o no son clickeables.")
    except ElementClickInterceptedException:
        print("El clic en el chevron fue interceptado por otro elemento en la página.")


def upload_file_after_click_selector(driver, selector_chevron, selector_upload_field, file_path):
    try:
        # Esperar hasta que el chevron sea clickeable
        chevron_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector_chevron))
        )

        # Hacer clic en el chevron para desplegar el campo de carga de archivo
        chevron_element.click()

        # Encontrar el campo de carga de archivo después de desplegar el chevron
        upload_input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector_upload_field))
        )

        # Adjuntar el archivo al campo de carga de archivo
        upload_input_element.send_keys(file_path)

        print(f"Archivo '{file_path}' cargado con éxito después de hacer clic en el chevron!")

    except TimeoutException:
        print("Tiempo de espera agotado. El chevron o el campo de carga de archivo no están presentes o no son clickeables.")
    except ElementClickInterceptedException:
        print("El clic en el chevron fue interceptado por otro elemento en la página.")




def select_option_click(driver, xpath_chevron, xpath_upload_field ):
    try:
        # Esperar hasta que el chevron sea clickeable
        xpath_chevron = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_chevron))
        )

        # Hacer clic en el chevron para desplegar el campo de carga de archivo
        xpath_chevron.click()

        # Encontrar el campo de carga de archivo después de desplegar el chevron
        upload_input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_upload_field))
        )

        # Adjuntar el archivo al campo de carga de archivo
        upload_input_element.click()


    except TimeoutException:
        print("Tiempo de espera agotado. El chevron no están presentes o no son clickeables.")
    except ElementClickInterceptedException:
        print("El clic en el chevron fue interceptado por otro elemento en la página.")

def locate_option_click(driver, xpath_chevron, xpath_upload_field ):
    try:
        # Esperar hasta que el chevron sea clickeable
        xpath_chevron = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_chevron))
        )

        # Hacer clic en el chevron para desplegar el campo de carga de archivo
        xpath_chevron.click()

        # Encontrar el campo de carga de archivo después de desplegar el chevron
        upload_input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_upload_field))
        )

        # Adjuntar el archivo al campo de carga de archivo
        upload_input_element.click()

        print( "La opcion fue seleccionada en el dropdown con exito  ")

    except TimeoutException:
        print("Tiempo de espera agotado. El chevron no están presentes o no son clickeables.")
    except ElementClickInterceptedException:
        print("El clic en el chevron fue interceptado por otro elemento en la página.")

def validate_text(driver, xpath, valor_esperado):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        valor = elemento.text
        if valor == valor_esperado:
            print(f"El texto encontrado es  {valor_esperado}")
        else:
            print(f"El texto no fue encontrado {valor_esperado}")
    except TimeoutException:
        print(f"Tiempo de espera agotado. El texto por xpaht no está presente.")

def validate_values_text(driver, xpath, valores_esperados):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        valor = elemento.text
        if valor in valores_esperados:
            print(f"El texto encontrado es uno de los valores esperados: {valor}")
        else:
            print(f"El texto '{valor}' no fue encontrado en los valores esperados: {valores_esperados}")
    except TimeoutException:
        print(f"Tiempo de espera agotado. El elemento con xpath '{xpath}' no está presente.")

        

def validate_text_css_selector(driver, css_selector, valor_esperado):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        valor = elemento.text
        if valor == valor_esperado:
            print(f"El texto encontrado es  {valor_esperado}")
        else:
            print(f"El texto no fue encontrado {valor_esperado}")
    except TimeoutException:
        print(f"Tiempo de espera agotado. el texto por selector no está presente.")

def validate_text_by_text(driver, expected_text):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_text}')]"))
        )
        valor = elemento.text
        if valor == expected_text:
            print(f"El texto encontrado es  {expected_text}")
        else:
            print(f"El texto no fue encontrado {expected_text}")
    except TimeoutException:
        print(f"Tiempo de espera agotado. El texto por texto no está presente.")

def validate_text_by_strt(driver, expected_text):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_text}')]"))
        )
        valor = elemento.text
        if isinstance(valor, str):
            if valor == expected_text:
                print(f"El texto encontrado es  {expected_text}")
            else:
                print(f"El texto encontrado '{valor}' no coincide con el esperado '{expected_text}'")
        else:
            print(f"El valor encontrado no es un string: {valor}")
    except TimeoutException:
        print(f"Tiempo de espera agotado. El texto por texto no está presente.")

def validate_strt(driver, expected_text, xpaht):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpaht))
        )
        valor = elemento.text
        if isinstance(valor, str):
            if valor == expected_text:
                print(f"El texto encontrado es  {expected_text}")
            else:
                print(f"El texto encontrado '{valor}' no coincide con el esperado '{expected_text}'")
        else:
            print(f"El valor encontrado no es un string: {valor}")
    except TimeoutException:
        print(f"Tiempo de espera agotado. El texto por texto no está presente.")

def validate_strt_selector(driver, expected_text, css_aelector):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_aelector))
        )
        valor = elemento.text
        if isinstance(valor, str):
            if valor == expected_text:
                print(f"El texto encontrado es  {expected_text}")
            else:
                print(f"El texto encontrado '{valor}' no coincide con el esperado '{expected_text}'")
        else:
            print(f"El valor encontrado no es un string: {valor}")
    except TimeoutException:
        print(f"Tiempo de espera agotado. El texto por texto no está presente.")


def validate_chart_value(driver, html_content, valor_esperado):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        data_value = soup.find('path')['data:value']
        if data_value == valor_esperado:
            print(f"El valor del gráfico es {valor_esperado}.")
        else:
            print(f"El valor del gráfico es {data_value}, pero se esperaba {valor_esperado}.")
    except TimeoutException:
        print("Tiempo de espera agotado.")
    


def validate_chain_text_xpaht(driver, xpath, expected_texts):
    try:
        # Espera explícita para asegurarse de que el elemento esté presente y visible
        text_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        
        actual_text = text_element.text.strip()

        # Verificar si el texto obtenido es un substring de alguno de los textos esperados
        for expected_text in expected_texts:
            if expected_text in actual_text:
                print(f"El texto es visible para el usuario: '{actual_text}'")
                return  # Sale del bucle si encuentra una coincidencia

        # Si no se encontró ninguna coincidencia
        print(f"El texto no coincide con los valores esperados. Texto actual: '{actual_text}'")

    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no se ha vuelto visible.")
    except NoSuchElementException:
        print("No se encontró el elemento con el xpath especificado.")




def validate_image_xpaht(driver, xpath, urls_esperadas):
    imagen = driver.find_element(By.XPATH, xpath)
    url_imagen_obtenida = imagen.get_attribute('src')

    if url_imagen_obtenida in urls_esperadas:
        print("La imagen es visible para el usuario. URL:", url_imagen_obtenida)
    else:
        print("La imagen no es visible para el usuario. URL:", url_imagen_obtenida)

def validate_image_css_selector(driver, css_selector, urls_esperadas):
    imagen = driver.find_element(By.CSS_SELECTOR, css_selector)
    url_imagen_obtenida = imagen.get_attribute('src')

    if url_imagen_obtenida in urls_esperadas:
        print("La imagen es visible para el usuario. URL:", url_imagen_obtenida)
    else:
        print("La imagen no es visible para el usuario. URL:", url_imagen_obtenida)

def validate_character_numeric_element(driver, xpath):
    elemento = driver.find_element(By.XPATH, xpath)
    valor = elemento.text

    if re.search(r'\d', valor):
        print(f'El valor es un carácter numérico. Valor: {valor}')
    else:
        print(f'El valor no es un carácter numérico. Valor: {valor}')

def validate_character_numeric_element_selector(driver, css_selector):
    elemento = driver.find_element(By.CSS_SELECTOR, css_selector)
    valor = elemento.text

    if re.search(r'\d', valor):
        print(f'El valor es un carácter numérico. Valor: {valor}')
    else:
        print(f'El valor no es un carácter numérico. Valor: {valor}')

def validate_text_visible(driver, xpath, text_expected):
    element = driver.find_element(By.XPATH, xpath)
    is_visible = element.is_displayed()

    if is_visible:
        print("El texto es visible para el usuario")
    else:
        print("El texto no es visible para el usuario")

    text_obtained = element.text
    assert text_obtained == text_expected

    if text_obtained:
        print("El texto fue validado correctamente:", text_obtained)
    else:
        print("No se pudo validar el texto")
    
def validate_text_visible_selector(driver, css_selector, text_expected):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    is_visible = element.is_displayed()

    if is_visible:
        print("El texto es visible para el usuario")
    else:
        print("El texto no es visible para el usuario")

    text_obtained = element.text
    assert text_obtained == text_expected

    if text_obtained:
        print("El texto fue validado correctamente:", text_obtained)
    else:
        print("No se pudo validar el texto")

def extract_percentage_values(driver, xpaht):
    try:
        # Esperar a que el gráfico esté presente en la página
        elemento_grafico = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpaht))
        )
        # Obtener el HTML del gráfico
        html_grafico = elemento_grafico.get_attribute('outerHTML')
        
        # Parsear el HTML con BeautifulSoup
        soup = BeautifulSoup(html_grafico, 'html.parser')
        
        # Encontrar los elementos <path> dentro del gráfico
        path_elements = soup.find_all('path')
        
        # Inicializar un diccionario para almacenar los valores de porcentajes
        valores_porcentaje = {}
        
        # Iterar sobre los elementos y extraer los valores de porcentajes
        for path_element in path_elements:
            color = path_element.get('fill')
            valor = path_element.get('data:value')
            if color and valor:  # Asegurar que ambos color y valor existan
                valores_porcentaje[color] = valor
                print(f"Color: {color}, Valor: {valor}")
        
        return valores_porcentaje
        
    except TimeoutException:
        print("El elemento del gráfico no se encontró en el tiempo especificado.")
        return {}
    
def extract_percentage_values(driver, grafico_selector, valores_selector, tiempo_espera=10):
    try:
        # Localizar el elemento del gráfico interactivo
        grafico_interactivo = WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, grafico_selector))
        )

        # Simular mover el mouse sobre el gráfico para activar la visualización de los valores
        actions = ActionChains(driver)
        actions.move_to_element(grafico_interactivo).perform()

        # Esperar un momento para que el gráfico muestre los valores de porcentaje
        # Puedes ajustar el tiempo de espera según tus necesidades
        WebDriverWait(driver, tiempo_espera).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, valores_selector))
        )

        # Una vez que los valores de porcentaje se han activado, extraer la información del gráfico
        valores_de_porcentaje = driver.find_element(By.CSS_SELECTOR, valores_selector).text

        print("Valores de porcentaje del gráfico:", valores_de_porcentaje)

        return valores_de_porcentaje
    except Exception as e:
        print("Error al extraer los valores de porcentaje del gráfico:", e)
        return None
    
def simulate_hover(driver, id):
    # Encontrar el elemento del gráfico interactivo
    graph_element = driver.find_element(By.ID, id)
    
    # Ejecutar un script JavaScript para simular el evento de pasar el mouse
    driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('mouseover', { bubbles: true }))", graph_element)
    
    
def search_for_select_account(driver, account_number, xpaht, send_element, select_element ):
    try:
        # Encontrar el elemento de entrada y escribir el número de cuenta

        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpaht ))
        )
        select_element.click()

        send_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpaht ))
        )
        send_element.send_keys(account_number)

        send_element.send_keys(Keys.ENTER)

        # Encontrar y hacer clic en el elemento deseado
        select_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpaht ))
        )
        select_input.click()

        print(f"¡Cuenta encontrada y seleccionada {account_number}  con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")     
    

def search_and_displace_account(driver, account_number, located_element, xpaht):
    try:

        located_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(( By.XPATH, xpaht)))
        
        located_element.click()
        
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(( By.XPATH, xpaht)))
        
        driver.execute_script("arguments[0].style.display = 'block';", input_element)
        
        input_element.send_keys(account_number)
        time.sleep(2)

        

        print(f"¡Cuenta encontrada y seleccionada {account_number}  con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")     
    

def search_and_displace_element(driver, account_number, located_element, xpaht):
    try:

        located_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(( By.XPATH, xpaht)))
        
        located_element.click()
        
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(( By.XPATH, xpaht)))
        
        driver.execute_script("arguments[0].style.display = 'block';", input_element)
        
        input_element.click()
        time.sleep(2)

        

        print(f"¡Cuenta encontrada y seleccionada {account_number}  con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")  

def click_icon_delete(driver, css_selector):
    while True:
        try:
            icono_borrar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
            driver.execute_script("arguments[0].style.display = 'block';", icono_borrar)
             
            icono_borrar.click()
            print("Se hizo clic en un icono de borrar.")
        except TimeoutException:
            print("No se encontraron más movimientos para borrar.")
            break
        except NoSuchElementException:
            print("No se encontró el icono de borrar.")
            break

def click_icon_delete_xpaht(driver, xpaht):
    while True:
        try:
            icono_borrar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpaht)))
            driver.execute_script("arguments[0].style.display = 'block';", icono_borrar)
             
            icono_borrar.click()
            print("Se hizo clic en un icono de borrar.")
        except TimeoutException:
            print("No se encontraron más movimientos para borrar.")
            break
        except NoSuchElementException:
            print("No se encontró el icono de borrar.")
            break

def click_icon_delete_id(driver, id):
    while True:
        try:
            icono_borrar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, id)))
            driver.execute_script("arguments[0].style.display = 'block';", icono_borrar)
             
            icono_borrar.click()
            print("Se hizo clic en un icono de borrar.")
        except TimeoutException:
            print("No se encontraron más movimientos para borrar.")
            break
        except NoSuchElementException:
            print("No se encontró el icono de borrar.")
            break


def seleccionar_ultimo_icono(driver, selector_iconos):
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, selector_iconos)))
    iconos = driver.find_elements(By.XPATH, selector_iconos)
    
    ultimo_icono = iconos[-1]
    ultimo_icono.click()

def ingresar_rango_fecha(xpath_calendario, driver):
    # Obtener la fecha de hoy y la de ayer
    hoy = datetime.date.today()
    fecha_hoy = hoy.strftime("%d")

    

    # Encontrar el elemento de entrada de fecha por su XPath
    calendario_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(( By.XPATH, xpath_calendario)))
    driver.execute_script("arguments[0].style.display = 'block';",  calendario_element)
    

    calendario_element.click()

    # Ingresar las fechas directamente en el campo de entrada
    

     # Encontrar el elemento que corresponde a la fecha actual y hacer clic en él
    fecha_actual_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//td[@aria-label='Today']")))
    fecha_actual_element.click()


def delete_element(driver, xpaht):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,xpaht)))
        element.click()

        element.send_keys(Keys.CONTROL, "a")

        element.send_keys(Keys.BACKSPACE)

        
    except TimeoutException:
            print("No se encontraron los datos para borrar.")



def hop_element(driver, xpath):
    try:
        # Espera hasta que los elementos sean clickeables
        elementos = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )

        # Haz clic en el segundo elemento si existe
        if len(elementos) >= 2:
            segundo_elemento = elementos[1]
            segundo_elemento.click()
            print("¡Elemento encontrado y clickeado con éxito!")
        else:
            print("No se encontraron suficientes elementos.")
    except TimeoutException:
        print("No se encontraron elementos o no fueron clickeables dentro del tiempo de espera.")

def calendar_todate(driver, input_xpath, popup_xpath):
    input_fecha = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, input_xpath))
    )
    input_fecha.click()

    # Esperar a que aparezca el pop-up del calendario
    popup_calendario = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, popup_xpath))
    )

    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")

    # Buscar el elemento de la fecha actual en el pop-up del calendario
    try:
        fecha_elemento = popup_calendario.find_element(By.XPATH, f"//span[contains(@class, 'flatpickr-day') and @aria-current='date']")
        # Darle doble clic a la fecha
        ActionChains(driver).move_to_element(fecha_elemento).double_click().perform()
    except:
        print("La fecha actual no está disponible en el calendario.")

def calendar_todate_retro(driver, input_xpath, popup_xpath, chevron_xpath, popup_xpath2, clicks=6):
    input_fecha = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, input_xpath))
    )
    input_fecha.click()

    # Esperar a que aparezca el pop-up del calendario
    popup_calendario = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, popup_xpath))
    )

    # Obtener el día actual
    dia_actual = datetime.datetime.now().day

    # Buscar el elemento de la fecha actual en el pop-up del calendario
    try:
        fecha_elemento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[contains(@class, 'flatpickr-day') and @aria-current='date']"))
        )
        # Darle clic a la fecha para seleccionarla
        ActionChains(driver).move_to_element(fecha_elemento).click().perform()
    except Exception as e:
        print("La fecha actual no está disponible en el calendario.")
        print(e)
        return

    # Hacer clic 6 veces en el botón de retroceder mes
    for i in range(clicks):
        try:
            back_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, chevron_xpath))
            )
            back_button.click()
            time.sleep(1)  # Esperar un segundo para que el calendario se actualice
        except Exception as e:
            print(f"No se pudo hacer clic en el botón de retroceso en el intento {i+1}.")
            print(e)
            return

    # Esperar a que el calendario se actualice después de retroceder meses
    popup_calendario2 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, popup_xpath2))
    )

    # Seleccionar el día correspondiente al número del día actual después de retroceder meses
    try:
        dia_elemento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[contains(@class, 'flatpickr-day') and text()='{dia_actual}']"))
        )
        dia_elemento.click()
    except Exception as e:
        print(f"El día {dia_actual} no está disponible en el calendario después de retroceder meses.")
        print(e)

def  select_previous_day(driver, popup_xpath):
    # Esperar a que aparezca el pop-up del calendario
    popup_calendario = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, popup_xpath))
    )

    # Obtener la fecha de ayer en el formato que coincide con el calendario
    fecha_ayer = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%d-%m-%Y")

    # Buscar el elemento del día de ayer en el pop-up del calendario y hacer clic
    try:
        fecha_elemento_ayer = popup_calendario.find_element(By.XPATH, f"//span[contains(@class, 'flatpickr-day') and @aria-label='{fecha_ayer}']")
        fecha_elemento_ayer.click()
        print("Día de ayer seleccionado con éxito.")
    except:
        print("La fecha de ayer no está disponible en el calendario.")

def generate_and_send_number(driver, xpath_input):
   
    # Genera un número aleatorio
    random_number = random.randint(1000, 9999)
    
    # Encuentra el campo de entrada y envía el número
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath_input))
    )
    input_field.clear()  # Limpia el campo de entrada
    input_field.send_keys(str(random_number))  # Envía el número como una cadena de texto
    
    # Espera un breve momento para permitir que la página procese la entrada
    time.sleep(1)

    return random_number

def generate_and_number_sequential(driver, xpath_input):
    
    numero_secuencial = [0]  # Inicializa el contador dentro de una lista

    def obtener_numero_secuencial():
        numero_secuencial[0] += 1
        return numero_secuencial[0]

    # Encuentra el campo de entrada y envía el número secuencial
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath_input))
    )
    input_field.clear()  # Limpia el campo de entrada
    input_field.send_keys(str(obtener_numero_secuencial()))  # Envía el número secuencial como una cadena de texto
    
    # Espera un breve momento para permitir que la página procese la entrada
    time.sleep(1)

    return numero_secuencial[0]



def verify_and_click(driver, number_generate, xpath_number):
    try:
        # Encuentra el número generado
        number_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[text()='{number_generate}']"))
        )
        
        # Imprime el texto del número obtenido
        print(f"Número obtenido desde la función: {number_element.text}")
        
        # Encuentra el contenedor padre del número
        parent_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_number))
        )
        
        # Encuentra todos los elementos svg con el id 'Grupo_10473' dentro del contenedor padre
        elements = parent_element.find_elements(By.XPATH, ".//svg[@id='Grupo_10473']")
        
        # Selecciona el segundo elemento (índice 1, ya que Python usa indexación basada en cero)
        target_element = elements[1]
        
        # Verifica si el elemento está presente y es clickeable
        clickable_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(target_element)
        )
        
        # Haz clic en el elemento
        clickable_element.click()
        
        # Imprime una confirmación
        print("El elemento en la posición siguiente ha sido clickeado.")
        
        return clickable_element

    except Exception as e:
        print(f"Ha ocurrido un error al obtener o clicar en el elemento: {e}")
        return None
    
