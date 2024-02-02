import requests
from bs4 import BeautifulSoup
import random
import string

class EmailGenerator:
    @staticmethod
    def generate_email():
        # URL del servicio de correo temporal
        yopmail_url = "https://yopmail.com/es/wm"
        response = requests.get(yopmail_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        email_element = soup.find('input', {'id': 'login'})
        
        if email_element:
            random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            return f"{email_element['value']}_{random_string}@yopmail.com"
        else:
            raise Exception("No se pudo obtener el correo electrónico temporal de Yopmail.")