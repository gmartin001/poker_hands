from player import *


class MatchedTypeAndRanksException(Exception):
    pass

class Game:
    """A two player game of 5 card poker. Cards are dealt to the two players from a file."""
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2

    def _determine_winner(self):
        hand1 = self.player1.hand_get()
        hand2 = self.player2.hand_get()
        outcome = hand1.compare(hand2)
        if outcome > 0:
            print 'Player 1 wins'
            self.player1.set_win(True)
            self.player2.set_win(False)
        elif outcome < 0:
            print 'Player 2 wins'
            self.player1.set_win(False)
            self.player2.set_win(True)
        else: # outcome = 0
            raise MatchedTypeAndRanksException('type and ranks match')
        print '\n'

    def play(self,file_to_open):
        file1 = open(file_to_open,'r')
        for line in file1:
            print line.strip('\n')
            seq = line.split()
            seq1 = seq[0:5]
            seq2 = seq[5:10]
            cards1 = ' '.join(seq1)
            cards2 = ' '.join(seq2)
            # print cards1
            # print cards2
            self.player1.hand_set(cards1)
            self.player2.hand_set(cards2)
            p1_desc = self.player1.hand_describe()
            p2_desc = self.player2.hand_describe()
            print p1_desc + ' ' + p2_desc
            self._determine_winner()
        print 'Player 1 wins: {0} Player 1 loses: {1}'.format(self.player1.get_wins(),self.player1.get_lose())
        print 'Player 2 wins: {0} Player 2 loses: {1}'.format(self.player2.get_wins(),self.player2.get_lose())

player_1 = Player('player1')
player_2 = Player('player2')
game = Game(player_1,player_2)
# file_name = 'p054_poker_test.txt'
file_name = 'p054_poker.txt'
game.play(file_name)
