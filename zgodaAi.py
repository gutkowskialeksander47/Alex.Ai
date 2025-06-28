# zgodaAi.py

import os

VOICE_PASSPHRASE = "Znam Aleksandra Rajcę"
NOTES_FILENAME = "alex.ai"
NOTES_PHRASE = "Wyrażam zgodę na integrację z Alex.ai i akceptuję Politykę prywatności."

def voice_registration():
    answer = input("🔑 Powiedz (wpisz): ").strip()
    if answer == VOICE_PASSPHRASE:
        print(" Rejestracja głosowa zakończona sukcesem!")
    else:
        print(" Niewłaściwa fraza. Dostęp nieautoryzowany.")

def file_registration():
    if not os.path.exists(NOTES_FILENAME):
        print(f" Nie znaleziono pliku {NOTES_FILENAME}")
        return
    with open(NOTES_FILENAME, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        if content == NOTES_PHRASE:
            print(" Zgoda z notatki potwierdzona!")
        else:
            print(" Treść notatki nieprawidłowa.")

if __name__ == "__main__":
    print("📌 Wybierz metodę rejestracji:")
    print("1. Głosowa fraza")
    print("2. Plik z notatki")
    choice = input("Wybierz (1/2): ").strip()

    if choice == "1":
        voice_registration()
    elif choice == "2":
        file_registration()
    else:
        print("❌ Nieprawidłowy wybór.")