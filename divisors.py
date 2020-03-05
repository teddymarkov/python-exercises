# SRC: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
from typing import List


def calc_divisors(num: int) -> List[int]:
    return [i for i in range(1, num) if num % i == 0]


def output_res(res: List[int]):
    print(str(res))


def main():
    num = int(input("Enter a num: "))
    output_res(calc_divisors(num))


if __name__ == '__main__':
    main()
