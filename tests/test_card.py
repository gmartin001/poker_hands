import unittest

from card import *


class CardTestCase(unittest.TestCase):
    """Tests the card module"""

    def runTest(self):
        self.test_deck_init()
        self.test_from_str()
        self.test_invalid_from_str()
        self.test_cmp()
        self.test_to_str()
        self.test_to_long_str()

    def test_deck_init(self):
        deck = range(52)
        for i in range(52):
            c = Card(i)
            self.assertEquals(c.rank, i % 13)
            self.assertEquals(c.suit, i / 13)

    def test_from_str(self):
        ace_spades   = Card.from_str('AS')
        ten_clubs    = Card.from_str('TC')
        three_hearts = Card.from_str('3H')
        four_spades  = Card.from_str('4S')
        two_diamonds = Card.from_str('2D')

        self.assertEquals(ace_spades.suit, SPADES)
        self.assertEquals(ace_spades.rank, ACE)
        self.assertEquals(ten_clubs.suit, CLUBS)
        self.assertEquals(ten_clubs.rank, TEN)
        self.assertEquals(three_hearts.suit, HEARTS)
        self.assertEquals(three_hearts.rank, THREE)
        self.assertEquals(four_spades.suit, SPADES)
        self.assertEquals(four_spades.rank, FOUR)
        self.assertEquals(two_diamonds.suit, DIAMONDS)
        self.assertEquals(two_diamonds.rank, TWO)

    def test_invalid_from_str(self):
        self.assertRaises(CardFormatException, Card.from_str, '#$')
        self.assertRaises(CardFormatException, Card.from_str, 'A')    # not enough chars
        self.assertRaises(CardFormatException, Card.from_str, 'AX')   # bad suit
        self.assertRaises(CardFormatException, Card.from_str, 'ZS')   # bad rank

    def test_cmp(self):
        ace_spades   = Card.from_str('AS')
        ten_clubs    = Card.from_str('TC')
        three_hearts = Card.from_str('3H')
        four_spades  = Card.from_str('4S')
        two_diamonds = Card.from_str('2D')
        two_clubs    = Card.from_str('2C')

        self.assertTrue(ace_spades > two_diamonds)
        self.assertTrue(ace_spades > ten_clubs)
        self.assertTrue(ace_spades > three_hearts)
        self.assertTrue(ace_spades > four_spades)

        self.assertTrue(three_hearts < ace_spades)
        self.assertTrue(three_hearts < four_spades)

        self.assertEquals(two_diamonds, two_clubs)

    def test_to_str(self):
        for i in range(52):
            c = Card(i)
            self.assertEquals(str(c), RANK_ABBR[c.rank] + SUIT_ABBR[c.suit])

    def test_to_long_str(self):
        self.assertEquals(Card.from_str('AS').describe(long_fmt=True), "ace of spades")
        self.assertEquals(Card.from_str('TC').describe(long_fmt=True), "ten of clubs")
        self.assertEquals(Card.from_str('2D').describe(long_fmt=True), "two of diamonds")
        self.assertEquals(Card.from_str('QH').describe(long_fmt=True), "queen of hearts")
