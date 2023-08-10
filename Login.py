from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(username, password):
    driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")  # Configura el driver de Selenium (en este caso, Chrome)
    driver.get("https://pwa-portal-qa.silohub.ag/login")  # Abre la página de inicio de sesión

    # Encuentra los campos de usuario y contraseña y envía los datos
    driver.find_element(By.ID, "email").send_keys("admingd@silohub.ag")
    driver.find_element(By.ID, "password").send_keys("G@viglio123")

    # Envía el formulario de inicio de sesión
    driver.find_element(By.XPATH, "/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button").click()
    time.sleep(2)
   
      ## seleccionar el tenant 
    driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[2]/div/div/img").click()
    time.sleep(2)
    
    
    # Verifica si el inicio de sesión fue exitoso
    
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div/div/div/app-home/app-balances/div[1]/div[1]/div')))

    is_visible = element.is_displayed()

    if is_visible:
        print("Inicio de sesión exitoso")
        return True
        
    else:
         print("Inicio de sesión fallido")
         return False

def prueba_estres_login(username, password, num_repeticiones):
    exito = 0
    fallido = 0

    for _ in range(num_repeticiones):
         if login(username, password):
            exito += 1
    else:
            fallido += 1

    print("Prueba de estrés finalizada.")
    print(f"Intentos exitosos: {exito}")
    print(f"Intentos fallidos: {fallido}")

# Llama a la función prueba_estres_login con los parámetros deseados
prueba_estres_login("admingd@silohub.ag", "G@viglio123", 10)  # Realiza 10 intentos de inicio de sesión