def get_factorial(a: int) -> int:
    for b in range(1, a):
        a = a * b
    return a


def output_fact(res: int):
    print(str(res))


def main():
    num = int(input("Enter a number: "))
    output_fact(get_factorial(num))


if __name__ == "__main__":
    main()
