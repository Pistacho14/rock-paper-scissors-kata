import pytest
from main import MainGame
from src.actions import GameAction, GameResult



@pytest.fixture
def game():
    '''
    Setup del objeto game
    '''
    setup_game = MainGame()
    return setup_game


@pytest.mark.draw
def test_draw():
    game = MainGame()
    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.SPOCK)

    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.LIZZARD)

    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.ROCK)

    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.SCISSOR,
        computer_action=GameAction.SCISSOR)

    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.PAPER)


@pytest.mark.spock
def test_spock_loses():
    '''
    Spock pierde con Lizard y Paper 
    '''
    game = MainGame()
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SPOCK)

    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.SPOCK)


@pytest.mark.spock
def test_spock_wins():
    '''
    Spock gana a Rock y Scissors 
    '''
    game = MainGame()
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SPOCK)

    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.SCISSOR,
        computer_action=GameAction.SPOCK)


@pytest.mark.lizard
def test_lizard_loses():
    '''
    Lizard pierde con Rock y Scissors 
    '''
    game = MainGame()
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.LIZZARD)

    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.SCISSOR,
        computer_action=GameAction.LIZZARD)


@pytest.mark.lizard
def test_lizard_wins():
    '''
    Lizard gana a Spock y Paper 
    '''
    game = MainGame()
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.LIZZARD)

    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.LIZZARD)


@pytest.mark.ROCK
def test_rock_loses():
    '''
    Rock pierde con Spock y Paper 
    '''
    game = MainGame()
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.ROCK)

    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.ROCK)


@pytest.mark.ROCK
def test_rock_wins():
    '''
    Rock gana a Scissors y Lizard 
    '''
    game = MainGame()
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.SCISSOR,
        computer_action=GameAction.ROCK)

    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.ROCK)


@pytest.mark.PAPER
def test_paper_loses():
    '''
    Paper pierde con Scissors y Lizard 
    '''
    game = MainGame()
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.SCISSOR,
        computer_action=GameAction.PAPER)

    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.PAPER)


@pytest.mark.PAPER
def test_paper_wins():
    '''
    Paper gana a Rock y Spock 
    '''
    game = MainGame()
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.PAPER)

    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.PAPER)


@pytest.mark.SCISSORS
def test_scissors_loses():
    '''
    Scissors pierde con Spock y Rock 
    '''
    game = MainGame()
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.SPOCK,
        computer_action=GameAction.SCISSOR)

    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SCISSOR)


@pytest.mark.SCISORS
def test_scissors_wins():
    '''
    Scissors gana a Lizard y Paper 
    '''
    game = MainGame()
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.LIZZARD,
        computer_action=GameAction.SCISSOR)

    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SCISSOR)