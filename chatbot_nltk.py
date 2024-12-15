import nltk
import random
import re
from termcolor import colored  # For colorful text in the terminal

# Download required NLTK data files
nltk.download('punkt')
nltk.download('wordnet')

# Predefined responses for specific inputs
greeting_inputs = ["hello", "hi", "hey", "greetings", "sup", "what's up"]
greeting_responses = ["Hello! How can I assist you today?", "Hey there! Need any help?", "Hi! How can I support you today?", "Greetings! What can I do for you?"]

# Responses for unknown input
unknown_responses = [
    "I'm not sure I understand that.",
    "Can you rephrase that, please?", 
    "I'm still learning, so I may not have an answer to that.",
    "Hmm, that's interesting. Could you explain it differently?"
]

# Function to check if the user's input is a greeting
def check_for_greeting(user_input):
    for word in user_input.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_responses)
    return None

# Function to generate a response from the chatbot
def generate_response(user_input):
    response = check_for_greeting(user_input)
    if response is not None:
        return response
    else:
        return get_response_from_corpus(user_input)

# Function to get a response from the chatbot's knowledge base (basic corpus-based matching)
def get_response_from_corpus(user_input):
    responses = {
        "what is your name": "I am ChatBot, your friendly assistant!", 
        "how are you": "I'm just a computer program, but I'm feeling helpful today!", 
        "what can you do": "I can chat with you, answer questions, and try to make your day better!", 
        "who created you": "I was created by a team of developers who love coding and AI.", 
        "bye": "Goodbye! Take care! If you need me, I'll be here.", 
        "exit": "Goodbye! Have a great day!"
    }
    
    # Normalize user input (lowercase, remove punctuation, etc.)
    user_input = re.sub(r'[^a-zA-Z ]', '', user_input).lower()
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    # If no predefined response, return a random unknown response
    return random.choice(unknown_responses)

# Function to style text for better aesthetics
def styled_text(text, color="cyan", attrs=[]):
    return colored(text, color, attrs=attrs)

# Main chatbot loop
def start_chatbot():
    print(styled_text("Welcome to the ChatBot!", "green", ["bold", "underline"]))
    print(styled_text("Type 'bye' or 'exit' to end the chat.\n", "yellow"))
    
    while True:
        # Get user input
        user_input = input(styled_text("You: ", "blue", ["bold"]))
        
        if user_input.lower() in ["bye", "exit"]:
            print(styled_text("ChatBot: Goodbye! Have a great day!", "green", ["bold"]))
            break
        
        # Generate a response from the chatbot
        response = generate_response(user_input)
        print(styled_text("ChatBot: ", "magenta", ["bold"]) + styled_text(response, "white"))

if __name__ == "__main__":
    start_chatbot()
