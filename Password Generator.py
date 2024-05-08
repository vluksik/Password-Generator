import random
import string


def generate_random_password(length=30): # Default length is 30
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = "!()_+=-:,.<>?" # Add more special characters if needed

    all_characters = lowercase_letters + uppercase_letters + numbers + special_characters 

    length = max(length, 8) # Minimum length of password should be 8

    password = ''.join(random.choice(all_characters) for _ in range(length)) # Generate random password

    return password


if __name__ == "__main__": # If this file is run directly
    password = generate_random_password()
    print("Generated Password:", password)
