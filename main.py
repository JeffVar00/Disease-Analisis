from src.disease_system import DiseaseDiagnosisSystem, Patient


def main():
    engine = DiseaseDiagnosisSystem()
    engine.reset()
    engine.run()

if __name__ == "__main__":
    main() 

