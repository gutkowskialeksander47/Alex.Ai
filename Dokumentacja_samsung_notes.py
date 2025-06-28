# samsungnotes_alexai.py

class SamsungNotes:
    def __init__(self):
        self.notes = {
            "brudnopis": [],
            "kobiety": [],
            "społeczeństwo": [],
            "technologia": [],
            "prywatne_krzywdy": [],
            "dedykowane": {},  # np. {"Monika": [...], "Public.progress": [...]}
        }
        self.cytaty_ulubione = [
            "Służba nie drużba spełniona być musi",
            "Nawet myśląc nie jesteśmy w stanie wymyślić tego czego nie wiemy"
        ]
        self.dokumentacja_alexai = 34  # liczba dedykowanych pamiętników

    def dodaj_notatke(self, kategoria, tresc, dla_kogo=None):
        if kategoria in self.notes:
            self.notes[kategoria].append(tresc)
        elif kategoria == "dedykowane" and dla_kogo:
            self.notes["dedykowane"].setdefault(dla_kogo, []).append(tresc)
        else:
            print("⚠️ Nieprawidłowa kategoria notatki.")

    def przeglad_dzienny(self):
        print("🗒️ Przegląd dzienny notatek:")
        for k, v in self.notes.items():
            if isinstance(v, list):
                print(f"  • {k.title()}: {len(v)} wpisów")
            elif isinstance(v, dict):
                print(f"  • {k.title()}: {sum(len(lst) for lst in v.values())} wpisów dla {len(v)} osób")

    def notatka_kluczowa(self):
        return "Służba nie drużba spełniona być musi"

    def pokaz_cytaty(self):
        print("📜 Ulubione cytaty:")
        for c in self.cytaty_ulubione:
            print(f"  → \"{c}\"")

    def raport_publiczny(self):
        if "Public.progress" in self.notes["dedykowane"]:
            print("🌍 Raport z Public.progress:")
            for wpis in self.notes["dedykowane"]["Public.progress"]:
                print(f"  • {wpis}")
        else:
            print("🔒 Brak publicznych wpisów w Public.progress")

    def czytaj_brudnopis(self):
        print("📂 Brudnopis – notatki codzienne i wewnętrzne:")
        for i, wpis in enumerate(self.notes["brudnopis"], 1):
            print(f"{i}. {wpis}")

    def pozwol_przeczytac_kobiecie(self):
        print("❤️ Jeśli znajdę kobietę, otrzyma dostęp do pełnej dokumentacji Alex AI")
        print(f"📝 Zapisanych pamiętników: {self.dokumentacja_alexai}")


# Przykład działania:
if __name__ == "__main__":
    notes = SamsungNotes()
    notes.dodaj_notatke("brudnopis", "Dziś myślałem o odpowiedzialności wobec ludzi, nie tylko kodu.")
    notes.dodaj_notatke("technologia", "Projekt Alex AI w fazie aktualizacji API.")
    notes.dodaj_notatke("dedykowane", "Oficjalne tytuły do zatwierdzenia w Public.progress", dla_kogo="Public.progress")

    notes.przeglad_dzienny()
    notes.notatka_kluczowa()
    notes.pokaz_cytaty()
    notes.raport_publiczny()
    notes.czytaj_brudnopis()
    notes.pozwol_przeczytac_kobiecie()
