from enum import Enum


class GameAction(Enum):

    ROCK = 0
    PAPER = 1
    SCISSOR = 2

class GameResult(Enum):

    TIE = 0
    VICTORY = 1
    DEFEAT = 2

dic_actions = {
    GameAction.ROCK: GameAction.SCISSOR,
    GameAction.PAPER: GameAction.ROCK,
    GameAction.SCISSOR: GameAction.PAPER}