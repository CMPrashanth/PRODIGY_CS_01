# Caesar Cipher Program

This Python program implements the Caesar Cipher algorithm for both encryption and decryption of text. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- Encrypt messages by shifting characters forward.
- Decrypt messages by shifting characters backward.
- Handles both uppercase and lowercase letters.
- Ignores non-alphabetic characters, leaving them unchanged.

## How It Works

The program consists of the following components:

### Functions

1. **`caesar_cipher_encrypt(text, shift)`**
   - Encrypts the input text using the Caesar Cipher with the given shift value.
   - **Parameters:**
     - `text` (str): The text to be encrypted.
     - `shift` (int): The number of positions to shift each character.
   - **Returns:**
     - `str`: The encrypted text.

2. **`caesar_cipher_decrypt(text, shift)`**
   - Decrypts the input text using the Caesar Cipher with the given shift value.
   - **Parameters:**
     - `text` (str): The text to be decrypted.
     - `shift` (int): The number of positions to shift each character.
   - **Returns:**
     - `str`: The decrypted text.

### Main Program

The `main()` function provides a user interface for encryption and decryption. It repeatedly prompts the user for their choice to either encrypt or decrypt a message, the message itself, and the shift value. After processing, it displays the result and asks the user if they want to process another message.

#### Steps:
1. The user is asked whether they want to encrypt or decrypt a message.
2. The user inputs the message they wish to process.
3. The user inputs the shift value.
4. The program outputs the encrypted or decrypted message.
5. The user is prompted to process another message or exit.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python.
   ```sh
   python caesar_cipher.py
