import unittest
from src.disease_system import DiseaseDiagnosisSystem, Patient

class TestDiseaseDiagnosis(unittest.TestCase):
    
    def setUp(self):
        self.engine = DiseaseDiagnosisSystem()
    
    def test_patient_symptoms(self):

        patient_fact = Patient(name="Jeff", origin="Palmares", symptoms=["Tos", "Estornudos"])
        self.engine.reset()  
        self.engine.declare(patient_fact)
        self.engine.run()

        disease = "Gripe"
        expected_diagnosis = f"Usted podría tener {disease}"
        self.assertEqual(self.engine.facts[-1].name, expected_diagnosis)