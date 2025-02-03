import pytest
from src.class_main import MainGame
from src.enum import GameAction, GameResult


@pytest.fixture
def game():
    setup_game = MainGame()
    return setup_game

@pytest.mark.draw
def test_draw(game):
    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.SPOCK)

    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.LIZARD,
        computer_action=GameAction.LIZARD)

    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.ROCK)

    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.SCISSORS)

    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.PAPER)


@pytest.mark.spock
def test_spock_loses(game):
    '''
    Spock pierde con Lizard y Paper 
    '''
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SPOCK)

    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.LIZARD,
        computer_action=GameAction.SPOCK)


@pytest.mark.spock
def test_spock_wins(game):
    '''
    Spock gana a Rock y Scissors 
    '''
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SPOCK)

    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.SPOCK)


@pytest.mark.lizard
def test_lizard_loses(game):
    '''
    Lizard pierde con Rock y Scissors 
    '''
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.LIZARD)

    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.LIZARD)


@pytest.mark.lizard
def test_lizard_wins(game):
    '''
    Lizard gana a Spock y Paper 
    '''
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.LIZARD)

    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.LIZARD)

@pytest.mark.rock
def test_rock_loses(game):
    '''
    Rock pierde con Spock y Paper 
    '''
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.ROCK)

    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.ROCK)

@pytest.mark.rock
def test_rock_wins(game):
    '''
    Rock gana a Scissors y Lizard 
    '''
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.ROCK)

    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.LIZARD,
        computer_action=GameAction.ROCK)

@pytest.mark.paper
def test_paper_loses(game):
    '''
    Paper pierde con Scissors y Lizard 
    '''
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.PAPER)

    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.LIZARD,
        computer_action=GameAction.PAPER)

@pytest.mark.paper
def test_paper_wins(game):
    '''
    Paper gana a Rock y Spock 
    '''
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.PAPER)

    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.PAPER)

@pytest.mark.scissors
def test_scissors_loses(game):
    '''
    Scissors pierde con Spock y Rock 
    '''
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.SCISSORS)

    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SCISSORS)

@pytest.mark.scissors
def test_scissors_wins(game):
    '''
    Scissors gana a Lizard y Paper 
    '''
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.LIZARD,
        computer_action=GameAction.SCISSORS)

    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SCISSORS)


@pytest.mark.actions
def test_minus_action():

    assert 1 == len(GameAction.minus(
        GameAction.SCISSORS,
        GameAction.LIZARD,
        GameAction.PAPER,
        GameAction.ROCK))

    assert 4 == len(GameAction.minus(GameAction.LIZARD))

    assert GameAction.LIZARD not in GameAction.minus(GameAction.LIZARD)

    assert GameAction.LIZARD in GameAction.minus(GameAction.SPOCK, GameAction.ROCK)