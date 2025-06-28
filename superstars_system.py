# superstars_system.py

class SuperstarSystem:
    def __init__(self):
        self.status_aktywny = False
        self.uzytkownik = None
        self.dostepne_funkcje = {
            "personalizacja": True,
            "ekskluzywne_narzedzia": True,
            "rozszerzona_automatyzacja": True,
            "wsparcie_premium": True,
            "integracje_technologie": ["AI_emocjonalna", "AR", "IoT"]
        }

    def aktywuj(self, uzytkownik):
        if self._spelnia_kryteria(uzytkownik):
            self.status_aktywny = True
            self.uzytkownik = uzytkownik
            print(f"⭐ Status SUPERSTAR aktywowany dla użytkownika: {uzytkownik}")
        else:
            print(f"⛔ Użytkownik {uzytkownik} nie spełnia kryteriów dostępu do Superstar.")

    def _spelnia_kryteria(self, uzytkownik):
        # Przykładowe kryteria – można rozszerzyć o subskrypcje, tokeny itp.
        return hasattr(uzytkownik, "poziom") and uzytkownik.poziom >= 5

    def pokaz_funkcje(self):
        if self.status_aktywny:
            print("\n🔓 Dostępne funkcje SUPERSTAR:")
            for funkcja, wartosc in self.dostepne_funkcje.items():
                print(f"  ✓ {funkcja.capitalize()} - {wartosc}")
        else:
            print("🔒 Funkcje niedostępne – aktywuj status Superstar.")

    def korzysci(self):
        if self.status_aktywny:
            return {
                "efektywnosc": "Zwiększona dzięki automatyzacji",
                "personalizacja": "Pełna kontrola interfejsu i działania",
                "wsparcie": "Priorytetowa pomoc techniczna",
                "technologia": "Dostęp do najnowszych innowacji"
            }
        return {}

# Przykładowy użytkownik do testów
class Uzytkownik:
    def __init__(self, imie, poziom):
        self.imie = imie
        self.poziom = poziom

# Przykładowe uruchomienie
if __name__ == "__main__":
    user = Uzytkownik("Rihanna", poziom=7)
    system = SuperstarSystem()
    system.aktywuj(user)
    system.pokaz_funkcje()
    print("\n🎁 Korzyści:")
    for k, v in system.korzysci().items():
        print(f"  → {k.capitalize()}: {v}")
