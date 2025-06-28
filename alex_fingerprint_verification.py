# alex_fingerprint_verification.py
"""
Projekt Alex.ai – Weryfikacja użytkownika za pomocą odcisku palca z ustawień

Opis:
Alex AI nie pobiera bezpośrednio odcisku palca od użytkownika podczas działania.
Korzysta wyłącznie z odcisku palca zapisanych w ustawieniach systemu/urządzenia.

Autor: Zespół Alex.ai
"""

class AlexFingerprintVerifier:
    def __init__(self):
        # Symulacja bazy odcisków palca zapisanych w ustawieniach
        self.stored_fingerprints = {
            "user1": "fp_hash_1234567890abcdef",
            "user2": "fp_hash_abcdef1234567890",
            # ... inne zapisane odciski
        }

    def get_fingerprint_from_settings(self, username):
        """
        Pobierz odcisk palca zapisany w ustawieniach systemu dla danego użytkownika.
        W prawdziwym systemie to będzie interakcja z bezpiecznym magazynem urządzenia.
        """
        print(f"🔐 Pobieranie zapisanego odcisku palca dla użytkownika: {username}")
        fingerprint = self.stored_fingerprints.get(username)
        if fingerprint:
            print("✅ Odcisk palca znaleziony w ustawieniach.")
        else:
            print("❌ Brak odcisku palca w ustawieniach.")
        return fingerprint

    def verify_fingerprint(self, username, fingerprint_to_check):
        """
        Weryfikacja podanego odcisku palca z tym zapisanym w ustawieniach.
        """
        stored_fp = self.get_fingerprint_from_settings(username)
        if not stored_fp:
            return False
        if stored_fp == fingerprint_to_check:
            print("✔️ Weryfikacja zakończona sukcesem.")
            return True
        else:
            print("❌ Weryfikacja nie powiodła się.")
            return False


if __name__ == "__main__":
    verifier = AlexFingerprintVerifier()

    # Symulowany odcisk palca, który aplikacja otrzymuje z urządzenia
    # (w praktyce: po stronie sprzętowej, odcisk jest pobierany i przesyłany przez system)
    sample_fingerprint_input = "fp_hash_1234567890abcdef"
    username = "user1"

    print(f"\n🔎 Weryfikacja użytkownika {username} za pomocą odcisku palca...\n")
    result = verifier.verify_fingerprint(username, sample_fingerprint_input)

    if result:
        print("\n✅ Dostęp przyznany.")
    else:
        print("\n❌ Dostęp odmówiony.")
