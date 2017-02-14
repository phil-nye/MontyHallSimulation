import random as rnd


class GameShow:
    win_count = 0
    lose_count = 0
    total = 0

    def __init__(self):
        self.doors = ['reward', 'nothing a', 'nothing b']
        self.host = ''
        self.reward = ''
        self.player = ''
        self.set_door()

    def set_door(self):
        rnd.shuffle(self.doors)
        self.host = 'reward'

    # only enable if you want user input
    def player_choice(self):
        decision = input('Enter (1, 2, or 3): ')

        # loop if invalid input
        while decision != 3 and decision != 2 and decision != 1:
            decision = input('Enter (1, 2, or 3): ')
            
        self.player = self.doors[decision]

    def get_wrong(self):       # this method is suboptimal
        # pick a wrong door that has not been chosen, yet
        while self.host == 'reward' or self.host == self.player:
            self.host = rnd.choice(self.doors)

    def check_win(self):
        if self.player == 'reward':
            self.win_count += 1
        else:
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

        while new_choice == self.choice or new_choice == wrong:
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

            if method == 2:
                wrong = self.get_wrong()
                self.choice = self.rand_change(wrong)
            elif method == 1:
                wrong = self.get_wrong()
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
# print("Randomly Change")
# g = GameShow()
# g.autoplay(2, 1000000)
