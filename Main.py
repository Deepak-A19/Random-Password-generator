import secrets
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    characters = ''
    
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Please include at least one character type.")
        return None

    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the desired password length: "))
    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, include_letters, include_numbers, include_symbols)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()

