class MedicalDiagnosisExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "fever": {
                "symptoms": ["high body temperature", "headache"],
                "diagnosis": "Flu"
            },
            "cough": {
                "symptoms": ["persistent cough", "shortness of breath"],
                "diagnosis": "Respiratory infection"
            },
            "rash": {
                "symptoms": ["itchy rash", "redness"],
                "diagnosis": "Skin allergy"
            },
            "fatigue": {
                "symptoms": ["extreme tiredness", "weakness"],
                "diagnosis": "Chronic fatigue syndrome"
            },
        }

    def get_diagnosis(self, symptoms):
        for condition, data in self.knowledge_base.items():
            if all(symptom in symptoms for symptom in data["symptoms"]):
                return data["diagnosis"]
        return "Unknown"

def main():
    expert_system = MedicalDiagnosisExpertSystem()

    print("Medical Diagnosis Expert System")
    print("Enter your symptoms (comma-separated) or type 'exit' to quit.")

    while True:
        user_input = input("Symptoms: ").strip().lower()

        if user_input == 'exit':
            break

        symptoms = [symptom.strip() for symptom in user_input.split(',')]
        diagnosis = expert_system.get_diagnosis(symptoms)
        print("Diagnosis:", diagnosis)

if __name__ == "__main__":
    main()
