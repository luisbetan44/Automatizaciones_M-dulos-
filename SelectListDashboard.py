from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.DEBUG)

def verify_text_and_click(driver, xpath1, xpath2, xpath3, xpath4, xpath5, xpath6, xpath7, xpath8, xpath9, xpath10, xpath11):
    try:
        logging.debug("Waiting for element_list...")
        element_list = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath1))
        )
        element_list.click()
        logging.debug("element_list clicked")

        try:
            logging.debug("Checking status1...")
            status1 = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath2))
            ).text
            logging.debug(f"status1: {status1}")

            if status1 == "Pendiente":
                logging.debug("status1 is 'Pendiente'")
                otro_elemento2 = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, xpath3))
                )
                otro_elemento2.click()
                logging.debug("otro_elemento2 clicked")

                otro_elemento3 = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, xpath4))
                )
                otro_elemento3.click()
                logging.debug("otro_elemento3 clicked")
                return
        except Exception as e:
            logging.debug(f"status1 exception occurred: {e}")

        try:
            logging.debug("Checking status2...")
            status2 = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath5))
            ).text
            logging.debug(f"status2: {status2}")

            if status2 == "Pendiente":
                logging.debug("status2 is 'Pendiente'")
                otro_elemento4 = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, xpath6))
                )
                otro_elemento4.click()
                logging.debug("otro_elemento4 clicked")

                otro_elemento5 = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, xpath7))
                )
                otro_elemento5.click()
                logging.debug("otro_elemento5 clicked")
                return
        except Exception as e:
            logging.debug(f"status2 exception occurred: {e}")

        try:
            logging.debug("Checking status3...")
            status3 = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath8))
            ).text
            logging.debug(f"status3: {status3}")

            if status3 == "Pendiente":
                logging.debug("status3 is 'Pendiente'")
                otro_elemento6 = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, xpath9))
                )
                otro_elemento6.click()
                logging.debug("otro_elemento6 clicked")

                otro_elemento7 = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, xpath10))
                )
                otro_elemento7.click()
                logging.debug("otro_elemento7 clicked")
                return
        except Exception as e:
            logging.debug(f"status3 exception occurred: {e}")

        # Si ninguno de los estados es "Pendiente", se ejecuta esto
        logging.debug("Clicking final element...")
        otro_elemento9 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath11))
        )
        otro_elemento9.click()
        logging.debug("El elemento de salida fue clicado.")
    except Exception as e:
        logging.error(f"An exception occurred: {e}")