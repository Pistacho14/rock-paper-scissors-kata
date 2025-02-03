from enum import IntEnum


class GameAction(IntEnum):

    ROCK = 0
    PAPER = 1
    SCISSOR = 2

class GameResult(IntEnum):

    TIE = 0
    VICTORY = 1
    DEFEAT = 2