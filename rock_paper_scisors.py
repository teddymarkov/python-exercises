# SRC: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
from random import randint
from typing import Dict, List

BEATS_MAP: Dict[str, str] = {
    'Paper': "Rock",
    'Scisors': "Paper",
    'Rock': "Scisors"
}
OPTIONS: List[str] = list(BEATS_MAP.keys())
OPTS_MSG: str = ", ".join(OPTIONS)
REQUEST_MV_MSG: str = f"Enter move ({OPTS_MSG}): "


def get_player_move() -> str:
    # Prompt for a move until input is recognized
    player_mv = ""
    while player_mv not in OPTIONS:
        player_mv: str = input(REQUEST_MV_MSG)
    return player_mv


def determine_outcome(pl_mv: str, comp_mv: str):
    if pl_mv == comp_mv:
        print("Draw!")
    elif comp_mv == BEATS_MAP[pl_mv]:
        print("Congratulations! You won!")
    else:
        print("Sorry, you lose...")


def check_continue():
    terminate: bool = input('One more game? (y)') != "y"
    if terminate:
        print("Bye!")
        exit()


def start_game():
    player_mv: str = get_player_move()
    comp_mv: str = OPTIONS[randint(0, 2)]

    print(f"Your move: {player_mv}")
    print(f"Computer move: {comp_mv}")

    determine_outcome(player_mv, comp_mv)

    check_continue()


def main():
    while True:
        start_game()


if __name__ == '__main__':
    main()
