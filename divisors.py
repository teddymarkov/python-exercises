# SRC: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
num = int(input("Enter a num: "))

print(
    [i for i in range(1, num) if num % i == 0]
)
