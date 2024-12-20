import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import unittest
import xmlrunner

from ComproContractV2 import comprobanteContratoV2
from ComproCtaCteV2 import comprobanteCtaCteV2
from ComproEntregasV2 import comprobanteEntregasV2
from ComproVentasV2 import comprobanteVentasV2
from ConfISolicitudes import confi_Solicitudes
from ConfiClientes import confi_registro_cliente
from ConfigSucursales import config_Sucursales
from CtaCtoDtaEntVent2 import detalle_ctro_entregaVentasV2
from CtaCtoDtaFijaV2 import detalle_ctro_fijacionesV2
from CtaCtoDtaLiquiV2 import detalle_cto_liquidacionesV2
from CtaCtoDtalCertificado2 import detalle_cto_certificadosV2
from Dashboar import dashboard_granos
from EntVentaV2 import EntregasVentasV2
from EntregasApliV2 import entregas_AplicadasV2
from EntregasFactV2 import entregas_facturadosV2
from EntregasPendApliV2 import entregas_pend_AplicadasV2
from EntregasPendFactV2 import entregas_Pend_FacturarV2
from GranosContratos import granos_contratos
from HomeEntVentReciV2 import HomeEntVentRecientesV2
from HomeResuNegoV2 import HomeResNegocioTenantV2
from HomeSaldoCuetHoyV2 import HomeSaldoCuentHoyV2
from MisIntenciones import mis_intenciones
from Onboarding import Onboarding_test_tenant
from Precio_Fijacion import precio_granos_fijaciones
from Profile_User import Perfil_Usuario
from RegistroUsuario import TestRegistroUsuario
from ReportMerFactV2 import cuenta_mercaderia_facturarV2
from ReportMerRemitV2 import cuenta_mercaderia_remitidaV2
from ReportPendFactV2 import cuenta_pend_facturarV2
from ReportPendRetiV2 import cuenta_pend_retirarV2
from ResuEntVentV2 import resuEntregasVentas
from ServFacturado import ServFacturadoV2
from TenenImposiV2 import TenenImpositivasV2
from VentaV2 import cuenta_ventasV2
from ctacte_HistAcobrarV2 import cuenta_ctacte_histAcobrarV2
from ctacte_HistApagarV2 import cuenta_ctacte_histApagarV2
from ctacte_HistAvencerV2 import cuenta_ctacte_histAvencerV2
from ctacte_HistVencidoV2 import cuenta_ctacte_histVencidoV2
from ctacte_PesiFechaComproV2 import cta_cte_pesiFechaComproV2
from ctacte_apliAcobrar import cta_cte_apliAcobrar
from ctacte_apliApagar2 import cta_cte_apliApagarV2
from ctacte_apliAvencer2 import cta_cte_apliAvencerV2
from ctacte_apliVencida2 import cta_cte_apliVencidoV2
from ctacte_aplicada15diasV import cta_cte_aplicada_15_Vencer
from ctacte_pesifechavenci import cta_cte_pesiFechaVevcimiento
from RetencionesV2 import cuenta_retencionesV2
from finanzasPagos import finanzaspagos
from insumos_producto import insumosProductos
from logistOperPrimarias import logistOperPrimarias


def ejecutar_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRegistroUsuario))
    test_suite.addTest(unittest.makeSuite(Perfil_Usuario))
    test_suite.addTest(unittest.makeSuite(HomeSaldoCuentHoyV2))
    test_suite.addTest(unittest.makeSuite(HomeResNegocioTenantV2))
    test_suite.addTest(unittest.makeSuite(HomeEntVentRecientesV2))
    test_suite.addTest(unittest.makeSuite(granos_contratos))
    test_suite.addTest(unittest.makeSuite(insumosProductos))
    test_suite.addTest(unittest.makeSuite(precio_granos_fijaciones))
    test_suite.addTest(unittest.makeSuite(dashboard_granos))
    test_suite.addTest(unittest.makeSuite(mis_intenciones))
    test_suite.addTest(unittest.makeSuite(cta_cte_apliAcobrar))
    test_suite.addTest(unittest.makeSuite(cta_cte_apliApagarV2))
    test_suite.addTest(unittest.makeSuite(cta_cte_apliAvencerV2))
    test_suite.addTest(unittest.makeSuite(cta_cte_apliVencidoV2))
    test_suite.addTest(unittest.makeSuite(cta_cte_aplicada_15_Vencer))
    test_suite.addTest(unittest.makeSuite(cta_cte_pesiFechaComproV2))
    test_suite.addTest(unittest.makeSuite(cta_cte_pesiFechaVevcimiento))
    test_suite.addTest(unittest.makeSuite(cuenta_ctacte_histAcobrarV2))
    test_suite.addTest(unittest.makeSuite(cuenta_ctacte_histApagarV2))
    test_suite.addTest(unittest.makeSuite(cuenta_ctacte_histAvencerV2))
    test_suite.addTest(unittest.makeSuite(cuenta_ctacte_histVencidoV2))
    test_suite.addTest(unittest.makeSuite(cuenta_retencionesV2))
    test_suite.addTest(unittest.makeSuite(resuEntregasVentas))
    test_suite.addTest(unittest.makeSuite(EntregasVentasV2))
    test_suite.addTest(unittest.makeSuite(ServFacturadoV2))
    test_suite.addTest(unittest.makeSuite(detalle_ctro_entregaVentasV2))
    test_suite.addTest(unittest.makeSuite(detalle_ctro_fijacionesV2))
    test_suite.addTest(unittest.makeSuite(detalle_cto_certificadosV2))
    test_suite.addTest(unittest.makeSuite(detalle_cto_liquidacionesV2))
    test_suite.addTest(unittest.makeSuite(entregas_AplicadasV2))
    test_suite.addTest(unittest.makeSuite(entregas_pend_AplicadasV2))
    test_suite.addTest(unittest.makeSuite(entregas_facturadosV2))
    test_suite.addTest(unittest.makeSuite(entregas_Pend_FacturarV2))
    test_suite.addTest(unittest.makeSuite(cuenta_ventasV2))
    test_suite.addTest(unittest.makeSuite(TenenImpositivasV2))
    test_suite.addTest(unittest.makeSuite(cuenta_pend_facturarV2))
    test_suite.addTest(unittest.makeSuite(cuenta_pend_retirarV2))
    test_suite.addTest(unittest.makeSuite(cuenta_mercaderia_facturarV2))
    test_suite.addTest(unittest.makeSuite(cuenta_mercaderia_remitidaV2))
    test_suite.addTest(unittest.makeSuite(comprobanteCtaCteV2))
    test_suite.addTest(unittest.makeSuite(comprobanteContratoV2))
    test_suite.addTest(unittest.makeSuite(comprobanteEntregasV2))
    test_suite.addTest(unittest.makeSuite(comprobanteVentasV2))
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
        ruta_informe_fallidos = generar_informe_fallidos(failed_tests, "reporte_suiteV2")
        enviar_informe_por_correo(ruta_informe_fallidos)
    else:
        print("No hubo tests fallidos.") 