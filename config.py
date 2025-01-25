# Configuration for SupportBot

GREETING_RESPONSES = ("Hello!", "Hi there!", "Greetings!")
FAREWELL_RESPONSES = (
    "Thanks for chatting with me. Have a great day!",
    "It was nice talking to you. Take care!",
    "Goodbye, and feel free to reach out if you need any other assistance."
)
NEGATIVE_RESPONSES = ("no", "nope", "nay", "not a chance", "sorry")
EXIT_COMMANDS = ("quit", "pause", "exit", "goodbye", "bye", "farewell", "thanks")

SUPPORT_RESPONSES = {
    'ask_about_product': r'.*\b(product|item|thing)\b.*',
    'technical_support': r'.*\b(technical|IT|software|hardware)\b.*\b(help|support|issue)\b.*',
    'about_returns': r'.*\b(return|refund|exchange)\b.*',
    'general_query': r'.*\b(how|what|when|where|why|who)\b.*\b(help|assist|do)\b.*'
}
