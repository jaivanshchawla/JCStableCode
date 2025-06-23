import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

class RockPaperScissorsGame:
    def __init__(self, rounds_to_win=3):
        self.choices = ["rock", "paper", "scissors"]
        self.scores = {"user": 0, "computer": 0, "tie": 0}
        self.history = []
        self.rounds_to_win = rounds_to_win

    def animate_countdown(self):
        for count in ["Rock...", "Paper...", "Scissors...", "Shoot!"]:
            print(Fore.YELLOW + count)
            time.sleep(0.5)

    def get_user_choice(self):
        while True:
            user_input = input(Fore.CYAN + "\nChoose (rock/paper/scissors) or 'q' to quit: ").strip().lower()
            if user_input == 'q':
                return 'q'
            if user_input in self.choices:
                return user_input
            print(Fore.RED + "Invalid choice. Please enter rock, paper, or scissors.")

    def determine_winner(self, user, computer):
        if user == computer:
            return "tie"
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            return "user"
        else:
            return "computer"

    def print_round_result(self, user, computer, result):
        color = { "user": Fore.GREEN, "computer": Fore.RED, "tie": Fore.YELLOW }
        messages = {
            "user": "You win this round!",
            "computer": "Computer wins this round!",
            "tie": "It's a tie!"
        }
        print(f"\nYou chose: {Fore.CYAN}{user.capitalize()}{Style.RESET_ALL}")
        print(f"Computer chose: {Fore.MAGENTA}{computer.capitalize()}{Style.RESET_ALL}")
        print(color[result] + messages[result])
        print(Fore.BLUE + f"Score - You: {self.scores['user']}  Computer: {self.scores['computer']}  Ties: {self.scores['tie']}")

    def print_history(self):
        print(Fore.YELLOW + "\nGame History:")
        for idx, (user, computer, result) in enumerate(self.history, 1):
            print(f"Round {idx}: You - {user.capitalize()} | Computer - {computer.capitalize()} | Result - {result.capitalize()}")

    def play(self):
        print(Fore.GREEN + "=== Rock-Paper-Scissors: Best of {} ===".format(self.rounds_to_win))
        print(Fore.WHITE + "Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")

        while self.scores["user"] < self.rounds_to_win and self.scores["computer"] < self.rounds_to_win:
            user_choice = self.get_user_choice()
            if user_choice == 'q':
                break

            computer_choice = random.choice(self.choices)
            self.animate_countdown()
            result = self.determine_winner(user_choice, computer_choice)
            if result != "tie":
                self.scores[result] += 1
            else:
                self.scores["tie"] += 1
            self.history.append((user_choice, computer_choice, result))
            self.print_round_result(user_choice, computer_choice, result)

        print(Fore.CYAN + "\nFinal Score:")
        print(Fore.BLUE + f"You: {self.scores['user']}  Computer: {self.scores['computer']}  Ties: {self.scores['tie']}")
        if self.scores['user'] > self.scores['computer']:
            print(Fore.GREEN + "Congratulations! You won the match!")
        elif self.scores['user'] < self.scores['computer']:
            print(Fore.RED + "Computer wins the match. Better luck next time!")
        else:
            print(Fore.YELLOW + "It's a draw!")
        self.print_history()
        print(Fore.WHITE + "Thanks for playing!")

if __name__ == "__main__":
    RockPaperScissorsGame(rounds_to_win=3).play()
