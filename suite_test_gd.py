import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import xmlrunner
import unittest
from ConfISolicitudes import confi_Solicitudes
from ConfiClientes import confi_registro_cliente
from ConfigSucursales import config_Sucursales
from CtaContOperSecundaria import contrato_operSecundarias
from CtaCte_HistoApagar import cuenta_ctacte_histApagar
from CtaCte_HistoAvenver import cuenta_ctacte_histAvencer
from CtaCte_HistoVencido import cuenta_ctacte_histVencido
from CtaCtoDtalCertificados import detalle_cto_certificados
from CtaCtoDtalEntVta import detalle_ctro_entregaVentas
from CtaCtoDtalFijaciones import detalle_ctro_fijaciones
from CtaCtoDtalLiquidaciones import detalle_cto_liquidaciones
from ctacte_histoAcobrar import cuenta_ctacte_histAcobrar
from Cuentacontrato import contrato_tenant
from Dashboar import dashboard_granos
from EntregasAplicadas import cta_entregasAplicadas
from EntregasPendApli import entregas_pend_Aplicadas
from GranosContratos import granos_contratos
from Home import HomeTenant
from HomeEntRecientes import HomeEntRecientesTenant
from finanzasPagos import finanzaspagos
from indicaInsumosHome import IndicaInsumosHome
from MisIntenciones import mis_intenciones
from Precio_Fijacion import precio_granos_fijaciones
from Profile_User import Perfil_Usuario
from RegistroUsuario import TestRegistroUsuario 
from ReportCompPenFact import reportPendFacturar
from ReportEntreVentas import reportEntregasVentas
from ReportMerFacturada import reportMerFacturada
from Ventas import cuenta_ventas
from Onboarding import Onboarding_test_tenant
from comproContratos import comprobanteContrato
from comproCtaCte import comprobantectacte
from comproEntregas import comprobanteEntregas
from comproVentas import comprobanteVentas
from ctacte_ApliApagar import cta_cte_apliApagar
from ctacte_ApliAvencer import cta_cte_apliAvencer
from ctacte_ApliVencido import cta_cte_apliVencido
from ctacte_apliAcobrar import cta_cte_apliAcobrar
from ctacte_aplicada15diasV import cta_cte_aplicada_15_Vencer
from ctacte_histórica import cuenta_ctacte_historica
from insumos_producto import insumosProductos
from logistOperPrimarias import logistOperPrimarias
from reportInsuRetirar import ReportinsumosPendRetirar


def ejecutar_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRegistroUsuario))
    test_suite.addTest(unittest.makeSuite(Perfil_Usuario))
    test_suite.addTest(unittest.makeSuite(HomeTenant))
    test_suite.addTest(unittest.makeSuite(HomeEntRecientesTenant))
    test_suite.addTest(unittest.makeSuite(IndicaInsumosHome))
    test_suite.addTest(unittest.makeSuite(granos_contratos))
    test_suite.addTest(unittest.makeSuite(insumosProductos))
    test_suite.addTest(unittest.makeSuite(precio_granos_fijaciones))
    test_suite.addTest(unittest.makeSuite(dashboard_granos))
    test_suite.addTest(unittest.makeSuite(mis_intenciones))
    test_suite.addTest(unittest.makeSuite(contrato_tenant))
    test_suite.addTest(unittest.makeSuite(detalle_ctro_entregaVentas))
    test_suite.addTest(unittest.makeSuite(detalle_ctro_fijaciones))
    test_suite.addTest(unittest.makeSuite(detalle_cto_certificados))
    test_suite.addTest(unittest.makeSuite(detalle_cto_liquidaciones))
    test_suite.addTest(unittest.makeSuite(contrato_operSecundarias))
    test_suite.addTest(unittest.makeSuite(cta_entregasAplicadas))
    test_suite.addTest(unittest.makeSuite(entregas_pend_Aplicadas))
    test_suite.addTest(unittest.makeSuite(cuenta_ventas))
    test_suite.addTest(unittest.makeSuite(cta_cte_aplicada_15_Vencer))
    test_suite.addTest(unittest.makeSuite(cta_cte_apliAcobrar))
    test_suite.addTest(unittest.makeSuite(cta_cte_apliApagar))
    test_suite.addTest(unittest.makeSuite(cta_cte_apliAvencer))
    test_suite.addTest(unittest.makeSuite(cta_cte_apliVencido))
    test_suite.addTest(unittest.makeSuite(cuenta_ctacte_historica))
    test_suite.addTest(unittest.makeSuite(cuenta_ctacte_histApagar))
    test_suite.addTest(unittest.makeSuite(cuenta_ctacte_histAcobrar))
    test_suite.addTest(unittest.makeSuite(cuenta_ctacte_histAvencer))
    test_suite.addTest(unittest.makeSuite(cuenta_ctacte_histVencido))
    test_suite.addTest(unittest.makeSuite(comprobantectacte))
    test_suite.addTest(unittest.makeSuite(comprobanteContrato))
    test_suite.addTest(unittest.makeSuite(comprobanteEntregas))
    
    test_suite.addTest(unittest.makeSuite(comprobanteVentas))
    test_suite.addTest(unittest.makeSuite(reportPendFacturar))
    test_suite.addTest(unittest.makeSuite(reportEntregasVentas))
    test_suite.addTest(unittest.makeSuite(ReportinsumosPendRetirar))
    test_suite.addTest(unittest.makeSuite(reportMerFacturada))
    test_suite.addTest(unittest.makeSuite(finanzaspagos))
    test_suite.addTest(unittest.makeSuite(logistOperPrimarias))
    test_suite.addTest(unittest.makeSuite(confi_registro_cliente))
    test_suite.addTest(unittest.makeSuite(config_Sucursales))
    test_suite.addTest(unittest.makeSuite(confi_Solicitudes))
    test_suite.addTest(unittest.makeSuite(Onboarding_test_tenant))
    
    # Configuración para generar informes XML solo de los tests fallidos
    output_folder = 'reporte_suite'
    os.makedirs(output_folder, exist_ok=True)

    runner = xmlrunner.XMLTestRunner(output=output_folder, outsuffix='failed', failfast=False)
    result = runner.run(test_suite)
    
    # Filtrar solo los fallos
    failed_tests = []
    for test, err in result.failures + result.errors:
        failed_tests.append(test)

    return failed_tests

def generar_informe_fallidos(failed_tests, carpeta_prueba):
    informe_fallidos = os.path.join(carpeta_prueba, 'informe_fallidos.txt')
    with open(informe_fallidos, 'w') as f:
        for test in failed_tests:
            f.write(f'{test.id()}\n')
    return informe_fallidos

def enviar_informe_por_correo(ruta_informe_fallidos):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cuerpo_correo = f"Resultados de las pruebas ejecutadas el {fecha_hora}:\n\nAdjunto encontrará el informe de los tests fallidos."
    
    from_email = "luis.tacourt@gmail.com"
    to_email = "luis@silohub.ag"
    subject = "Informe de Pruebas Automatizadas - Tests Fallidos"

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "luis.tacourt@gmail.com"
    smtp_password = "wrimlphlmonftprz"

    mensaje = MIMEMultipart()
    mensaje.attach(MIMEText(cuerpo_correo, 'plain'))
    mensaje['From'] = from_email
    mensaje['To'] = to_email
    mensaje['Subject'] = subject

    with open(ruta_informe_fallidos, "rb") as archivo_informe:
        adjunto = MIMEApplication(archivo_informe.read(), _subtype="txt")
        adjunto.add_header("Content-Disposition", f"attachment; filename={os.path.basename(ruta_informe_fallidos)}")
        mensaje.attach(adjunto)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, mensaje.as_string())

if __name__ == "__main__":
    failed_tests = ejecutar_suite()
    if failed_tests:
        ruta_informe_fallidos = generar_informe_fallidos(failed_tests, "reporte_suite")
        enviar_informe_por_correo(ruta_informe_fallidos)
    else:
        print("No hubo tests fallidos.") 