# Validate without REGEX

email = input("What is your email? ").strip()

"""
if "@" in email and "." in email:
    print("valid")
else:
    print("Inavlid")
"""

username, domain = email.split("@")
if username and domain.endswith(".com"):     #("." in domain)
    print("Valid")
else:
    print("Invalid")
