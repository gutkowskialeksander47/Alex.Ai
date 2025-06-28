# potrzeba_ai.py
"""
Projekt Alex.ai – Model potrzeb i zalet Alex.ai

Opis:
Alex.ai to wszechstronne narzędzie z wieloma zastosowaniami,
które dostarcza wartość na różnych poziomach.

Autor: Zespół Alex.ai
"""

class PotrzebaAi:
    def __init__(self):
        self.features = {
            "Automatyzacja Procesów": "Automatyzacja rutynowych zadań oszczędza czas i zasoby.",
            "Analiza Danych": "Przetwarzanie i analiza dużych ilości danych w czasie rzeczywistym.",
            "Bezpieczeństwo": "Monitorowanie i wykrywanie zagrożeń dzięki zaawansowanym algorytmom.",
            "Wsparcie Decyzyjne": "Dostarczanie wartościowych informacji wspierających podejmowanie decyzji.",
            "Personalizacja Usług": "Dostosowanie usług do indywidualnych potrzeb użytkowników."
        }

    def ocena_przydatnosci(self, user_needs):
        """
        Ocena przydatności Alex.ai w zależności od potrzeb użytkownika.

        user_needs: list[str] - lista potrzeb użytkownika (np. ["Analiza Danych", "Bezpieczeństwo"])
        """
        print("🔍 Ocena przydatności Alex.ai dla wybranych potrzeb:")
        for need in user_needs:
            description = self.features.get(need)
            if description:
                print(f"✔️ {need}: {description}")
            else:
                print(f"❓ {need}: Brak szczegółowej informacji o tej funkcji.")

        print("\n💡 Alex.ai to wszechstronne narzędzie, które może wspierać różne dziedziny i cele.")

if __name__ == "__main__":
    potrzeba_ai = PotrzebaAi()

    # Przykładowe potrzeby użytkownika
    user_needs = [
        "Automatyzacja Procesów",
        "Bezpieczeństwo",
        "Personalizacja Usług"
    ]

    potrzeba_ai.ocena_przydatnosci(user_needs)
