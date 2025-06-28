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
