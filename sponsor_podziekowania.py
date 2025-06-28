# sponsor_podziekowania.py

class Sponsor:
    def __init__(self, nazwa, logo_url=None):
        self.nazwa = nazwa
        self.logo_url = logo_url

class PodziekowaniaDlaSponsorow:
    def __init__(self, projekt_nazwa="Alex.ai"):
        self.projekt = projekt_nazwa
        self.poziom_uprawnien = 4
        self.sponsorzy = []

    def dodaj_sponsora(self, sponsor: Sponsor):
        self.sponsorzy.append(sponsor)

    def wyswietl_podziekowania(self):
        print(f"\n🛡️ Projekt [{self.projekt}]")
        print("🎉 Podziękowania dla Sponsorów\n")
        print("Serdecznie dziękujemy wszystkim naszym sponsorom za ich hojność i wsparcie.")
        print("Bez Waszej pomocy ten projekt nie byłby możliwy.")
        print(f"\n💎 Szczególne podziękowania dla sponsorów na poziomie uprawnień ${self.poziom_uprawnien}:\n")

        if not self.sponsorzy:
            print("Brak sponsorów na poziomie $4.")
        else:
            for s in self.sponsorzy:
                print(f" - {s.nazwa}" + (f" (logo: {s.logo_url})" if s.logo_url else ""))

        print("\n💼 Korzyści dla Sponsorów ($4):")
        print("✅ Wzmianka na Stronie Projektu – nazwa i logo w sekcji podziękowań")
        print("✅ Dostęp do Wersji Beta – wcześniejszy dostęp do nowych funkcji")
        print("✅ Ekskluzywne Aktualizacje – informacje o postępach i planach")
        print("✅ Wsparcie Priorytetowe – pierwszeństwo w pomocy technicznej\n")
        print("Dziękujemy za Wasze wsparcie i zaufanie. ❤️")
        print("Wasza hojność pozwala nam rozwijać ten projekt i wprowadzać innowacje.")

# Przykład użycia
if __name__ == "__main__":
    system_podziekowan = PodziekowaniaDlaSponsorow()

    # Dodaj sponsorów poziomu $4
    system_podziekowan.dodaj_sponsora(Sponsor("SB Maffija"))
    system_podziekowan.dodaj_sponsora(Sponsor("Ekipa S.A.", logo_url="https://ekipa.pl/logo.png"))
    system_podziekowan.dodaj_sponsora(Sponsor("Śliwa x.com", logo_url="https://x.com/sliwa"))

    # Wyświetl podziękowania
    system_podziekowan.wyswietl_podziekowania()
