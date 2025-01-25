import random
import re

class SupportBot:
    negative_res = ("no", "nope", "nay", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "farewell", "thanks")
    greeting_responses = ("Hello!", "Hi there!", "Greetings!")
    farewell_responses = ("Thanks for chatting with me. Have a great day!", "It was nice talking to you. Take care!",
                          "Goodbye, and feel free to reach out if you need any other assistance.")

    def __init__(self):
        self.support_responses = {
            'ask_about_product': r'.*\b(product|item|thing)\b.*',
            'technical_support': r'.*\b(technical|IT|software|hardware)\b.*\b(help|support|issue)\b.*',
            'about_returns': r'.*\b(return|refund|exchange)\b.*',
            'general_query': r'.*\b(how|what|when|where|why|who)\b.*\b(help|assist|do)\b.*'
        }
        self.name = None

    def greet(self):
        print(random.choice(self.greeting_responses))
        self.name = input("What's your name?\n")
        will_help = input(f"Hi {self.name}, how may I assist you today?\n")
        if will_help in self.negative_res:
            print("Okay, I'll be here if you need me.")
        else:
            self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply.lower():
                print(random.choice(self.farewell_responses))
                return True
        return False

    def chat(self):
        reply = input("Please tell me your query: ").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match:
                if intent == 'ask_about_product':
                    return self.ask_about_product()
                elif intent == 'technical_support':
                    return self.technical_support()
                elif intent == 'about_returns':
                    return self.about_returns()
                elif intent == 'general_query':
                    return self.general_query()
        return self.no_match_intent()

    def ask_about_product(self):
        responses = ("Our product is top-notch and has excellent reviews!\nYou can find all product details on our website.",
                     "I'd be happy to provide more information about our products. What would you like to know?",
                     "Our products are designed with quality and customer satisfaction in mind. How can I assist you with the product you're interested in?")
        return random.choice(responses)

    def technical_support(self):
        responses = ("Please visit our technical support page for detailed assistance.\nYou can also call our tech support helpline for immediate help.",
                     "I'm sorry you're having a technical issue. Can you provide more details about the problem you're experiencing?",
                     "For technical support, I recommend checking our online resources or contacting our support team directly. They'll be able to assist you better with any software or hardware problems.")
        return random.choice(responses)

    def about_returns(self):
        responses = ("We have a 30-day return policy.\nPlease ensure the product is in its original condition when returning.",
                     "Our return policy allows you to return items within 30 days if you're not completely satisfied. What can I help you with regarding returns?",
                     "You can find our full return and refund policy on our website. Let me know if you have any specific questions about the process.")
        return random.choice(responses)

    def general_query(self):
        responses = ("How can I assist you further?",
                     "Is there anything else you'd like to know?",
                     "Please feel free to ask me anything, and I'll do my best to help.")
        return random.choice(responses)

    def no_match_intent(self):
        responses = ("I'm sorry, I didn't quite understand that. Can you please rephrase?",
                     "My apologies, can you provide more details about your question?",
                     "I'm afraid I didn't catch that. Could you rephrase your query in a different way?")
        return random.choice(responses)

bot = SupportBot()
bot.greet()