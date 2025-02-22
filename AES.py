import os
from Crypto.Cipher import AES

def pad(plaintext):
    padding_len = 16 - (len(plaintext) % 16)
    padding = bytes([padding_len] * padding_len)
    return plaintext + padding, padding_len

def encrypt_file():
    input_file = input("Enter the path to the file to encrypt: ")
    output_file = input("Enter the path to save the encrypted file: ")
    key_file = input("Enter the path to save the key file: ")

    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    padded_text, padding_len = pad(plaintext)
    
    key = os.urandom(16)
    iv = os.urandom(16)
    
    with open(key_file, 'wb') as kf:
        kf.write(key)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = iv + cipher.encrypt(padded_text)
    
    ciphertext = bytes([padding_len]) + ciphertext
    
    with open(output_file, 'wb') as of:
        of.write(ciphertext)
    
    print(f"Encrypted file saved at {output_file}")
    print(f"Key saved at {key_file}")

def decrypt_file():
    input_file = input("Enter the path to the file to decrypt: ")
    output_file = input("Enter the path to save the decrypted file: ")
    key_file = input("Enter the path to the key file: ")

    with open(key_file, 'rb') as kf:
        key = kf.read()
    
    with open(input_file, 'rb') as inf:
        ciphertext = inf.read()
    
    padding_len = ciphertext[0]
    iv = ciphertext[1:17]
    encrypted_data = ciphertext[17:]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    plaintext = decrypted_data[:-padding_len]
    
    with open(output_file, 'wb') as outf:
        outf.write(plaintext)
    
    print(f"Decrypted file saved at {output_file}")

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a file? ").strip().lower()
    if choice == 'e':
        encrypt_file()
    elif choice == 'd':
        decrypt_file()
    else:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()
