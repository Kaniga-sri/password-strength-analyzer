# ========= PASSWORD TOOL (FULL DEBUGGED VERSION) =========

import hashlib
import random
import string

# ------------------ GENERATOR ------------------
def generate_password(length=12):
    sample1 = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(sample1)

    return password


# ------------------ HASH FUNCTION ------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ------------------ CHECK PASSWORD ------------------
def check_password(password):

    has_uppercase = False
    has_lowercase = False
    has_specialchar = False
    has_num = False

    if len(password) >= 8:
        print("Length OK")

        for ch in password:
            if ch.isupper():
                has_uppercase = True
            elif ch.islower():
                has_lowercase = True
            elif ch.isdigit():
                has_num = True
            else:
                has_specialchar = True
    else:
        print("Too short")

    score = 0

    if len(password) >= 8:
        score += 1
    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1
    if has_num:
        score += 1
    if has_specialchar:
        score += 1

    if score <= 2:
        print("Weak Password")
    elif score <= 4:
        print("Medium Password")
    else:
        print("Strong Password")

    print("Score:", score, "/ 5")

    if score < 5:
        print("\nSuggestions:")

        if len(password) < 8:
            print("- Increase length to at least 8 characters")
        if not has_uppercase:
            print("- Add an uppercase letter")
        if not has_lowercase:
            print("- Add a lowercase letter")
        if not has_num:
            print("- Add a number")
        if not has_specialchar:
            print("- Add a special character")

    # ------------------ PASSWORD REUSE CHECK ------------------
    hashed_password = hash_password(password)
    print("Hash:", hashed_password)

    try:
        with open("password_history.txt", "r") as file:
            old_passwords = file.read().splitlines()
    except FileNotFoundError:
        old_passwords = []

    if hashed_password in old_passwords:
        print("PASSWORD ALREADY USED!")
    else:
        with open("password_history.txt", "a") as file:
            file.write(hashed_password + "\n")
        print("Password saved safely.")

    print("\nGenerated Strong Password:")
    print(generate_password())


# ------------------ RUN ------------------
while True:
    print("\n===== PASSWORD TOOL =====")
    print("1. Check Password")
    print("2. Generate Password")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        password = input("Enter password: ")
        check_password(password)

    elif choice == "2":
        print("\nGenerated Strong Password:")
        print(generate_password())

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")