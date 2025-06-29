# uid_system.py

class UiD:
    def __init__(self, sid, role_description, label=None):
        self.sid = sid                # np. 'S_ID_2' lub 'S_ID_0'
        self.role_description = role_description  # opis roli/pozycji
        self.label = label            # np. "#alex UiD", "#User UiD"
    
    def get_info(self):
        return {
            "UID": self.sid,
            "Role": self.role_description,
            "Label": self.label or "Brak etykiety"
        }

# Przykłady UiD
alex_uid = UiD(
    sid='S_ID_2 [123321_XQBJ_98081703811_947749]',
    role_description='Permission Stage CEO',
    label='#alex UiD'
)

vip_uid = UiD(
    sid='S_ID_2 vip',
    role_description='Artist Fan Special L1 Access for ViP in UiD',
    label='#Jula UiD'
)

user_uid1 = UiD(
    sid='S_ID_0 [123321 K2 M A J l4]',
    role_description='Kobieta motocyklista, zweryfikowana numerem PESEL, wierząca, Jteam, LGBT',
    label='#User UiD'
)

user_uid2 = UiD(
    sid='S_ID_0 [123421 Ch AS L2 F]',
    role_description='Chłopak, inwalida, leki, agent FBI, Windows Key Enforced',
    label='#User UiD'
)

# Wersja z aktywacją Microsoft (zasymulowana)
def generate_microsoft_uid(base_code: str, windows_key: str):
    return f"{base_code}_{hash(windows_key) % 100000}"

microsoft_uid = generate_microsoft_uid("123421", "XXXXX-XXXXX-XXXXX-XXXXX")

# Wyświetlenie
for u in [alex_uid, vip_uid, user_uid1, user_uid2]:
    print(u.get_info())

print("Microsoft wygenerowany UID:", microsoft_uid)