from functools import reduce


def get_factorial(b: int) -> int:
    fac_rng = list(range(1, b + 1))
    return reduce(lambda x, y: x * b, fac_rng)


def output_fact(res: int):
    print(str(res))


def main():
    num = int(input("Enter a number: "))
    output_fact(get_factorial(num))


if __name__ == "__main__":
    main()
