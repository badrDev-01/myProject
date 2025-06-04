import random
import string

def generate_password(length=12):
    if length < 6:
        return "Error: Password length should be at least 6 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
try:
    length = int(input("Enter password length (min 6): "))
    print(f"Generated Password: {generate_password(length)}")
except ValueError:
    print("Error: Please enter a valid number.")
