def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt the message? (E/D): ").strip().upper()
        if choice not in ['E', 'D']:
            print("Invalid choice. Please choose either 'E' to encrypt or 'D' to decrypt.")
            continue
        
        message = input("Enter the message: ").strip()
        shift = int(input("Enter the shift value: ").strip())

        if choice == 'E':
            result = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {result}")
        else:
            result = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {result}")
        
        another = input("Do you want to process another message? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
