from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



def find_element_by_id(driver, id):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id)))
    

def find_element_by_xpath(driver, xpath):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

def find_element_by_css_selector(driver, css_selector):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

