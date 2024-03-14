# chatbot.py

import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ("(.*) keluhan (.*)", ("Saya akan mencoba membantu Anda. Silakan ceritakan lebih lanjut tentang keluhan Anda.",)),
    # Contoh pola pertanyaan yang dapat dikenali oleh chatbot
]

fallback_responses = ["Mohon maaf, data tidak ditemukan."]

chatbot = Chat(pairs, reflections)

def main():
    print("Selamat datang! Saya chatbot konsultasi penyakit lambung.")
    while True:
        user_input = input("Anda: ")
        response = chatbot.respond(user_input)
        if not response:
            print("Chatbot:", fallback_responses[0])
        else:
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
