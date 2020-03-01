# SRC: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
ref = int(input("Enter a num: "))
print(
    list(
        filter(
            lambda x: x < ref,
            [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        )
    )
)
