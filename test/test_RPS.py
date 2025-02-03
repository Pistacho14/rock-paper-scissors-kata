import pytest
from src.class_main import MainGame
from src.enum import GameAction, GameResult


@pytest.mark.draw
def test_draw():
    '''
    Partidas con empate
    '''

    assert GameResult.Tie == MainGame.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.ROCK)

    assert GameResult.Tie == MainGame.assess_game(
        user_action=GameAction.SCISSOR, 
        computer_action=GameAction.SCISSOR)

    assert GameResult.Tie == MainGame.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.PAPER)

@pytest.mark.ROCK
def test_rock_loses():
    '''
    Rock pierde con Paper 
    '''
    assert GameResult.Victory == MainGame.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.ROCK)

@pytest.mark.ROCK
def test_rock_wins():
    '''
    Rock gana a SCISSOR
    '''
    assert GameResult.Defeat == MainGame.assess_game(
        user_action=GameAction.SCISSOR,
        computer_action=GameAction.ROCK)

@pytest.mark.PAPER
def test_paper_loses():
    '''
    Paper pierde con SCISSOR
    '''
    assert GameResult.Victory == MainGame.assess_game(
        user_action=GameAction.SCISSOR,
        computer_action=GameAction.PAPER)

@pytest.mark.PAPER
def test_paper_wins():
    '''
    Paper gana a Rock
    '''
    assert GameResult.Defeat == MainGame.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.PAPER)

@pytest.mark.SCISSOR
def test_scissor_loses():
    '''
    SCISSOR pierde con Rock 
    '''
    assert GameResult.Victory == MainGame.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SCISSOR)

@pytest.mark.SCISSOR
def test_scissor_wins():
    '''
    SCISSOR gana a Paper 
    '''
    assert GameResult.Defeat == MainGame.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SCISSOR)