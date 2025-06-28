# Projekt: Alex.ai – Moduł Pracowników z Niepełnosprawnościami
# Autor: Aleksander Rajca
# Wersja: 1.0

MINIMALNE_WYNAGRODZENIE = 3490  # Przykład: Minimalna krajowa brutto (PLN)
UID_SRODKI_OTRZYMANE = False    # Flaga: czy środki za UiD zostały przelane

# Baza pracowników z niepełnosprawnością
inwalidzi = {}

# Rejestracja pracownika jako inwalida i administrator
def zglos_inwalide(imie_nazwisko):
    inwalidzi[imie_nazwisko] = {
        "rola": "Administrator",
        "status": "Aktywny",
        "autoryzacja_1euro": False,
        "wynagrodzenie": 0
    }
    print(f"✅ {imie_nazwisko} został zarejestrowany jako Administrator Alex.ai (Inwalida).")

# Potwierdzenie autoryzacji 1€ (np. przelew, potwierdzenie w aplikacji)
def autoryzuj_1euro(imie_nazwisko):
    if imie_nazwisko in inwalidzi:
        inwalidzi[imie_nazwisko]["autoryzacja_1euro"] = True
        print(f"💰 {imie_nazwisko} autoryzował się poprzez wpłatę 1€.")
    else:
        print("❌ Osoba nie została wcześniej zarejestrowana jako inwalida.")

# Wypłata wynagrodzenia po otrzymaniu środków z UiD
def wyplac_wynagrodzenia():
    global UID_SRODKI_OTRZYMANE
    if not UID_SRODKI_OTRZYMANE:
        print("🚫 Środki z UiD nie zostały jeszcze otrzymane. Wypłaty wstrzymane.")
        return

    for osoba in inwalidzi:
        if inwalidzi[osoba]["autoryzacja_1euro"]:
            inwalidzi[osoba]["wynagrodzenie"] = MINIMALNE_WYNAGRODZENIE
            print(f"✅ Wypłacono wynagrodzenie {MINIMALNE_WYNAGRODZENIE} PLN dla: {osoba}")
        else:
            print(f"⏳ {osoba} nie autoryzował się – brak wypłaty.")

# Funkcja aktywacji wypłat (symuluje otrzymanie środków z UiD)
def aktywuj_fundusze_uid():
    global UID_SRODKI_OTRZYMANE
    UID_SRODKI_OTRZYMANE = True
    print("💼 Środki z
