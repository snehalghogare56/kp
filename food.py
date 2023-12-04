51) Develop a conversational AI chatbot in the field of food ordering system
import random

class FoodOrderingChatbot:
    def __init__(self):
        self.menu = {
            '1': {'name': 'Pizza', 'price': 10.99},
            '2': {'name': 'Burger', 'price': 5.99},
            '3': {'name': 'Pasta', 'price': 8.99},
        }
        self.user_order = {}

    def welcome(self):
        return "Welcome to the Food Ordering Chatbot! How can I help you today?"

    def display_menu(self):
        menu_text = "Menu:\n"
        for item_id, details in self.menu.items():
            menu_text += f"{item_id}. {details['name']} - ${details['price']}\n"
        return menu_text

    def order_food(self, food_item_id):
        if food_item_id in self.menu:
            item = self.menu[food_item_id]
            self.user_order = {'name': item['name'], 'price': item['price']}
            return f"You have ordered {item['name']}. Your total is ${item['price']}. Would you like to place the order?"
        else:
            return "Sorry, I couldn't find that item in the menu. Please try again."

    def check_order_status(self):
        if self.user_order:
            return f"Your current order status is: {self.user_order['name']} is in process."
        else:
            return "You don't have any active orders. Would you like to place a new order?"

    def handle_input(self, user_input):
        user_input = user_input.lower()
        if "order" in user_input:
            food_item_id = input("Enter the item number you want to order: ")
            return self.order_food(food_item_id)
        elif "status" in user_input:
            return self.check_order_status()
        elif "menu" in user_input:
            return self.display_menu()
        elif "exit" in user_input or "quit" in user_input:
            return "Thank you for using the Food Ordering Chatbot. Goodbye!"
        else:
            return "Sorry, I didn't understand that. Can you please repeat?"

    def run(self):
        print(self.welcome())
        while True:
            user_input = input("User: ")
            response = self.handle_input(user_input)
            print(f"Bot: {response}")
            if "exit" in user_input or "quit" in user_input:
                break

if __name__ == "__main__":
    chatbot = FoodOrderingChatbot()
    chatbot.run()
