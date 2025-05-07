# Expert system for diagnosing common illnesses based on symptoms

def diagnose(symptoms):
    # Symptoms to diagnosis mapping
    diagnosis_rules = {
        "fever, cough, tiredness": "You may have the flu. Please consult a doctor for a test.",
        "headache, nausea, fever": "You might have a viral infection. It's advised to rest and hydrate.",
        "shortness of breath, cough, fever": "It could be COVID-19. Please get a COVID-19 test immediately.",
        "sore throat, cough, runny nose": "It may be a common cold. Rest and hydration can help.",
        "chest pain, sweating, dizziness": "This could be a heart-related issue. Please seek medical help immediately.",
    }

    # Look for a match in the diagnosis rules
    symptoms_key = ", ".join(symptoms).lower()
    
    if symptoms_key in diagnosis_rules:
        return diagnosis_rules[symptoms_key]
    else:
        return "I'm not sure about the symptoms. Please consult a doctor for a proper diagnosis."

# Simple interaction with the user
def medical_expert_system():
    print("Welcome to the Medical Expert System!")
    symptoms = input("Please list your symptoms, separated by commas (e.g., fever, cough, tiredness): ").split(", ")
    
    diagnosis = diagnose(symptoms)
    print(diagnosis)

# Run the system
medical_expert_system()
