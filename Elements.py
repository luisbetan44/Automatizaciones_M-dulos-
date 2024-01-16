from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re


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




# Otra función útil si deseas manipular la visibilidad de un elemento antes de interactuar con él
def make_visible(driver, xpath):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        driver.execute_script("arguments[0].style.display = 'block';", elemento)
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

def validate_chain_text_xpaht(driver, xpath, urls_esperadas):
    text = driver.find_element(By.XPATH, xpath)
    url_text_obtenida = text.get_attribute('src')

    if url_text_obtenida in urls_esperadas:
        print("La Cadena de texto es visible para el usuario. :", url_text_obtenida)
    else:
        print("La cadena de texto no es visible para el usuario. :", url_text_obtenida)



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