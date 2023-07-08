"""
def main():
    yell("This is alx")

def yell(phrase):
    print(phrase.upper())

if __name__ == "__main__":
    main()
"""

"""
def main():
    yell("This", "is", "cs50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()
"""

def main():
    yell("This", "is", "cs50")

def yell(*words):
    #uppercased = map(str.upper, words)
    uppercased = [word.upper() for word in words]  # List comprehension
    print(*uppercased)

if __name__ == "__main__":
    main()
