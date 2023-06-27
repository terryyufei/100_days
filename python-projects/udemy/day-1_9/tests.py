'''
names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    print("Hello, " + name + "!")

for i in range(5):
    print(i)

count = 1
while count <= 5:
    print(count)
    count += 1
'''
'''
for i in range(10):
    print(i)
else: 
    print("Loop completed without a break statement")
'''

def say_hello(name):
    print(f"Hello, {name}!")
result = say_hello("Alice")
print(type(result))
