from enum import Enum


class GameAction(Enum):

    ROCK = 0
    PAPER = 1
    SCISSOR = 2
    LIZZARD = 3
    SPOCK = 4

class GameResult(Enum):

    TIE = 0
    VICTORY = 1
    DEFEAT = 2

dic_actions = {
    GameAction.ROCK: (GameAction.SCISSOR, GameAction.LIZZARD),
    GameAction.PAPER: (GameAction.ROCK, GameAction.SPOCK),
    GameAction.SCISSOR: (GameAction.PAPER, GameAction.LIZZARD),
    GameAction.LIZZARD: (GameAction.PAPER, GameAction.SPOCK),
    GameAction.SPOCK: (GameAction.SCISSOR, GameAction.ROCK)}