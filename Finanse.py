# finanse.py
"""
Projekt Alex.ai – Informacja o Opłatach Dostępu
Autor: Zespół Alex.ai

Opis:
Skrypt zarządza modelem subskrypcyjnym Alex.ai – umożliwia rejestrację,
przegląd planów, wybór planu, aktywację oraz podziękowanie użytkownikowi.
"""

class AlexFinance:
    def __init__(self):
        # baza użytkowników: {username: {"plan": None, "active": False}}
        self.users = {}

        # dostępne plany subskrypcji z cenami
        self.plans = {
            "query.netzt": {"price": "free"},
            "UiD": {"price": "0€"},
            "project.d": {"price": "20$"},
            "RUiDV2": {"price": "29$"},
            "SUID": {"price": "50€"},
            "Samsung Notes": {"price": "19.99€"},
            "RUiDV3": {"price": "39.99€"},
            "RUiDV4": {"price": "12.99€"}
        }

        self.paid_features = [
            "Zaawansowana analiza danych",
            "Integracja z zewnętrznymi systemami",
            "Personalizowane usługi i interfejs"
        ]

    def list_plans(self):
        """Wyświetla dostępne plany subskrypcji."""
        print("📄 Dostępne plany subskrypcji:")
        for name, details in self.plans.items():
            print(f" - {name}: {details['price']}")

    def register_user(self, username):
        if username in self.users:
            print(f"✅ {username} jest już zarejestrowany.")
        else:
            self.users[username] = {"plan": None, "active": False}
            print(f"📝 Zarejestrowano nowego użytkownika: {username}")

    def choose_plan(self, username, plan_name):
        if username not in self.users:
            print("❌ Użytkownik niezarejestrowany. Zarejestruj najpierw.")
            return
        if plan_name not in self.plans:
            print("❌ Niepoprawny plan subskrypcji. Wybierz ponownie.")
            return
        self.users[username]["plan"] = plan_name
        price = self.plans[plan_name]['price']
        print(f"📦 {username} wybrał plan: {plan_name} ({price} / mies.)")

    def activate_features(self, username):
        if username not in self.users:
            print("❌ Użytkownik niezarejestrowany.")
            return
        plan = self.users[username]["plan"]
        if not plan:
            print("⚠️ Wybierz plan subskrypcji przed aktywacją funkcji.")
            return
        self.users[username]["active"] = True
        print(f"✅ Funkcje premium zostały aktywowane dla {username} (plan: {plan}).")
        print("🔓 Dostępne funkcje:")
        for feature in self.paid_features:
            print(f" - {feature}")

    def thank_you(self):
        print("\n🙏 Dziękujemy wszystkim użytkownikom za wsparcie Alex.ai!")
        print("Wasza lojalność pozwala nam rozwijać innowacje i utrzymać najwyższą jakość usług.")


if __name__ == "__main__":
    system = AlexFinance()
    system.list_plans()
    print()

    system.register_user("aleksander.rajca")
    system.choose_plan("aleksander.rajca", "UiD")
    system.activate_features("aleksander.rajca")
    system.thank_you()
