# SRC: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
from random import randint

options: tuple = (
    "Paper",
    "Scisors",
    "Rock"
)

beats_map: tuple = {
    'Paper': "Rock",
    'Scisors': "Paper",
    'Rock': "Scisors"
}

opts_msg: str = ", ".join(options)
req_mv_msg: str = f"Enter move ({opts_msg}): "

while True:
    # Prompt for a move until input is recognized
    player_mv = None
    while player_mv not in options:
        player_mv: str = input(req_mv_msg)

    comp_mv: str = options[randint(0, 2)]

    print(f"Your move: {player_mv}")
    print(f"Computer move: {comp_mv}")

    if player_mv == comp_mv:
        print("Draw!")
    elif comp_mv == beats_map[player_mv]:
        print("Congratulations! You won!")
    else:
        print("Sorry, you lose...")

    terminate: bool = input('One more game? (y)') != "y"
    if terminate:
        print("Bye!")
        break
