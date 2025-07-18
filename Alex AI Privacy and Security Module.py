# --- Alex AI Privacy and Security Module ---

class PrivacySecurityModule:
    def __init__(self):
        # "Baza danych" w uproszczonej formie (przykład, normalnie powinien być to DB np. SQLite/PostgreSQL)
        self.user_data = {}

    def register_user(self, uid, data):
        """ Rejestracja nowego użytkownika z jego UID i danymi. """
        self.user_data[uid] = data
        print(f"Zarejestrowano użytkownika UID: {uid}")

    def view_user_data(self, requester_uid, target_uid):
        """
        Wgląd w dane prywatne.
        Pozwala zobaczyć dane tylko jeśli requester UID == target UID (sam użytkownik zagląda w swoje dane).
        """
        if requester_uid == target_uid:
            return self.user_data.get(target_uid, "Brak danych użytkownika.")
        else:
            return "Odmowa dostępu: brak uprawnień."

    def edit_user_data(self, requester_uid, target_uid, new_data):
        """
        Edycja danych prywatnych.
        Pozwala edytować dane tylko jeśli requester UID == target UID.
        """
        if requester_uid == target_uid:
            self.user_data[target_uid] = new_data
            return f"Dane użytkownika UID {target_uid} zostały zaktualizowane."
        else:
            return "Odmowa dostępu: brak uprawnień."

# --- Przykładowe użycie modułu ---

alex_ai_privacy = PrivacySecurityModule()

# Dodajmy użytkownika:
alex_ai_privacy.register_user(uid="user123", data={"email": "user@example.com", "phone": "123-456-789"})

# Próba wglądu przez właściwego użytkownika:
print(alex_ai_privacy.view_user_data(requester_uid="user123", target_uid="user123"))

# Próba edycji danych:
print(alex_ai_privacy.edit_user_data(requester_uid="user123", target_uid="user123", new_data={"email": "nowy@example.com"}))

# Próba wglądu przez kogoś innego:
print(alex_ai_privacy.view_user_data(requester_uid="intruz", target_uid="user123"))
