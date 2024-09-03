
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


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