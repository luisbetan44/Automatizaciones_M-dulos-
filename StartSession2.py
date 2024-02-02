from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class StartSession:
    def __init__(self, url):
        chrome_options = Options()
        chrome_path = r"C:\driverchrome\chromedriver-win64\chromedriver.exe"
        chrome_options.add_argument(f"executable_path={chrome_path}")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(url)

    def close_session(self):
        self.driver.quit()