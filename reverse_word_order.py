# SRC: https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
# NOTE: Usage of functions was explicitly required.

def reverse_words_order(target_sent: str) -> list:
    tgt: list = target_sent.split()
    return tgt[::-1]

sentence: str = input("Enter some words: ")
res: list = reverse_words_order(sentence)
print(" ".join(res))
