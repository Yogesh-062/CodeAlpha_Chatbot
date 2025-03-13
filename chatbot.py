import customtkinter as ctk
import random
from datetime import datetime


def send_message(event=None):
    user_text = entry.get().strip()
    if user_text:
        chat_window.insert("end", f"You: {user_text}\n", "user")
        entry.delete(0, "end")
        response = get_bot_response(user_text)
        chat_window.insert("end", f"Bot: {response}\n", "bot")
        chat_window.yview("end")


def get_bot_response(user_text):
    responses = {
        "hello": [
            "Hi there! How can I assist you today?",
            "Hello! What can I do for you?",
            "Hey! What's up?",
        ],
        "how are you": [
            "I'm just a chatbot, but I'm doing great! How about you?",
            "Feeling chatty today!",
            "I'm functioning at 100%! How's your day going?",
        ],
        "who are you": [
            "I'm your Yogi's chatbot!",
            "I go by many names, but you can call me ChatBot.",
            "I’m ChatBot, your virtual assistant!",
        ],
        "bye": [
            "Goodbye! Have a great day!",
            "See you soon! Take care.",
            "Bye! Chat with you later.",
        ],
        "what can you do": [
            "I can chat with you, answer basic questions, and keep you entertained!",
            "I can assist with basic queries. What do you need?",
            "I'm here to chat! What do you want to talk about?",
        ],
        "tell me a joke": [
            "Why don't skeletons fight each other? Because they don't have the guts!",
            "Why did the computer catch a cold? It left its Windows open!",
            "What’s a robot’s favorite type of music? Heavy metal!",
        ],
    }
    user_text = user_text.lower()
    for key in responses:
        if key in user_text:
            return random.choice(responses[key])
    return "I'm not sure I understand. Could you rephrase that?"


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Chatbot UI")
root.geometry("400x600")

chat_window = ctk.CTkTextbox(root, width=380, height=500, wrap="word")
chat_window.pack(padx=10, pady=10, fill="both", expand=True)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

entry = ctk.CTkEntry(root, width=300)
entry.pack(padx=10, pady=5, side="left", fill="x", expand=True)
entry.bind("<Return>", send_message)  # Bind Enter key to send message

send_button = ctk.CTkButton(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=5, side="right")

root.mainloop()
