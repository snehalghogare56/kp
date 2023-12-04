43,60) Build an expert system for financial planning
class FinancialExpertSystem:
    def __init__(self):
        self.knowledge_base = {}

    def ask_question(self, question):
        response = input(question + " (yes/no): ").lower()
        return response == 'yes'

    def get_numeric_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid numeric value.")

    def recommend_investment_strategy(self):
        age = int(input("What is your age? "))
        income = self.get_numeric_input("What is your annual income? $")
        debt = self.get_numeric_input("Do you have any outstanding debt? $")
        risk_tolerance = self.ask_question("Are you comfortable with high-risk investments?")

        # Basic recommendation logic
        recommendation = "Conservative" if age > 50 or debt > 10000 else "Moderate"
        if risk_tolerance:
            recommendation = "Aggressive"

        self.knowledge_base['age'] = age
        self.knowledge_base['income'] = income
        self.knowledge_base['debt'] = debt
        self.knowledge_base['risk_tolerance'] = risk_tolerance

        return recommendation

if __name__ == "__main__":
    financial_expert = FinancialExpertSystem()

    print("Welcome to the Financial Planning Expert System!")

    investment_strategy = financial_expert.recommend_investment_strategy()

    print("\nBased on your responses, we recommend an", investment_strategy, "investment strategy.")
    print("Thank you for using the Financial Planning Expert System!")

