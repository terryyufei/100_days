import re

"""
syntax for re.sub(pattern, repl, string, count=0, flags=0)
"""

url = input("URL: ").strip()

#username = url.replace("https://twitter.com/", "")
#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
"""
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))
else:
    print("Inavlid input")
"""
# OR
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
else:
    print("Inavlid input")
