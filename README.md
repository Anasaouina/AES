# AES File Encryption and Decryption

This Python script allows you to securely encrypt and decrypt files using the AES (Advanced Encryption Standard) algorithm in CBC (Cipher Block Chaining) mode.

## Features
- **Encrypt a file**: Prompts for the file path, generates a random 16-byte key, and saves the encrypted file and key.
- **Decrypt a file**: Prompts for the encrypted file and key path to restore the original content.
- **Padding**: Ensures proper block size alignment using PKCS#7-like padding.
- **User interaction**: Offers a simple console-based menu to choose between encryption and decryption.

## Prerequisites
Ensure you have Python installed along with the required dependencies:

```bash
pip install pycryptodome
```

## Usage
Run the script with Python:

```bash
python AES.py
```

### Encrypt a file
1. Select **E** when prompted.
2. Enter the path of the file you wish to encrypt.
3. Provide the output path to save the encrypted file.
4. Specify the path to store the generated key (`key.bin`).
5. The encrypted file and key are saved to the specified locations.

### Decrypt a file
1. Select **D** when prompted.
2. Enter the path of the file you wish to decrypt.
3. Provide the output path to save the decrypted file.
4. Specify the path to the key file used for encryption.
5. The decrypted content is saved to the specified location.

## File Formats
- **Encrypted file**: Contains the IV, encrypted data, and padding length.
- **Key file**: Contains the randomly generated 16-byte key used for encryption.

## Security Notes
- **Key management**: Ensure the key file is stored securely — without it, decryption is impossible.
- **IV randomness**: A new IV is generated for each encryption, enhancing security.

## Example
### Encrypt a file
```
Do you want to (E)ncrypt or (D)ecrypt a file? E
Enter the path to the file to encrypt: example.txt
Enter the path to save the encrypted file: example_encrypted.bin
Enter the path to save the key file: key.bin
Encrypted file saved at example_encrypted.bin
Key saved at key.bin
```

### Decrypt a file
```
Do you want to (E)ncrypt or (D)ecrypt a file? D
Enter the path to the file to decrypt: example_encrypted.bin
Enter the path to save the decrypted file: example_decrypted.txt
Enter the path to the key file: key.bin
Decrypted file saved at example_decrypted.txt
```

## License
This project is for educational purposes. Feel free to modify and use it as needed.



