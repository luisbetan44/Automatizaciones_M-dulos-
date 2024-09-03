from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class StartSessionFirefox:
    def __init__(self):
        # Crea una instancia de FirefoxOptions
        firefox_options = Options()

        # Desactiva las notificaciones
        firefox_options.set_preference("dom.webnotifications.enabled", False)

        # Agrega la ruta del controlador de Firefox al PATH
        firefox_path = r"C:\geckodriver\geckodriver.exe"  # Reemplaza con la ruta correcta

        firefox_options.add_argument(f"executable_path={firefox_path}")

        # Crea una instancia del controlador de Firefox con FirefoxOptions
        self.driver = webdriver.Firefox(options=firefox_options)

        # Configuraciones adicionales
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://pwa-portal-staging.silohub.ag/login")

# Crear una instancia de la clase StartSession para iniciar sesión
##session = StartSessionFirefox()

# Acceder al controlador del navegador
##driver = session.driver