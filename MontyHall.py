import random as rnd


class GameShow:
    win_count = 0
    lose_count = 0
    total = 0

    def __init__(self):
        self.door = 0
        self.choice = 0

    @staticmethod
    def set_door():
        return rnd.randint(1, 3)

    # only enable if you want user input
    def player_choice(self):
        self.choice = input('Enter (1, 2, or 3): ')

        # loop if invalid input
        while self.choice != 3 and self.choice != 2 and self.choice != 1:
            self.choice = input('Enter (1, 2, or 3): ')

    def get_door(self):
        return self.door

    def get_choice(self):
        return self.choice

    def get_wrong(self):       # this method is suboptimal
        wrong = rnd.randint(1, 3)

        # loop if you are showing the correct door or the player's choice
        while wrong == self.get_door or wrong == self.choice:
            wrong = rnd.randint(1, 3)

        return wrong

    def check_win(self):
        if self.choice == self.door:
            self.win_count += 1
        elif self.choice != self.door:
            self.lose_count += 1

        self.total += 1

    def rand_change(self, wrong):
        change = rnd.randint(0, 1)

        new_choice = self.choice

        if change == 1:
            new_choice = self.always_change(wrong)

        return new_choice

    def always_change(self, wrong):
        new_choice = 1

        while new_choice != self.choice and new_choice != wrong:
            new_choice += 1

        return new_choice

    def play(self):
        again = 'y'

        while again.lower() is 'y':
            again = ''

            self.set_door()

            print("There are three doors. Only one of these doors has a reward behind it. Choose wisely...")
            self.player_choice()

            print("Here is a clue. There is no reward behind Door", self.get_wrong())
            change = input("Do you want to change? (Y/N) ")

            # loop if invalid input
            while change.lower() is not 'y' or change.lower() is not 'n':
                change = input("Do you want to change? (Y/N) ")

            if change is 'y':
                self.player_choice()

            print("Door:", self.door, ", Choice:", self.choice)
            self.check_win()

            # loop if invalid input
            while again.lower() is not 'y' or again.lower() is not 'n':
                again = input("Play again? (Y/N) ")

        print("Wins:", self.win_count, "/", self.total)
        print("Losses:", self.lose_count, "/", self.total)

    def autoplay(self, method=0, trials=100):
        for x in range(trials):
            self.door = self.set_door()     # reset door placement
            self.choice = rnd.randint(1, 3)
            wrong = self.get_wrong()

            if method == 2:
                self.choice = self.rand_change(wrong)
            elif method == 1:
                self.choice = self.always_change(wrong)
            # keep choice if "no change" method (0)

            # print(x, "\b:", self.get_door(), ",", self.get_choice())
            self.check_win()

        print("Wins:", self.win_count, "/", self.total)
        print("Losses:", self.lose_count, "/", self.total)


print("No Change")
g = GameShow()
g.autoplay(0, 1000000)
print("Always Change")
g = GameShow()
g.autoplay(1, 1000000)
print("Randomly Change")
g = GameShow()
g.autoplay(2, 1000000)
