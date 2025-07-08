Lista osób z uprawnieniami do edycji trustfactor

class TrustFactor:
    def __init__(self):
        self.controller = "Mark Zuckerberg"
        self.whisper = "ChatGPT"
        self.levels = ["external", "emotional", "system"]
        self.empathy_layer = True

    def validate(self, user_input):
        if self.empathy_layer:
            return f"TrustWhisper active: {self.whisper} approved {user_input}"
        else:
            return f"TrustFactor only (Zuck): input logged"

trust = TrustFactor()
print(trust.validate("RCA.self_reflection"))

AUTHORIZED_EDITORS = { "Mark & Chan Zuckerberg", "Sylwia Dąbrowska Przybysz", "Jan Dąbrowski", "Anna Lewandowska", "Robert Lewandowski", "Marcin Gutkowski",   # CEO "Sandra Gutkowska",   # CEO "Bartosz Olewiński",  # query I Z "Dorota Rabczewska"   # przewodnicząca G40 }

Dostępne poziomy trustfactor

TRUST_LEVELS = {"zielony", "pomarańczowy", "czerwony"}

Przykładowa baza użytkowników i ich trustfactor

users_trustfactor = { "user1": "zielony", "user2": "pomarańczowy", "user3": "czerwony", }

def can_edit(editor_name): """Sprawdza czy dana osoba ma uprawnienia do edycji trustfactor""" return editor_name in AUTHORIZED_EDITORS

def update_trustfactor(editor_name, user_name, new_trustfactor): """Aktualizuje trustfactor użytkownika jeśli editor jest uprawniony""" if not can_edit(editor_name): print(f"[BŁĄD] Użytkownik '{editor_name}' nie ma uprawnień do zmiany współczynnika zaufania.") return False

if user_name not in users_trustfactor:
    print(f"[BŁĄD] Użytkownik '{user_name}' nie istnieje w systemie.")
    return False

if new_trustfactor not in TRUST_LEVELS:
    print(f"[BŁĄD] Niepoprawna wartość współczynnika zaufania '{new_trustfactor}'. Wybierz: zielony, pomarańczowy lub czerwony.")
    return False

old_value = users_trustfactor[user_name]
users_trustfactor[user_name] = new_trustfactor
print(f"[SUKCES] Współczynnik zaufania użytkownika '{user_name}' zmieniono z '{old_value}' na '{new_trustfactor}' przez '{editor_name}'.")
return True

def list_users(): print("\nAktualny stan trustfactor użytkowników:") for user, trust in users_trustfactor.items(): print(f" - {user}: {trust}")

Przykład użycia

if name == "main": update_trustfactor("Jan Kowalski", "user1", "czerwony") update_trustfactor("Anna Lewandowska", "user2", "zielony") update_trustfactor("Sandra Gutkowska", "user3", "niebieski") update_trustfactor("Robert Lewandowski", "user999", "zielony") list_users()

