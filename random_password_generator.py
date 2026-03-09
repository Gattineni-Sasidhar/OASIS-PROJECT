import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    
    if not characters:
        print("Error: You must select at least one character type.")
        return None

    
    password = ''.join(random.choices(characters, k=length))
    return password


def main():
    print("===== Random Password Generator =====")

    
    while True:
        try:
            length = int(input("Enter password length (e.g., 8–16): "))
            if 8 <= length <= 16:
                break
            else:
                print("You Have Entered The Number Above Given Number.")
                print("Please enter the number between 8 and 16.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    use_uppercase = input("Should It Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Should It Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Should It Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Should It Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)

    if password:
        print("\nYour generated password is:\n", password)
        print("\n Password generated successfully!.....")

if __name__ == "__main__":
    main()
