# program_overview.py

class Program:
    def __init__(self):
        self.nazwa = "Alex.ai + RUiDv2"
        self.struktura_plikow = [".d", ".cpp", ".txt", ".html", ".js"]
        self.adres_www = "https://rajcawroclaw.pl"
        self.funkcje = {
            "zarzadzanie_zawartoscia": True,
            "podzial_dostepow": True,
            "funkcjonalnosc_komunikacyjna": True,
            "bezpieczenstwo": True,
        }
        self.ideologia_forum = {
            "wspolpraca": True,
            "konsultacje": True,
            "spolecznosc": True,
        }
        self.ruidv2 = RUiDv2()

    def pokaz_opis(self):
        print(f"📦 Program: {self.nazwa}\n")
        print("📁 Struktura plików:")
        for ext in self.struktura_plikow:
            print(f"  - {ext}")
        print("\n🌐 Strona internetowa:", self.adres_www)

        print("\n🛠️ Kluczowe Funkcje:")
        for k, v in self.funkcje.items():
            print(f"  ✓ {k.replace('_', ' ').capitalize()}")

        print("\n🧠 Ideologia Forum:")
        for k, v in self.ideologia_forum.items():
            print(f"  ✓ {k.capitalize()}")

        print("\n🔍 Informacje o RUiDv2:")
        self.ruidv2.pokaz_info()

class RUiDv2:
    def __init__(self):
        self.wersja = "v2"
        self.linii_kodu = 1200
        self.moduly = [
            "identyfikacja użytkownika",
            "zarządzanie danymi",
            "automatyzacja procesów",
            "analiza danych"
        ]
        self.zastosowania = [
            "korporacje",
            "instytucje rządowe",
            "organizacje non-profit"
        ]

    def pokaz_info(self):
        print(f"🔧 RUiDv2 – Rozszerzona wersja systemu UiD (wersja {self.wersja})")
        print(f"🧩 Linijki kodu: {self.linii_kodu}")
        print("📚 Moduły:")
        for m in self.moduly:
            print(f"  • {m}")
        print("🌍 Zastosowania:")
        for z in self.zastosowania:
            print(f"  • {z}")

# Główne uruchomienie programu
if __name__ == "__main__":
    program = Program()
    program.pokaz_opis()
