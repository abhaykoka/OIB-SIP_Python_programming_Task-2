import random
import string


def generate_password(length=8):
    """
    Generate a password with at least one uppercase letter, one lowercase letter, one number, and one symbol.
    The minimum length is 8 characters.
    """
    if length < 8:
        length = 8

    # Ensure each character type is included at least once
    mandatory_characters = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices from all character types
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining_characters = [random.choice(all_characters) for _ in range(length - 4)]

    # Combine the mandatory characters with the remaining ones and shuffle the result
    password_list = mandatory_characters + remaining_characters
    random.shuffle(password_list)

    # Join the list to form the final password string
    password = ''.join(password_list)
    return password


def main():
    length = int(input("Enter the desired password length (minimum 8): "))
    if length < 8:
        print("Password length should be at least 8 characters. Setting length to 8.")
        length = 8

    password = generate_password(length)
    print("Generated Password:", password)


if __name__ == "__main__":
    main()
