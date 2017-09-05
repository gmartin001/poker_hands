from hand import *


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = None
        self.wins = 0
        self.lose = 0

    def __str__(self):
        return '%s' % self.name

    def hand_set(self, hand_str):
        self.hand = Hand.from_str(hand_str)

    def hand_get(self):
        return self.hand

    def hand_describe(self):
        return self.hand.describe()

    def hand_get_type(self):
        return self.hand.get_type()

    def set_win(self,win):
        if win:
            self.wins += 1
        else:
            self.lose += 1

    def get_wins(self):
        return self.wins

    def get_lose(self):
        return self.lose
