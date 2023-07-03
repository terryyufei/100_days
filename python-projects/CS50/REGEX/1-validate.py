import re


"""
Regular Expression Patterns
syntax for re.search is re.search(pattern, string, flags=0)
flags include re.IGNORECASE, re.MULTILINE, re.DOTALL
"""
email = input("What is your email? ").strip()

#if re.search(r"^.+@.+\.com$", email):
#if re.search(r"^[^@]+@[^@]+\.com$", email):
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
#if re.search(r"^\w+@\w+\.com$", email):
#if re.search(r"^\w+@\w+\.com$", email, re.IGNORECASE):
if re.search(r"^\w+@(\w+\.)?(\w+\.)?\w+\.ke|com", email):
    print("Valid")
else:
    print("Invalid")
