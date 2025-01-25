# SupportBot

**SupportBot** is a simple chatbot implemented in Python that provides automated customer support for common queries. It uses pattern matching with regular expressions to understand user input and respond appropriately.

---

## Features

- **Greeting and Farewell**: Welcomes users when they start a conversation and provides polite goodbyes.
- **Pattern Matching**: Detects user intent using predefined regular expressions.
- **Support Categories**:
  - Product Information
  - Technical Support
  - Return and Refund Policies
  - General Queries
- **Dynamic Responses**: Provides varied responses to maintain a conversational tone.
- **Exit Commands**: Users can end the conversation by typing commands like "quit", "exit", or "bye".

---

## How It Works

1. **Initialization**: The bot starts with a greeting and asks for the user's name.
2. **Query Matching**: User inputs are matched against predefined intents using regular expressions.
3. **Response Generation**: Based on the matched intent, the bot provides an appropriate response.
4. **Exit Handling**: The conversation continues until the user inputs an exit command.

---

## Code Structure

- **Class `SupportBot`**: The main class that handles the chatbot's functionality.
  - `__init__`: Initializes the bot with predefined responses and patterns.
  - `greet`: Welcomes the user and starts the conversation.
  - `make_exit`: Checks if the user wants to exit the conversation.
  - `chat`: Handles the main conversation loop.
  - `match_reply`: Matches user input to predefined intents.
  - Intent Handlers:
    - `ask_about_product`
    - `technical_support`
    - `about_returns`
    - `general_query`
  - `no_match_intent`: Handles unmatched queries.

---

## Usage

1. **Run the Script**: 
   Execute the script in a Python environment:
   ```bash
   python support_bot.py
