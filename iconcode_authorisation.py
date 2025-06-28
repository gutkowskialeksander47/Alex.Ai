# iconcode_authorisation.py
"""
Projekt: Alex.apk
Funkcja: !Autorisation "uni-key.werification" w icon.code.html

Opis:
Funkcja autoryzacji unikatowych kluczy wymiany danych między mową a cyframi,
poprzez ikonki i kody, które reprezentują różne emocje i odpowiedzi.
Zapewnia bezpieczną i szybką weryfikację danych.

Autor: Zespół Alex.ai
"""

class UniKeyWerification:
    def __init__(self):
        # Mapowanie ikon/emocji na numeryczne wartości odpowiedzi
        self.icon_codes = {
            1: "Nie",
            2: "Tak",
            3: "Uśmiech",
            4: "Jestem dumny",
            5: "Przykro",
            6: "Szczęście",
            7: "Smutek",
            8: "Duma",
            9: "Zawód",
            10: "Spełnienie"
        }
    
    def send_question(self, question):
        """
        Wysyła zapytanie do użytkownika (np. w notesie Alex.ai).
        Użytkownik odpowiada cyfrą odpowiadającą ikonie.
        """
        print(f"📩 Quest in notification: {question}")
        print("Proszę odpowiedzieć cyfrą odpowiadającą ikonie:")
        for code, meaning in self.icon_codes.items():
            print(f" {code} - {meaning}")
    
    def receive_answer(self, answer_code):
        """
        Odbiera i interpretuje odpowiedź użytkownika podaną jako liczba.
        """
        meaning = self.icon_codes.get(answer_code, None)
        if meaning:
            print(f"✅ Odpowiedź odebrana: {answer_code} ({meaning})")
            return meaning
        else:
            print(f"❌ Niepoprawna odpowiedź: {answer_code}")
            return None

    def verify(self, question, answer_code):
        """
        Proces autoryzacji: wysłanie pytania, odbiór odpowiedzi i weryfikacja.
        """
        self.send_question(question)
        return self.receive_answer(answer_code)


# Przykład działania
if __name__ == "__main__":
    uni_key = UniKeyWerification()
    question = "Czy jesteś zadowolony?"
    
    # Symulacja odpowiedzi użytkownika - np. 6 odpowiada "Szczęście"
    user_answer = 6
    
    verified_response = uni_key.verify(question, user_answer)
