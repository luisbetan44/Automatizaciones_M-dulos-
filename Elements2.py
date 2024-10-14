
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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