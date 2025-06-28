from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import rsa

# Generowanie kluczy RSA odbiorcy (publiczny i prywatny)
(public_key, private_key) = rsa.newkeys(2048)

def encrypt_message(plain_text):
    # Generowanie klucza AES (symetrycznego)
    session_key = get_random_bytes(16)

    # Szyfrowanie tekstu za pomocą AES
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(plain_text.encode('utf-8'))

    # Szyfrowanie klucza AES za pomocą klucza publicznego RSA odbiorcy
    encrypted_session_key = rsa.encrypt(session_key, public_key)

    # Zwracamy zaszyfrowane dane i zaszyfrowany klucz AES
    return {
        'encrypted_session_key': encrypted_session_key,
        'nonce': cipher_aes.nonce,
        'ciphertext': ciphertext,
        'tag': tag
    }

def decrypt_message(encrypted_data):
    # Odszyfrowanie klucza AES przy pomocy klucza prywatnego RSA
    session_key = rsa.decrypt(encrypted_data['encrypted_session_key'], private_key)

    # Odszyfrowanie tekstu przy pomocy AES
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce=encrypted_data['nonce'])
    plaintext = cipher_aes.decrypt_and_verify(encrypted_data['ciphertext'], encrypted_data['tag'])

    return plaintext.decode('utf-8')

# Przykład użycia
if __name__ == "__main__":
    original_text = "To jest tajna wiadomość od artysty."
    encrypted = encrypt_message(original_text)
    decrypted = decrypt_message(encrypted)

    print("Oryginał:", original_text)
    print("Odszyfrowane:", decrypted)
