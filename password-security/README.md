🔐 Password Security Checker

Overview

This project is a small Python-based educational tool that evaluates password characteristics and provides recommendations for improving password strength.

The tool performs the evaluation locally and does not store the password.

Security Checks

The program checks whether a password contains:

- At least 12 characters
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

It then provides a basic strength classification:

- WEAK
- MEDIUM
- STRONG

Example

A password that lacks sufficient length and character variety may receive recommendations such as:

Password strength: MEDIUM

Recommendations:
- Use at least 12 characters.
- Add at least one special character.

Security Principles Demonstrated

This project demonstrates several basic security concepts:

- Password complexity
- Secure handling of sensitive input
- Local processing
- Input validation
- User security recommendations

Limitations

This tool is an educational password-strength checker. It does not determine whether a password has appeared in a data breach, and a high score does not guarantee that a password is secure.

Real authentication systems should use secure password hashing, salting, MFA, rate limiting, and other appropriate security controls.

Ethical Use

This project is intended for cybersecurity education and defensive security awareness.

No real passwords should be uploaded to this repository.

Technologies

- Python
- Regular expressions
- "getpass" for hidden terminal input
