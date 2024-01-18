from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class StartSession:
    def __init__(self):
        # Crea una instancia de ChromeOptions
        chrome_options = Options()

        # Agrega la ruta del controlador de Chrome al PATH
        chrome_path = r"C:\driverchrome\chromedriver-win64\chromedriver.exe"

        # Establece la ruta del controlador en ChromeOptions
        chrome_options.add_argument(f"executable_path={chrome_path}")

        # Crea una instancia del controlador de Chrome con ChromeOptions
        self.driver = webdriver.Chrome(options=chrome_options)

        # Configuraciones adicionales
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://pwa-portal-staging.silohub.ag/login")