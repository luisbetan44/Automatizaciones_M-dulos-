from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time







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
    time.sleep(3)

    # Ejecuta la prueba de estrés llamando a la función run_test varias veces
num_repeticiones = 10

for i in range(num_repeticiones):
    print(f"Ejecutando prueba de estrés #{i + 1}")
    run_test()

# Cierra el navegador al finalizar


driver.quit()