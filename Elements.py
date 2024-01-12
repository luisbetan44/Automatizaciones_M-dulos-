from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def find_elements(driver, xpath):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        select_nex_button.click()
        print("¡Botón encontrado y clickeado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El botón no está presente o no es clickeable.")

def find_elements_css_selector(driver, css_selector):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        select_nex_button.click()
        print("¡Botón encontrado y clickeado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El botón no está presente o no es clickeable.")

def find_elements_id(driver, id):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, id))
        )
        select_nex_button.click()
        print("¡Botón encontrado y clickeado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El botón no está presente o no es clickeable.")

def find_elements(driver, class_name):
    try:
        select_nex_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, class_name))
        )
        select_nex_button.click()
        print("¡Botón encontrado y clickeado con éxito!")
    except TimeoutException:
        print("Tiempo de espera agotado. El botón no está presente o no es clickeable.")




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



def validar_solapa(driver, xpath, valor_esperado):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        valor = elemento.text
        if valor == valor_esperado:
            print(f"Nos encontramos en la solapa {valor_esperado}")
        else:
            print(f"No estamos ubicados en la solapa {valor_esperado}")
    except TimeoutException:
        print(f"Tiempo de espera agotado. La solapa no está presente o no es clickeable.")

# Otra función útil si deseas manipular la visibilidad de un elemento antes de interactuar con él
def hacer_visible(driver, xpath):
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