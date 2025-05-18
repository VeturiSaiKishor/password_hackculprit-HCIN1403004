import re

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return bool(re.search(r'[A-Z]', password))

def check_lowercase(password):
    return bool(re.search(r'[a-z]', password))

def check_digit(password):
    return bool(re.search(r'\d', password))

def check_special_char(password):
    return bool(re.search(r'[\W_]', password))

def check_repeated_chars(password):
    # Check for 3 or more repeated characters in a row
    return not bool(re.search(r'(.)\1\1', password))

def check_sequential_chars(password):
    # Check for simple sequences like 'abc', '123'
    sequences = ['abcdefghijklmnopqrstuvwxyz', '0123456789']
    password_lower = password.lower()
    for seq in sequences:
        for i in range(len(seq) - 2):
            if seq[i:i+3] in password_lower:
                return False
    return True

def password_strength(password):
    score = 0
    feedback = []

    if check_length(password):
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if check_uppercase(password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if check_lowercase(password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if check_digit(password):
        score += 1
    else:
        feedback.append("Add digits.")

    if check_special_char(password):
        score += 1
    else:
        feedback.append("Add special characters.")

    if check_repeated_chars(password):
        score += 1
    else:
        feedback.append("Avoid repeated characters.")

    if check_sequential_chars(password):
        score += 1
    else:
        feedback.append("Avoid sequential characters.")

    strength_levels = {
        7: "Very Strong",
        5: "Strong",
        3: "Medium",
        1: "Weak",
        0: "Very Weak"
    }

    # Find closest strength level
    strength = "Very Weak"
    for level in sorted(strength_levels.keys(), reverse=True):
        if score >= level:
            strength = strength_levels[level]
            break

    return strength, feedback

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    strength, feedback = password_strength(pwd)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve:")
        for f in feedback:
            print(f"- {f}")