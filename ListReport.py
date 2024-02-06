

import os
import xml.etree.ElementTree as ET
from datetime import datetime

def register_validation_results(validations, folder_path, file_prefix):
    # Verificar si la carpeta especificada existe, si no existe, crearla
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generar un nombre de archivo único basado en la marca de tiempo actual
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{file_prefix}_{timestamp}.xml"
    file_path = os.path.join(folder_path, file_name)
    
    # Crear el elemento raíz del XML
    validations_element = ET.Element("validations")

    # Agregar cada validación como subelemento de validations
    for validation in validations:
        validation_element = ET.SubElement(validations_element, "validation")
        validation_element.text = validation
        br_element = ET.SubElement(validations_element, "br")
        br_element.text = "\n"  # Agregar un salto de línea

    # Crear el árbol XML y escribirlo en el archivo
    tree = ET.ElementTree(validations_element)
    tree.write(file_path, xml_declaration=True, encoding='utf-8')

    print(f'Validation results registered successfully. File saved as: {file_path}')

    # Devolver la ruta del archivo XML generado
    return file_path

#
