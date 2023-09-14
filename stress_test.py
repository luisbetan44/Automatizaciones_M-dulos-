import time
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Define tu función de prueba de Selenium
def run_test():
    driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://pwa-portal-staging.silohub.ag/login")

    username = driver.find_element_by_id("email")
    username.send_keys("luis@silohub.ag")
    username.send_keys(Keys.ENTER)
    time.sleep(3)

    passwordUser = driver.find_element_by_id("password")
    passwordUser.send_keys("Bet$714656")
    passwordUser.send_keys(Keys.ENTER)
    time.sleep(3)

    insertButton = driver.find_element_by_xpath("/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button")
    insertButton.send_keys(Keys.ENTER)
    time.sleep(3)

    # ... Continúa con el resto de tu prueba

    ## ingresa la tenant

    select_tenat = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[8]/div/div/img")
    select_tenat.click()
    time.sleep(35)

   # ingresar al menú de cuentas 

    
    
    driver.quit()

# Define la cantidad de repeticiones
num_repetitions = 1

# Ejecuta las pruebas en paralelo
with concurrent.futures.ThreadPoolExecutor(max_workers=num_repetitions) as executor:
    futures = [executor.submit(run_test) for _ in range(num_repetitions)]

# Espera a que todas las pruebas finalicen
concurrent.futures.wait(futures)

print("Pruebas de estrés completadas")