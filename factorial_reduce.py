from functools import reduce

c = int(input("Enter a number: "))

fac_rng = list(range(1, c+1))
print(
    reduce(lambda a, b: a * b, fac_rng)
)
