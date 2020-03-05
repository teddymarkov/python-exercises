# SRC: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
from typing import List


def get_less_items(a: int) -> List[int]:
    return list(
        filter(
            lambda x: x < a,
            [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        )
    )


def output_res(res: List[int]):
    print(str(res))


def main():
    num = int(input("Enter a num: "))
    output_res(get_less_items(num))


if __name__ == "__main__":
    main()
