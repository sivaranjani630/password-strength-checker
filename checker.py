import re

def check_password_strength(password):
    strength = 0

    # Rule 1: Length >= 8
    if len(password) >= 8:
        strength += 1

    # Rule 2: Uppercase
    if re.search(r"[A-Z]", password):
        strength += 1

    # Rule 3: Lowercase
    if re.search(r"[a-z]", password):
        strength += 1

    # Rule 4: Number
    if re.search(r"[0-9]", password):
        strength += 1

    # Rule 5: Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Strength Levels
    if strength == 5:
        return "Strong Password 💪"
    elif strength >= 3:
        return "Medium Password 🙂"
    else:
        return "Weak Password ⚠️"

# Main program
password = input("Enter a password to check: ")
print("Result:", check_password_strength(password))
