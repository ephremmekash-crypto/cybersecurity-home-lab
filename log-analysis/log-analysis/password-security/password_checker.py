import re
import getpass


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, feedback


print("=" * 50)
print("PASSWORD SECURITY CHECKER")
print("=" * 50)

password = getpass.getpass("Enter a password to evaluate: ")

strength, feedback = check_password_strength(password)

print(f"\nPassword strength: {strength}")

if feedback:
    print("\nRecommendations:")
    for item in feedback:
        print(f"- {item}")
else:
    print("\nGood password characteristics detected.")

print("\nSecurity note:")
print("This tool evaluates the password locally and does not store it.")
