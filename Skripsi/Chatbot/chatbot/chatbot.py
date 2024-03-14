# Contoh kode untuk menginisialisasi chatbot menggunakan Python dan library Natural Language Toolkit (NLTK)

import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ("(.*) keluhan (.*)", ("Saya akan mencoba membantu Anda. Silakan ceritakan lebih lanjut tentang keluhan Anda.",)),
    # Contoh pola pertanyaan yang dapat dikenali oleh chatbot
]

chatbot = Chat(pairs, reflections)

def main():
    print("Selamat datang! Saya chatbot konsultasi penyakit lambung.")
    while True:
        user_input = input("Anda: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
