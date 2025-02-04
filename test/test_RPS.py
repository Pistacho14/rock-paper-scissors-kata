import pytest
from src.class_main import MainGame
from src.enum import GameAction, GameResult


@pytest.mark.draw
def test_draw():
    game = MainGame()
    assert GameResult.TIE == game.assess_game(GameAction.ROCK, GameAction.ROCK)
    assert GameResult.TIE == game.assess_game(GameAction.SCISSOR, GameAction.SCISSOR)
    assert GameResult.TIE == game.assess_game(GameAction.PAPER, GameAction.PAPER)

@pytest.mark.ROCK
def test_rock_loses():
    game = MainGame()
    assert GameResult.DEFEAT == game.assess_game(GameAction.ROCK, GameAction.PAPER)

@pytest.mark.ROCK
def test_rock_wins():
    game = MainGame()
    assert GameResult.VICTORY == game.assess_game(GameAction.ROCK, GameAction.SCISSOR)

@pytest.mark.PAPER
def test_paper_loses():
    game = MainGame()
    assert GameResult.DEFEAT == game.assess_game(GameAction.PAPER, GameAction.SCISSOR)

@pytest.mark.PAPER
def test_paper_wins():
    game = MainGame()
    assert GameResult.VICTORY == game.assess_game(GameAction.PAPER, GameAction.ROCK)

@pytest.mark.SCISSOR
def test_scissor_loses():
    game = MainGame()
    assert GameResult.DEFEAT == game.assess_game(GameAction.SCISSOR, GameAction.ROCK)

@pytest.mark.SCISSOR
def test_scissor_wins():
    game = MainGame()
    assert GameResult.VICTORY == game.assess_game(GameAction.SCISSOR, GameAction.PAPER)