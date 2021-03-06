import random as rnd


class GameShow:
    win_count = 0
    lose_count = 0
    total = 0

    def __init__(self):
        self.doors = ['reward', 'nothing a', 'nothing b']
        self.reward = 0
        self.wrong = 0
        self.host = ''
        self.player = ''
        self.set_door()

    def set_door(self):
        rnd.shuffle(self.doors)
        print(self.doors)
        self.reward = self.doors.index('reward')
        self.host = 'reward'

    # only enable if you want user input
    def player_choice(self):
        decision = input('Enter (1, 2, or 3): ')

        # loop if invalid input
        while decision != '3' and decision != '2' and decision != '1':
            decision = input('Enter (1, 2, or 3): ')
            
        self.player = self.doors[int(decision) - 1]

    def set_wrong(self):       # this method is suboptimal
        # pick a wrong door that has not been chosen, yet
        while self.host == 'reward' or self.host == self.player:
            self.host = rnd.choice(self.doors)
            self.wrong = self.doors.index(self.host) + 1
        
    def get_wrong(self):
        return self.wrong

    def check_win(self):
        if self.player == 'reward':
            self.win_count += 1
        else:
            self.lose_count += 1

        self.total += 1

    def rand_change(self):
        change = rnd.randint(0, 1)

        if change == 1:
            self.always_change()

    def always_change(self):
        new_choice = rnd.choice(self.doors)

        while new_choice is self.player or new_choice is self.host:
            new_choice = rnd.choice(self.doors)
        
        self.player = new_choice

    def play(self):
        again = 'y'

        while again.lower() == 'y':
            again = ''

            print("There are three doors. Only one of these doors has a reward behind it. Choose wisely...")
            self.set_door()
            self.player_choice()

            self.set_wrong()
            print("\nHere is a clue. There is no reward behind Door", self.get_wrong(), '\b.')
            change = input("\nDo you want to change? (Y/N) ")

            # loop if invalid input
            while change.lower() != 'y' and change.lower() != 'n':
                change = input("Do you want to change? (Y/N) ")

            # Uncomment below to cheat
            # print("\nHost: ", self.wrong + 1, '(', self.host, ')', "\tPlayer: ", self.player)
            
            if change == 'y':
                self.player_choice()

            print("\nReward:", self.reward + 1, ", Choice:", self.doors.index(self.player) + 1, self.player)
            self.check_win()

            # loop if invalid input
            while again.lower() != 'y' and again.lower() != 'n':
                again = input("\nPlay again? (Y/N) ")
            
            print('\n\n')

        print("Wins:", self.win_count, "/", self.total)
        print("Losses:", self.lose_count, "/", self.total)

    def autoplay(self, method=0, trials=100):
        for x in range(trials):
            self.set_door()     # reset door placement
            self.player = rnd.choice(self.doors)
            self.set_wrong()
            self.get_wrong()

            if method == 2:
                print('Change Randomly')
                self.rand_change()
            elif method == 1:
                print('Always Change')
                self.always_change()
            else:
                print('No Change (by default)')

            # print(x, "\b:", self.get_door(), ",", self.get_choice())
            self.check_win()

        print("Wins:", self.win_count, "/", self.total)
        print("Losses:", self.lose_count, "/", self.total)
    
    @staticmethod
    def auto(method=0, trials=100):
        g = GameShow()
        g.autoplay(method, trials)
        
    @staticmethod
    def game():
        g = GameShow()
        g.play()


# print("No Change")
# g = GameShow()
# g.autoplay(0, 1000000)
# print("Always Change")
# g = GameShow()
# g.autoplay(1, 1000000)
# print("Randomly Change")
# g = GameShow()
# g.autoplay(2, 1000000)

# g = GameShow()
# g.play()
