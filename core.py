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

    suggestions = []

    for ch in password:
        if ch.isupper():
            has_uppercase = True
        elif ch.islower():
            has_lowercase = True
        elif ch.isdigit():
            has_num = True
        else:
            has_specialchar = True

    score = 0

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase length to at least 8 characters")

    if has_uppercase:
        score += 1
    else:
        suggestions.append("Add an uppercase letter")

    if has_lowercase:
        score += 1
    else:
        suggestions.append("Add a lowercase letter")

    if has_num:
        score += 1
    else:
        suggestions.append("Add a number")

    if has_specialchar:
        score += 1
    else:
        suggestions.append("Add a special character")

    if score <= 2:
        strength = "Weak Password"
    elif score <= 4:
        strength = "Medium Password"
    else:
        strength = "Strong Password"

    # Password Reuse Check
    hashed_password = hash_password(password)

    try:
        with open("password_history.txt", "r") as file:
            old_passwords = file.read().splitlines()
    except FileNotFoundError:
        old_passwords = []

    reused = hashed_password in old_passwords

    if not reused:
        with open("password_history.txt", "a") as file:
            file.write(hashed_password + "\n")

    return {
        "strength": strength,
        "score": score,
        "suggestions": suggestions,
        "reused": reused,
        "generated_password": generate_password()
    }