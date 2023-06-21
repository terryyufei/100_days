#Write your code below this line 👇
def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

"""
You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

Make sure you name your function/parameters the same as when it's called on the last line of code.

Use the same wording as the Example Outputs to make sure the tests pass.
"""