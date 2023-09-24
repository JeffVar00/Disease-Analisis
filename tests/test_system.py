import unittest
from unittest.mock import patch
import io
import sys
from src.disease_system import DiseaseDiagnosisSystem


class TestDiseaseDiagnosisSystem(unittest.TestCase):
    
    def setUp(self):
        self.engine = DiseaseDiagnosisSystem()

    # podria tener gripe o covid basado en las respuestas = sintomas = Fiebre y Dolor de garganta
    @patch('builtins.input', side_effect=['Jeff', 'Palmares', 's', 's', 'n', 'n', 'n', 'n', 'n', "n", "n"])
    def test_1(self, mock_input):
        
        self.engine.reset()  
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.engine.run()

        sys.stdout = sys.__stdout__

        captured_output_str = captured_output.getvalue()
        self.assertIn("Usted podría tener Gripe", captured_output_str)
        self.assertIn("Usted podría tener COVID-19", captured_output_str)

    # podria tener Resfriado o alergia basado en las respuestas = sintomas = Congestion y Estornudos
    @patch('builtins.input', side_effect=['Jeff', 'Palmares', 'n', 'n', 'n', 's', 'n', 'n', 'n', "s", "n"])
    def test_2(self, mock_input):
        
        self.engine.reset()  
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.engine.run()

        sys.stdout = sys.__stdout__

        captured_output_str = captured_output.getvalue()
        self.assertIn("Usted podría tener Resfriado comun", captured_output_str)
        self.assertIn("Usted podría tener Alergias estacionales", captured_output_str)

if __name__ == '__main__':
    unittest.main()