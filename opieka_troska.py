# opieka_troska.py

class SystemWsparcia:
    def __init__(self):
        self.baza_uzytkownikow = []

    def dodaj_uzytkownika(self, imie, rola):
        self.baza_uzytkownikow.append({
            "imie": imie,
            "rola": rola.lower(),
            "wsparcie": self.przypisz_keyword(rola)
        })

    def przypisz_keyword(self, rola):
        rola = rola.lower()
        if "artysta" in rola or "@artist" in rola:
            return "opieka"
        elif "deweloper" in rola or "developer" in rola or "@deweloper" in rola:
            return "troska"
        else:
            return "brak"

    def pokaz_baze(self):
        print("📘 Lista użytkowników objętych systemem wsparcia:")
        for u in self.baza_uzytkownikow:
            print(f" - {u['imie']} [{u['rola']}] ➤ ;keyword<\"{u['wsparcie']}\">")

    def opis_keyword(self, keyword):
        if keyword == "opieka":
            print("\n🩷 Opieka – dotyczy artystów.")
            print("Opis: W kontekście Alex.ai, słowo 'opieka' odnosi się do wsparcia i troski, jaką system zapewnia artystom w ich działaniach twórczych.")
            print("Przykład: ;keyword<\"opieka\">(@Artist)")
        elif keyword == "troska":
            print("\n🤍 Troska – dotyczy deweloperów.")
            print("Opis: W kontekście Alex.ai, słowo 'troska' odnosi się do uwagi i opieki, jaką system zapewnia deweloperom z czystymi intencjami.")
            print("Przykład: ;keyword<\"troska\"><(deweloper)>")
        else:
            print("\n🔒 Brak przypisanego wsparcia.")

# Przykład użycia
if __name__ == "__main__":
    system = SystemWsparcia()

    # Dodawanie użytkowników
    system.dodaj_uzytkownika("Sylwia Grzeszczak", "@Artist")
    system.dodaj_uzytkownika("Aleksander Rajca", "@Deweloper")
    system.dodaj_uzytkownika("Jan Nowak", "@Tester")

    # Wyświetlenie bazy
    system.pokaz_baze()

    # Opisy
    system.opis_keyword("opieka")
    system.opis_keyword("troska")
