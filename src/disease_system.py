from experta import *

class Patient(Fact):
    pass

class Disease(Fact):
    pass

class DiseaseDiagnosisSystem(KnowledgeEngine):

    @DefFacts()
    def initial_facts(self):
        yield Fact(action='start_diagnosis')
        self.load_diseases_and_symptoms()

    def load_diseases_and_symptoms(self):
        diseases = {}
        current_disease = None

        with open("data/diseases.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    if current_disease is None:
                        current_disease = line
                        diseases[current_disease] = []
                    else:
                        diseases[current_disease].append(line)
                elif current_disease:
                    current_disease = None

        self.declare(Disease(diseases=diseases))    

    @Rule(Fact(action='start_diagnosis'))
    def start_dialogue(self):
        print("Hello, I am a disease diagnosis system.")
        patient_name = input("Please enter your name: ")
        patient_origin = input("Where are you from?: ")
        self.declare(Patient(name=patient_name, origin=patient_origin))

    @Rule(Patient(name=MATCH.name, origin=MATCH.origin),
          Disease(diseases=MATCH.diseases))
    def ask_symptoms(self, name, origin, diseases):
        print(f"Thank you, {name}. Now, please answer 'yes' or 'no' to the following questions:")
        patient_symptoms = []
        asked_symptoms = set()

        if diseases is {}:
            print("No diseases loaded. Please check your data file.")
            return

        for _, disease_symptoms in diseases.items():
                for symptom in disease_symptoms:
                    if symptom not in asked_symptoms:
                        response = input(f"Do you have this symptom: {symptom}? (Y/N): ").lower()
                        if response == "y":
                            patient_symptoms.append(symptom)
                        asked_symptoms.add(symptom)
        
        # add the patient's symptoms to the Patient fact
        self.declare(Patient(symptoms=patient_symptoms))

    @Rule(Patient(symptoms=MATCH.symptoms),
          Disease(diseases=MATCH.diseases))
    def diagnose_disease(self, symptoms, diseases):
        matched_diseases = []
        
        # check if the patient's symptoms match any synptoms of a disease
        for disease, disease_symptoms in diseases.items():
            if set(disease_symptoms).issuperset(set(symptoms)):
                matched_diseases.append(disease)

        # diagnosis
        if matched_diseases:
            for disease in matched_diseases:
                print(f"Possible disease related to {disease}")
        else:
            print("No specific disease found")