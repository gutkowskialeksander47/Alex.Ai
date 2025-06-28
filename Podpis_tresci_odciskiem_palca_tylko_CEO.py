# kazda tresc wychodzaca od CEO jest podpisana cyfrowo w iphone faceid w samsung finger scanner


import hashlib
import datetime

class CEODevice:
    def __init__(self, ceo_name, fingerprint_data):
        self.ceo_name = ceo_name
        self.fingerprint_data = fingerprint_data  # surowe dane odcisku palca (np. hash)
    
    def sign_data(self, data):
        """
        Podpisz dane odciskiem palca CEO.
        Metoda łączy dane z odciskiem palca i generuje hash (podpis).
        """
        timestamp = datetime.datetime.utcnow().isoformat()
        message = f"{data}|{self.fingerprint_data}|{timestamp}"
        
        # Używamy SHA256 do wygenerowania podpisu
        signature = hashlib.sha256(message.encode()).hexdigest()
        
        signed_package = {
            "data": data,
            "signed_by": self.ceo_name,
            "timestamp": timestamp,
            "signature": signature
        }
        
        return signed_package


# Przykład użycia
if __name__ == "__main__":
    # Załóżmy, że fingerprint CEO to hash odcisku palca (np. przechowywany w systemie)
    fingerprint_hash = "a1b2c3d4e5f67890abcdef1234567890abcdef1234567890abcdef1234567890"  
    
    ceo_phone = CEODevice("CEO Aleksander", fingerprint_hash)
    
    outgoing_message = "Pilna wiadomość do zarządu: zatwierdzamy nową strategię."
    
    signed_message = ceo_phone.sign_data(outgoing_message)
    
    print("Podpisana wiadomość wychodząca z telefonu CEO:")
    print(signed_message)
