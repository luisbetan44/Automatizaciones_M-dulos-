import time
from typing import KeysView
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException,StaleElementReferenceException, InvalidSelectorException
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys



def find_elements(driver, xpath):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        select_nex_button.click()
        print("¡Elemento encontrado y clickeado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")

def find_elements_css_selector(driver, css_selector):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        select_nex_button.click()
        print("¡Elemento encontrado y clickeado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")




def find_elements_id(driver, id):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, id))
        )
        select_nex_button.click()
        print("¡Elemento encontrado y clickeado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")

def find_elements_name(driver, class_name):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, class_name))
        )
        select_nex_button.click()
        print("¡Elemento encontrado y clickeado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es clickeable.")

def find_elements_cleam(driver, xpath):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        select_nex_button.clear
        print("¡Elemento encontrado y limpiado con éxito!")
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


def wait_and_click(driver, xpath):
    try:
        # Esperar a que el elemento sea visible
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        # Hacer clic una vez que el elemento sea visible
        element.click()
        print("¡Elemento visible y clickeado con éxito!")
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

        print("¡Elemento encontrado, hecho visible y clickeado con éxito!")
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

        print("¡Elemento encontrado, hecho visible y clickeado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El elemento no está presente o no es visible o clickeable.")



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

def find_send_element(driver, xpath, input_data=None):
    try:
        # Esperar a que el elemento sea clickeable
        input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
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
            EC.element_to_be_clickable((By.XPATH, checkbox_xpaht))
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





# Otra función útil si deseas manipular la visibilidad de un elemento antes de interactuar con él
def make_visible(driver, xpath):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        driver.execute_script("arguments[0].style.display = 'block';", elemento)
    except TimeoutException:
        print(f"Tiempo de espera agotado. El elemento no está presente o no es visible.")


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
            EC.element_to_be_clickable((By.XPATH, xpath_chevron))
        )

        # Hacer clic en el chevron para desplegar el campo de carga de archivo
        chevron_element.click()

        # Encontrar el campo de carga de archivo después de desplegar el chevron
        upload_input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_upload_field))
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

        print( "La opcion fue seleccionada con éxito después de hacer clic en el chevron!")

    except TimeoutException:
        print("Tiempo de espera agotado. El chevron no están presentes o no son clickeables.")
    except ElementClickInterceptedException:
        print("El clic en el chevron fue interceptado por otro elemento en la página.")


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
                print(f"La cadena de texto es visible para el usuario: '{actual_text}'")
                return  # Sale del bucle si encuentra una coincidencia

        # Si no se encontró ninguna coincidencia
        print(f"La cadena de texto no coincide con los valores esperados. Texto actual: '{actual_text}'")

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

def handle_system_dialog(driver, xpath):
    # Hacer clic en el botón/elemento que abre el diálogo del sistema
    driver.find_element(By.XPATH, xpath).click()

    # Esperar un breve momento para asegurar que el diálogo del sistema ha aparecido
    time.sleep(2)

    # Enfocar en el diálogo del sistema (dependiendo del sistema operativo, puede variar)
    # En este ejemplo, se usa TAB para navegar por los elementos del sistema operativo.
    driver.switch_to.active_element.send_keys(Keys.TAB)
    time.sleep(1)

    # Presionar la tecla ENTER para seleccionar la opción (puede variar según el sistema operativo)
    driver.switch_to.active_element.send_keys(KeysView.ENTER)

    # Puedes ajustar y agregar más interacciones según sea necesario.

