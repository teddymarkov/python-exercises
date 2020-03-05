# SRC: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt


def get_factorial(b: int) -> int:
    if b == 0:
        return 1
    return b * get_factorial(b - 1)


def output_fact(res: int):
    print(str(res))


def main():
    a = int(input("Enter a number: "))
    output_fact(get_factorial(a))


if __name__ == "__main__":
    main()
