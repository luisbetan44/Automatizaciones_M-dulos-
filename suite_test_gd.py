import unittest
from Home import HomeTenant 
from Conf_ventas import Conf_ventas_test_tenant
from contrato import contrato_tenant
from Entregas import cuenta_entregas
from Ventas import cuenta_ventas
from Onboarding import Onboarding_test_tenant

if __name__ == "__main__":
    
    test_suite = unittest.TestSuite()

    
    test_suite.addTest(unittest.makeSuite(HomeTenant))
    test_suite.addTest(unittest.makeSuite(contrato_tenant))
    test_suite.addTest(unittest.makeSuite(cuenta_entregas))
    test_suite.addTest(unittest.makeSuite(cuenta_ventas))
    test_suite.addTest(unittest.makeSuite(Onboarding_test_tenant))

    runner = unittest.TextTestRunner()
    runner.run(test_suite)

