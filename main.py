import random
from src.actions import GameAction, GameResult

class MainGame:

    def __init__(self):
        self.user_action = None
        self.computer_action = None

    def get_computer_action(self):
        computer_selection = random.randint(0, len(GameAction) - 1)
        self.computer_action = GameAction(computer_selection)
        print(f"Computer picked {self.computer_action.name}.")
        return self.computer_action


    def get_user_action(self):
        # Scalable to more options (beyond rock, paper and scissors...)
        game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
        game_choices_str = ", ".join(game_choices)
        user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
        self.user_action = GameAction(user_selection)

        return self.user_action
    

    def assess_game(self, user_action, computer_action):
        if user_action == computer_action:
            print("It's a tie!")
            return GameResult.TIE

        elif user_action == GameAction.ROCK:
            if computer_action == GameAction.SCISSOR:
                print("Rock smashes scissors. You won!")
                return GameResult.VICTORY
            else:
                print("Paper covers rock. You lost!")
                return GameResult.DEFEAT

        elif user_action == GameAction.PAPER:
            if computer_action == GameAction.ROCK:
                print("Paper covers rock. You won!")
                return GameResult.VICTORY
            else:
                print("Scissors cuts paper. You lost!")
                return GameResult.DEFEAT

        elif user_action == GameAction.SCISSOR:
            if computer_action == GameAction.PAPER:
                print("Paper covers rock. You won!")
                return GameResult.VICTORY
            else:
                print("Rock smashes scissors. You lost!")
                return GameResult.DEFEAT

    def play_another_round(self):
        another_round = input("\nAnother round? (y/n): ")
        return another_round.lower() == 'y'
    

    def main(self):
        while True:
            try:
                self.user_action = self.get_user_action()
            except ValueError:
                print("Invalid selection. Please try again.")
                continue

            self.computer_action = self.get_computer_action()
            self.assess_game(self.user_action, self.computer_action)


            if not self.play_another_round():
                break


if __name__ == "__main__":
    MainGame().main()