
from datetime import datetime
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


## validar la fecha actual

def verify_todate(driver, xpath):
    # Obtener la fecha actual en formato 'YYYY-MM-DD'
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    
    try:
        # Encontrar el elemento de la fecha en la página
        elemento_fecha = driver.find_element(By.XPATH, xpath)
        fecha_elemento = elemento_fecha.text.strip()
        
        # Comparar la fecha del elemento con la fecha actual
        if fecha_elemento == fecha_actual:
            print(f"La fecha encontrada es la actual: {fecha_elemento}")
        else:
            print(f"Fecha encontrada: {fecha_elemento}")
    
    except NoSuchElementException:
        print(f"No se encontró el elemento con el XPath: {xpath}")

def validate_character_string_element(driver, xpath):
    elemento = driver.find_element(By.XPATH, xpath)
    valor = elemento.text.strip()  # Elimina posibles espacios en blanco al inicio o al final

    if valor.isalpha():
        print(f'El valor es un carácter alfabético. Valor: {valor}')
    else:
        print(f'El valor es un string. Valor: {valor}')

def download_pdf(driver, download_PDF_xpath, timeout=10):
    
    wait = WebDriverWait(driver, timeout)

    try:
        # Esperar hasta que el enlace de descargar PDF sea clicable
        pdf_element = wait.until(EC.element_to_be_clickable((By.XPATH, download_PDF_xpath)))
        
        # Ejecutar clic mediante JavaScript
        driver.execute_script("arguments[0].click();", pdf_element)
    except Exception as e:
         print(f"Error al encontrar o hacer clic en el elemento: {e}")


def calendar_todate_retro_selector(driver, input_selector, popup_selector, chevron_selector, popup_selector2, clicks=6):
    input_fecha = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, input_selector))
    )
    input_fecha.click()

    # Esperar a que aparezca el pop-up del calendario
    popup_calendario = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, popup_selector))
    )

    # Obtener el día actual
    dia_actual = datetime.datetime.now().day

    # Buscar el elemento de la fecha actual en el pop-up del calendario
    try:
        fecha_elemento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.flatpickr-calendar.rangeMode span.flatpickr-day.today"))
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
                EC.element_to_be_clickable((By.CSS_SELECTOR, chevron_selector))
            )
            back_button.click()
            time.sleep(1)  # Esperar un segundo para que el calendario se actualice
        except Exception as e:
            print(f"No se pudo hacer clic en el botón de retroceso en el intento {i+1}.")
            print(e)
            return

    # Esperar a que el calendario se actualice después de retroceder meses
    popup_calendario2 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, popup_selector2))
    )

    # Seleccionar el día correspondiente al número del día actual después de retroceder meses
    try:
        dia_elemento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"//span[contains(@class, 'flatpickr-day') and text()='{dia_actual}']"))
        )
        dia_elemento.click()
    except Exception as e:
        print(f"El día {dia_actual} no está disponible en el calendario después de retroceder meses.")
        print(e)
