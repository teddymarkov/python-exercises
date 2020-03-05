# SRC: https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
from typing import List


def reverse_words_order(target_sent: str) -> List[str]:
    tgt = target_sent.split()
    return tgt[::-1]


def output_res(res: List[str]):
    print(" ".join(res))


def main():
    sentence = input("Enter some words: ")
    output_res(reverse_words_order(sentence))


if __name__ == "__main__":
    main()
