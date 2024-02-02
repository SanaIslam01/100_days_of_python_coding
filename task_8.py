def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? Enter 'e' or 'd': ").lower()

        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue

        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            result = caesar_cipher(text, shift)
            print("Encrypted text:", result)
        elif choice == 'd':
            result = caesar_cipher(text, -shift)
            print("Decrypted text:", result)

        run_again = input("Do you want to run the code again? Enter 'yes' or 'no': ").lower()
        if run_again != 'yes':
            print("Exiting the program.")
            break
# Call the main function directly
main()
