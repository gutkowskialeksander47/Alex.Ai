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

"""
Skrypt do zarządzania dostępem do Alex.ai dla osób ubogich.
Julia Ratowska jest odpowiedzialna za dodawanie ich do systemu.
"""

# Lista użytkowników uprawnionych do bezpłatnego dostępu (dodawanych przez Julię)
free_access_users = set()

# Osoba odpowiedzialna za dodawanie kont – Julia Ratowska
AUTHORIZED_MANAGER = "Julia Ratowska"


def add_user_free_access(manager_name, username):
    """
    Dodaje użytkownika do listy zwolnionych z opłat, jeśli operację wykonuje Julia Ratowska.
    """
    if manager_name != AUTHORIZED_MANAGER:
        print(f"[Błąd] {manager_name} nie ma uprawnień do dodawania kont bezpłatnych.")
        return False
    
    if username in free_access_users:
        print(f"[Info] Użytkownik '{username}' już ma bezpłatny dostęp.")
        return True

    free_access_users.add(username)
    print(f"[Sukces] Dodano użytkownika '{username}' do listy zwolnionych z opłat.")
    return True


def is_user_exempt(username):
    """
    Sprawdza, czy użytkownik jest zwolniony z opłat.
    """
    return username in free_access_users


def show_exempt_list():
    """
    Wyświetla listę użytkowników z bezpłatnym dostępem.
    """
    print("\n📋 Lista użytkowników zwolnionych z opłat:")
    if not free_access_users:
        print(" - (brak)")
    for user in free_access_users:
        print(f" - {user}")


# Przykładowe użycie
if __name__ == "__main__":
    # Próba dodania użytkownika przez osobę nieuprawnioną
    add_user_free_access("Adam Nowak", "user_biedny_1")

    # Dodanie przez Julię Ratowską
    add_user_free_access("Julia Ratowska", "user_biedny_1")
    add_user_free_access("Julia Ratowska", "user_biedny_2")

    # Sprawdzenie statusu
    print("\nCzy 'user_biedny_1' musi płacić?")
    print("Nie" if is_user_exempt("user_biedny_1") else "Tak")

    # Wyświetlenie całej listy
    show_exempt_list()

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
"""
System Ostrzeżeń i Kar - Alex.ai
Autorzy egzekwujący: CEO, Xquery, Query I Z
Każda kara wymaga uzasadnienia i jest rejestrowana.
"""

# Uprawnieni egzekutorzy kar i ostrzeżeń
AUTHORIZED_ENFORCERS = {
    "Marcin Gutkowski",  # CEO
    "Sandra Gutkowska",  # CEO
    "Bartosz Olewiński",  # Query I Z
    "Sylwia Dąbrowska Przybysz",  # Xquery
    "Jan Dąbrowski",  # Xquery
    "Anna Lewandowska",  # Xquery
    "Robert Lewandowski"  # Xquery
}

# Baza danych użytkowników
users_data = {
    "user1": {"ostrzezenia": 0, "kara": None},
    "user2": {"ostrzezenia": 1, "kara": "czasowe zawieszenie"},
}

# Rejestr logów kar
penalty_log = []


def is_authorized(name):
    """Sprawdza, czy osoba może nakładać lub usuwać kary."""
    return name in AUTHORIZED_ENFORCERS


def issue_warning(admin, username, reason):
    """Wysyła ostrzeżenie użytkownikowi."""
    if not is_authorized(admin):
        print(f"❌ {admin} nie ma uprawnień do wystawiania ostrzeżeń.")
        return

    if username not in users_data:
        users_data[username] = {"ostrzezenia": 0, "kara": None}

    users_data[username]["ostrzezenia"] += 1
    print(f"⚠️ Ostrzeżenie dla {username} od {admin}. Powód: {reason}")


def apply_penalty(admin, username, penalty, reason):
    """Nakłada karę na użytkownika."""
    if not is_authorized(admin):
        print(f"❌ {admin} nie ma uprawnień do nakładania kar.")
        return

    if username not in users_data:
        users_data[username] = {"ostrzezenia": 0




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
