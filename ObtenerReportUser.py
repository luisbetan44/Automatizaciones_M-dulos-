import sys
import xml.etree.ElementTree as ET

def generate_html_report(xml_file, output_file):
    # Parsear el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Obtener información relevante del reporte
    test_name = root.find('testcase').attrib['name']
    time_taken = root.find('testcase').attrib['time']
    timestamp = root.find('testcase').attrib['timestamp']

    # Crear el contenido HTML del informe
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reporte de Pendientes por Facturar</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h2>Reporte de Pendientes por Facturar</h2>
        <p>Nombre del Test: {test_name}</p>
        <p>Tiempo tomado: {time_taken} segundos</p>
        <p>Fecha y hora de ejecución: {timestamp}</p>
        <table>
            <tr>
                <th>Nombre del Test</th>
                <th>Tiempo tomado</th>
                <th>Fecha y hora de ejecución</th>
            </tr>
            <tr>
                <td>{test_name}</td>
                <td>{time_taken} segundos</td>
                <td>{timestamp}</td>
            </tr>
        </table>
    </body>
    </html>
    """

    # Guardar el contenido HTML en el archivo de salida
    with open(output_file, 'w') as file:
        file.write(html_content)

    print("Se ha generado el reporte HTML correctamente.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python generate_report.py archivo.xml archivo_salida.html")
        sys.exit(1)
    
    xml_file = sys.argv[1]
    output_file = sys.argv[2]
    generate_html_report(xml_file, output_file)