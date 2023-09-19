import unittest
from unittest.mock import patch
import io
import sys
from src.disease_system import DiseaseDiagnosisSystem


class TestDiseaseDiagnosisSystem(unittest.TestCase):
    
    def setUp(self):
        self.engine = DiseaseDiagnosisSystem()

    @patch('builtins.input', side_effect=['Jeff', 'Palmares', 's', 's', 'n', 'n', 'n', 'n', 'n'])
    def test_ask_symptoms(self, mock_input):
        
        self.engine.reset()  
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.engine.run()

        sys.stdout = sys.__stdout__

        captured_output_str = captured_output.getvalue()
        self.assertIn("Usted podría tener Gripe", captured_output_str)

if __name__ == '__main__':
    unittest.main()