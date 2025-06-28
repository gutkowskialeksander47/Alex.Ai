# finanse.py
"""
Projekt Alex.ai – Informacja o Opłatach Dostępu
Autor: Zespół Alex.ai

Opis:
Skrypt zarządza informacją o modelu subskrypcyjnym Alex.ai, umożliwia rejestrację,
wybór planu oraz aktywację dostępu do zaawansowanych funkcji.
"""

class AlexFinance:
    def __init__(self):
        self.users = {}  # {username: {"plan": None, "active": False}}

        self.plans = {
 "query.netzt" wolonatriat {price=free}
"UiD" free 0€ 
 "project.d" 20$ 
"RUiDV2" 29$
"SUID" 50€
"Samsung Notes" 19,99€ 
"RUiDV3" 39,99€
"RUiDV4" 12,99€          
        } //#szczegoly dostepu i finansowania znajduja sie w pliku "price_for_subskryption"

        self.paid_features = [
            "Zaawansowana analiza danych",
            "Integracja z zewnętrznymi systemami",
            "Personalizowane usługi i interfejs"
        ]

    def register_user(self, username):
        if username in self.users:
            print(f"✅ {username} jest już zarejestrowany.")
        else:
            self.users[username] = {"plan": None, "active": False}
            print(f"📝 Zarejestrowano nowego użytkownika: {username}")

    def choose_plan(self, username, plan_name):
        if username not in self.users:
            print("❌ Użytkownik niezarejestrowany.")
            return
        if plan_name not in self.plans:
            print("❌ Niepoprawny plan subskrypcji.")
            return
        self.users[username]["plan"] = plan_name
        print(f"📦 {username} wybrał plan: {plan_name} ({self.plans[plan_name]} jednostek/mies.)")

    def activate_features(self, username):
        if username not in self.users:
            print("❌ Użytkownik niezarejestrowany.")
            return
        if not self.users[username]["plan"]:
            print("⚠️ Wybierz plan przed aktywacją.")
            return
        self.users[username]["active"] = True
        print(f"✅ Funkcje premium zostały aktywowane dla {username}.")
        print("🔓 Dostępne funkcje:")
        for feature in self.paid_features:
            print(f" - {feature}")

    def thank_you(self):
        print("\n🙏 Dziękujemy wszystkim użytkownikom za wsparcie!")
        print("Wasza lojalność pozwala nam tworzyć innowacje i utrzymać wysoką jakość usług.")


# Przykład działania
if __name__ == "__main__":
    system = AlexFinance()
    
    system.register_user("aleksander.rajca")
    system.choose_plan("aleksander.rajca", "string_stream")
    system.activate_features("aleksander.rajca")
    system.thank_you()
Oto gotowy skrypt "Finanse" dla projektu Alex.ai, stworzony w formacie dokumentacyjnym, który możesz umieścić na stronie lub w repozytorium:



💸 Skrypt Finansowy – Projekt Alex.ai

📘 Wprowadzenie

Projekt Alex.ai powstał z pasji do technologii, edukacji i twórczego podejścia do interakcji człowieka z AI. Przez długi czas oferowaliśmy nasze usługi bezpłatnie. Jednak w związku z dynamicznym rozwojem systemu oraz pojawieniem się nowych zaawansowanych funkcji, konieczne stało się wprowadzenie opłat dostępu.


---

🎯 Cel Wprowadzenia Opłat

1. Utrzymanie infrastruktury: Koszty związane z serwerami, pamięcią masową i ochroną danych.


2. Rozwój oprogramowania: Finansowanie nowych funkcji, aktualizacji i innowacyjnych modułów.


3. Wsparcie techniczne: Zatrudnienie specjalistów gotowych do pomocy w czasie rzeczywistym.


4. Bezpieczeństwo: Utrzymanie wysokiego poziomu szyfrowania i prywatności użytkowników.




---

🧠 Nowe Funkcje Dostępne w Planach Subskrypcyjnych

🔍 Zaawansowana analiza danych (w czasie rzeczywistym, AI-assisted).

🔗 Integracje API z systemami zewnętrznymi (Facebook, Google, Meta, Microsoft).

🧬 Personalizacja AI: Alex dostosowany do Twojej osobowości i nawyków.

📊 Statystyki i raporty użytkownika generowane przez Alex.ai.

🎓 Moduł edukacyjny "UiD Nauka" z dostępem do transmisji i wykładów.



---

📌 Jak Uzyskać Dostęp do Nowych Funkcji?

1. Rejestracja: Załóż konto na platformie alex.ai lub przez aplikację Alex.apk.


2. Wybierz plan: Oferujemy elastyczne plany dostosowane do użytkowników indywidualnych, VIP oraz organizacji.


3. Aktywacja: Po zaksięgowaniu płatności, funkcje premium zostaną odblokowane automatycznie.


4. Wsparcie: Użytkownicy planów płatnych otrzymują priorytetowe wsparcie 24/7.




---

💼 Plany Subskrypcji 

Plan	Cena roczna	Funkcje

 "query.netzt" wolonatriat {price=free}
"UiD" free 0€ 
 "project.d" 20$ 
"RUiDV2" 29$
"SUID" 50€
"Samsung Notes" 19,99€ 
"RUiDV3" 39,99€
"RUiDV4" 12,99€ 	
		


---

📬 Kontakt

Masz pytania dotyczące płatności lub subskrypcji?
Skontaktuj się z nami: aleksander@rajca.info

Dziękujemy za wspieranie rozwoju Alex.ai – dzięki Twojemu udziałowi możemy tworzyć przyszłość, która jest bezpieczna, inteligentna i naprawdę spersonalizowana.




