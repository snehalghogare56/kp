class MedicalChatbot:
    def __init__(self):
        self.knowledge_base = {
            "symptoms of flu": "Common symptoms of flu include fever, cough, sore throat, body aches, and fatigue.",
            "treatments for headache": "To relieve a headache, you can try resting in a quiet, dark room, applying a cold or warm compress, and taking over-the-counter pain relievers.",
            "signs of dehydration": "Signs of dehydration include dark yellow urine, dry mouth, dizziness, and increased thirst. It's important to drink enough fluids to stay hydrated.",
            "first aid for burns": "For minor burns, you can run cool water over the affected area, apply a clean bandage, and take over-the-counter pain relievers if needed. Seek medical attention for severe burns.",
            "chest pain": "Chest pain can be a symptom of various conditions, including heart-related issues. If you experience severe or persistent chest pain, seek emergency medical attention.",
            "foods for a healthy heart": "To maintain a healthy heart, consider including foods like fatty fish, nuts, whole grains, fruits, and vegetables in your diet.",
            "tips for better sleep": "Establish a regular sleep schedule, create a relaxing bedtime routine, and ensure your sleep environment is comfortable for better sleep.",
            "how to prevent the common cold": "To prevent the common cold, practice good hand hygiene, avoid close contact with sick individuals, and maintain a healthy lifestyle.",
            "benefits of regular exercise": "Regular exercise offers numerous benefits, including improved cardiovascular health, enhanced mood, and better weight management.",
            "goodbye": "Thank you for using the Medical Chatbot. If you have more health-related questions, consult a healthcare professional. Goodbye!",
        }

    def answer_question(self, question):
        question = question.lower()
        for keyword, answer in self.knowledge_base.items():
            if keyword in question:
                return answer
        return "I'm sorry, I don't have information on that. If you have health concerns, please consult a healthcare professional."

if __name__ == "__main__":
    chatbot = MedicalChatbot()

    print("Medical Chatbot: Hi! I'm here to provide information on common medical topics.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Medical Chatbot: Thank you for using the Medical Chatbot. If you have more health-related questions, consult a healthcare professional. Goodbye!")
            break

        answer = chatbot.answer_question(user_input)
        print("Medical Chatbot:", answer)
