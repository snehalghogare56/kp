class EducationalChatbot:
    def __init__(self):
        self.knowledge_base = {
            "courses": "We offer a variety of courses including Mathematics, Science, History, Computer Science, Literature, Economics, Chemistry, Physics, Biology, and more.",
            "computer science": "Computer Science is the study of computers, algorithms, and programming.",
            "mathematics": "Mathematics is the study of numbers, quantities, and shapes. It includes algebra, geometry, calculus, and more.",
            "science": "Science encompasses subjects like Physics, Chemistry, Biology, and Earth Science.",
            "literature": "Literature involves the study of written works, including novels, poetry, and plays.",
            "economics": "Economics is the social science that studies the production, distribution, and consumption of goods and services.",
            "chemistry": "Chemistry is the study of matter, its properties, composition, and the changes it undergoes.",
            "physics": "Physics is the study of matter, energy, and the fundamental forces of nature.",
            "biology": "Biology is the study of living organisms and their interactions with each other and the environment.",
            "history": "History is the study of past events, societies, and human achievements.",
            "teachers": "Our experienced faculty consists of dedicated teachers with expertise in their respective fields.",
            "admission": "For admission information, please visit our official website or contact the admission office.",
            "online learning": "We offer online learning options for various courses to provide flexibility to our students.",
            "study tips": "To improve your study habits, consider creating a study schedule, taking breaks, and staying organized.",
            "extracurricular activities": "We encourage students to participate in extracurricular activities like sports, clubs, and community service.",
            "goodbye": "Thank you for chatting with us! If you have more questions, feel free to ask. Goodbye!",
        }

    def answer_question(self, question):
        question = question.lower()
        for keyword, answer in self.knowledge_base.items():
            if keyword in question:
                return answer
        return "I'm sorry, I don't have information on that. If you have specific questions, feel free to ask."

if __name__ == "__main__":
    chatbot = EducationalChatbot()

    print("Educational Chatbot: Hi! I'm here to help with your educational inquiries.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Educational Chatbot: Goodbye! Have a great day.")
            break

        answer = chatbot.answer_question(user_input)
        print("Educational Chatbot:", answer)
