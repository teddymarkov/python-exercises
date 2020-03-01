# SRC: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt

a = int(input("Enter a number: "))

def fact(b):
    if b == 0:
        return 1
    return b * fact(b - 1)

print(fact(a))
