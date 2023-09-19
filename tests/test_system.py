import unittest
from src.disease_system import DiseaseDiagnosisSystem, Patient

class TestDiseaseDiagnosis(unittest.TestCase):
    
    def setUp(self):
        # Create a fresh instance of the expert system for each test case
        self.engine = DiseaseDiagnosisSystem()
    
    def test_patient_symptoms(self):

        # Set up facts (e.g., patient data)
        patient_fact = Patient(name="Alice", origin="City", symptoms=["Cough", "Sneezing"])
        self.engine.reset()  # Clear previous facts

        # Assert patient fact into the knowledge base
        self.engine.declare(patient_fact)

        # Run your rules
        self.engine.run()
        disease = "Common Cold"
        expected_diagnosis = f"Possible disease related to {disease}"

        # Assert the expected outcome
        self.assertEqual(self.engine.facts[-1].name, expected_diagnosis)