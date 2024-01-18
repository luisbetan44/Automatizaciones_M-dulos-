import random
from selenium.webdriver.common.by import By

def generar_dni(driver, input_xpath):
    dni = random.randint(10000000, 99999999)
    dni_verificado = str(dni) + str(calcular_digito_verificador(dni))
    
    campo_input = driver.find_element(By.XPATH, input_xpath)
    campo_input.clear()
    campo_input.send_keys(dni_verificado)

    # Imprimir el DNI generado en la consola
    print(f"Se generó y escribió el DNI verificado: {dni_verificado}")

    return dni_verificado

def calcular_digito_verificador(dni):
    tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
    return tabla[dni % 23]