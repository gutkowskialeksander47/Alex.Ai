# armia_bog_project7.py
"""
Projekt: "7" – ArmiaBog
Typ: Sojusz Bezpieczeństwa Globalnego
Opis: 
Projekt „7” to strategiczny sojusz najważniejszych organizacji bezpieczeństwa, którego celem jest zapewnienie 
globalnego pokoju, zwalczanie zagrożeń transgranicznych oraz wymiana informacji w czasie rzeczywistym.

Autor: Alex.ai Security Group | Współpraca z instytucjami partnerskimi
"""

class ArmiaBog:
    def __init__(self):
        self.name = "Projekt 7 – ArmiaBog"
        self.members = {
            "Interpol": [
                "Koordynacja międzynarodowych operacji ścigania",
                "Wymiana danych wywiadowczych",
                "Wsparcie techniczne i szkoleniowe"
            ],
            "PABI": [
                "Monitoring cyberzagrożeń",
                "Wymiana danych o incydentach",
                "Ochrona infrastruktury krytycznej"
            ],
            "ABW": [
                "Zwalczanie terroryzmu",
                "Ochrona bezpieczeństwa wewnętrznego",
                "Neutralizacja zagrożeń systemowych"
            ],
            "CIA": [
                "Globalny wywiad strategiczny",
                "Operacje specjalne",
                "Partnerstwa międzynarodowe"
            ],
            "FBI": [
                "Zwalczanie przestępczości federalnej",
                "Cyberbezpieczeństwo",
                "Ochrona praw obywatelskich"
            ],
            "POLIZEI": [
                "Bezpieczeństwo publiczne w Niemczech",
                "Współpraca transgraniczna",
                "Bezpieczeństwo drogowe i kryminalne"
            ],
            "POLICE": [
                "Bezpieczeństwo lokalne",
                "Ochrona obywateli",
                "Zwalczanie przestępczości międzynarodowej"
            ]
        }

    def show_structure(self):
        print(f"📘 {self.name}\n")
        print("🛡️ Organizacje członkowskie i ich zadania:")
        for agency, tasks in self.members.items():
            print(f"\n🔸 {agency}")
            for task in tasks:
                print(f"  - {task}")

    def thank_you(self):
        print("\n🙏 Podziękowania:")
        print("Dziękujemy wszystkim partnerom projektu '7' za niezłomne zaangażowanie i poświęcenie.")
        print("Wspólna misja przekłada się na zwiększenie bezpieczeństwa globalnego i ochronę przyszłych pokoleń.")

# Uruchomienie skryptu
if __name__ == "__main__":
    armia = ArmiaBog()
    armia.show_structure()
    armia.thank_you()
