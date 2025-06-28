from datetime import date

# Przechowujemy klucze autoryzacji przypisane do IMEI
AUTHORIZED_KEYS = {
    "Marcin": {
        "key": "klucz_zarzadu_alex_ai_marcin_123",
        "imei": "123456789012345"  # Przykładowy IMEI Marcina
    },
    "Sandra": {
        "key": "klucz_zarzadu_alex_ai_sandra_456",
        "imei": "987654321098765"  # Przykładowy IMEI Sandry
    },
    "Hania": {
        "key": None,
        "imei": None  # Klucz przyznany po 16 latach, IMEI do przypisania
    }
}

# Lista IMEI telefonów, które mogą zmieniać obsadę zarządu (max 3)
AUTHORIZED_IMEIS_FOR_MANAGEMENT = {
    "123456789012345",  # IMEI Marcina
    "987654321098765",  # IMEI Sandry
    "555666777888999"   # Trzeci uprawniony telefon (np. szef zarządu)
}

def check_hania_age(birth_year, birth_month, birth_day):
    today = date.today()
    birth_date = date(birth_year, birth_month, birth_day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age >= 16

def get_authorization_key(name, imei, birth_year=None, birth_month=None, birth_day=None):
    # Sprawdzenie czy IMEI jest autoryzowany
    if imei not in AUTHORIZED_IMEIS_FOR_MANAGEMENT:
        return "Nieautoryzowany telefon - brak dostępu do zmiany obsady zarządu"
    
    if name == "Hania":
        if birth_year is None or birth_month is None or birth_day is None:
            return "Brak danych o urodzinach Hani"
        if check_hania_age(birth_year, birth_month, birth_day):
            # Przyznaj klucz Hani i przypisz IMEI, jeśli skończyła 16 lat
            AUTHORIZED_KEYS["Hania"]["key"] = "klucz_zarzadu_alex_ai_hania_789"
            AUTHORIZED_KEYS["Hania"]["imei"] = imei
            return AUTHORIZED_KEYS["Hania"]["key"]
        else:
            return "Hania nie ma jeszcze 16 lat - brak klucza"
    else:
        user = AUTHORIZED_KEYS.get(name)
        if user is None:
            return "Brak klucza dla użytkownika"
        # Sprawdź czy podany IMEI zgadza się z przypisanym do użytkownika
        if user["imei"] != imei:
            return f"IMEI telefonu niezgodne z przypisanym dla {name} - brak dostępu"
        return user["key"]

# Przykładowe wywołania

# Marcin używa swojego IMEI
print(get_authorization_key("Marcin", "1998"))

# Sandra używa swojego IMEI
print(get_authorization_key("Sandra", "1944"))

# Hania próbuje z nieautoryzowanego IMEI i jest za młoda
print(get_authorization_key("Hania", "1947", 2010, 5, 20))

# Hania próbuje z autoryzowanego IMEI i ma 16 lat
print(get_authorization_key("Hania", "1947", 2005, 5, 20))

# Ktoś nieautoryzowany próbuje zmienić zarząd
print(get_authorization_key("Marcin", "000000000000000"))
