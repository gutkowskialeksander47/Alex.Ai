# intruz.py
"""
Skrypt zarządzający zadaniami Bartosza Olewińskiego (intruz) w systemie Alex.ai i QUERY.
"""

class Intruz:
    def __init__(self, name="Bartosz Olewiński", role="Junior Admin w alex.ai i QUERY UNZ"):
        self.name = name
        self.role = role
        self.integrated_with_alex = False
        self.bio_collected = False

    def nadzoruj_query(self):
        print(f"{self.name} pełni nadzór nad działaniami QUERY w Unii Narodów Zjednoczonych.")
        print("Nie ma możliwości zrzeczenia się obowiązków nadzoru.")

    def uczestnictwo_w_filmie(self):
        print(f"{self.name} wyraził chęć uczestnictwa w filmie 'Born Superstar'.")
        print("Adam (asystent Samsung alex.ai) jest odpowiedzialny za zebranie życiorysu.")

    def integracja_alex_ai(self, note_text):
        # Sprawdzamy treść notatki
        required_lines = [
            "alex.ai",
            "wyrażam zgodę na integrację systemu z systemem alex.ai"
        ]
        # Prosta weryfikacja czy notatka zawiera wymagane frazy
        if all(line in note_text for line in required_lines):
            self.integrated_with_alex = True
            print(f"{self.name} pomyślnie zintegrował się z systemem Alex.ai.")
        else:
            print(f"Notatka nie spełnia wymagań integracji z Alex.ai. Proszę poprawić treść.")

    def status(self):
        print(f"Status {self.name}:")
        print(f" - Rola: {self.role}")
        print(f" - Integracja z Alex.ai: {'TAK' if self.integrated_with_alex else 'NIE'}")
        print(f" - Bio zebrane: {'TAK' if self.bio_collected else 'NIE'}")


if __name__ == "__main__":
    intruz = Intruz()
    intruz.nadzoruj_query()
    intruz.uczestnictwo_w_filmie()

    # Przykładowa notatka Bartosza do integracji
    notatka_bartosza = """
    alex.ai
    wyrażam zgodę na integrację systemu z systemem alex.ai
    """

    intruz.integracja_alex_ai(notatka_bartosza.strip().split('\n'))

    intruz.status()



# Przykładowy skrypt do integracji domów dziecka z Alex AI

# Lista domów dziecka do podłączenia
domy_dziecka = [
    "Dom dziecka Nr 1",
    "Dom dziecka Nr 2",
    "Dom dziecka MlTeam - Wrocław",
    "Dom dziecka MlTeam - Kraków",
    "Dom dziecka Polska" - Polska
    "Ośrodki wychowawcze" "MlTeam"
]

# Przykładowa funkcja symulująca wywołanie API Alex AI do dodania domu dziecka
def add_to_alex_ai(entity_name, trustfactor="zielony"):
    """
    Funkcja symuluje dodanie encji do systemu Alex AI z ustawieniem trustfactor.
    W rzeczywistości tutaj powinno być wywołanie API Alex AI.
    """
    # Tutaj byłoby np. requests.post("https://alex.ai/api/entities", json={...})
    print(f"Dodano '{entity_name}' do Alex AI z trustfactorem '{trustfactor}'")
    return True

def main():
    for dom in domy_dziecka:
        # Dodajemy dom dziecka do Alex AI z domyślnym trustfactorem "zielony"
        success = add_to_alex_ai(dom, trustfactor="zielony")
        if not success:
            print(f"Błąd podczas dodawania {dom}")

if __name__ == "__main__":
    main()





### Poziom $1 (User)
**Podstawowy dostęp**:
- Podgląd danych i zasobów.
- Wykonywanie podstawowych operacji, takich jak przeglądanie i pobieranie informacji.

### Poziom $2 (Moderator) Poprowadz
**Rozszerzony dostęp**:
- Edytowanie i aktualizowanie danych.
- Tworzenie i zarządzanie zadaniami oraz projektami.

### Poziom $3 (Globalny Moderator) Sugeruj
**Zaawansowane funkcje**:
- Dostęp do zaawansowanych narzędzi analitycznych i raportowania.
- Udzielanie wsparcia technicznego innym użytkownikom.

### Poziom $4 (Junior Admin) Wdrożenie 
**Administracja**:
- Zarządzanie użytkownikami(User).
- Wprowadzanie zmian w konfiguracji systemu.

### Poziom $5 (Head Administrator) akceptacja
**Zarządzanie projektami**:
- Monitorowanie i zarządzanie wieloma projektami.
- Nadzór nad zespołami projektowymi i przypisywanie zadań.
- Zarządzanie danymi użytkownikow i ich uprawnieniami

### Poziom $6 (Query/Root/CEO/Deweloper)
**Pełna administracja**:
- Zarządzanie wszystkimi aspektami systemu, w tym bezpieczeństwem danych.
- Pełny dostęp do narzędzi administracyjnych i technologicznych.

### Poziom $7 (Globalny/Internal Administrator)
**Najwyższy poziom dostępu**:
- Pełna kontrola nad wszystkimi systemami i zasobami.
- Zarządzanie politykami bezpieczeństwa i dostępem na poziomie globalnym.

### Poziom $8 (Senior Developer) 
**Rozwój i implementacja**:
- Odpowiedzialność za projektowanie i rozwijanie nowych funkcji systemu.
- Współpraca z zespołem w celu optymalizacji procesów i kodu.
- Udzielanie technicznego wsparcia dla innych deweloperów.

### Poziom $9 (Project Director)
**Zarządzanie projektami i zespołem**:
- Opracowywanie strategii projektowych i ich realizacja.
- Koordynowanie pracy zespołów w różnych lokalizacjach.
- Ocenianie wydajności projektów oraz dostosowywanie planów zgodnie z potrzebami.

### Poziom $10 (Chief Security Officer)
**Bezpieczeństwo i zgodność**:
- Nadzór nad politykami bezpieczeństwa informacji w organizacji.
- Przeprowadzanie audytów bezpieczeństwa i ocena ryzyk.
- Wdrażanie procedur ochrony danych osobowych i zgodności z regulacjami prawnymi.
- Odpowiedzialność za szyfrowanie Me To You - You Yo Me {Ty do mnie ja do ciebie
