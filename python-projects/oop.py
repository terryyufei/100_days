# returning a tuple
"""
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) #returning a tuple

if __name__ == "__main__":
    main()
"""
"""
#returning a list

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] #returning a list, not advisable since lists are mutable

if __name__ == "__main__":
    main()
"""

#returning a dictionary

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")
'''
def get_student():
    """
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student #returning a dict
    """
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
'''

#class
"""
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()
"""

# class + raise
"""
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        if not name:
            raise ValueError("Missing name")
        if  house not in ["stark", "lannister", "baratheon", "targaryen"]:
            raise ValueError("Invalid name")

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    
if __name__ == "__main__":
    main()
"""
# using __str__
"""
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        if not name:
            raise ValueError("Missing name")
        if  house not in ["stark", "lannister", "baratheon", "targaryen"]:
            raise ValueError("Invalid name")

    def __str__(self):
     return f"{self.name} from house {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

    
if __name__ == "__main__":
    main()
"""

class Student:
    def __init__(self, name, house, sigil):
        self.name = name
        self.house = house
        self.sigil = sigil

        if not name:
            raise ValueError("Missing name")
        if  house not in ["stark", "lannister", "baratheon", "targaryen"]:
            raise ValueError("Invalid name")

    def __str__(self):
     return f"{self.name} from house {self.house}."
    
    def sigil_words(self):
        match self.sigil:
            case "direwolf":
                return "\U0001F43A winter is coming"
            case "lion":
                return "\U0001F981 hear me roar"
            case "stag":
                return "\U0001F98C Ours Is the Fury,"
            case _:
                return "support characters"



def main():
    student = get_student()
    print(student.sigil_words())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    sigil = input("Sigil: ")
    return Student(name, house, sigil)

    
if __name__ == "__main__":
    main()

