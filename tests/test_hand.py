import unittest

from hand import *

test_hands = [
    ( 'AC QD JH 4C 2C', HIGHCARD,      'ace-high'                       ),
    ( 'AC AD 8H 7C TC', PAIR,          'pair of aces'                   ),
    ( 'AC AD 8H 7C 7S', TWOPAIR,       'two pair (aces and sevens)'     ),
    ( '8S 8D 8H 7C TC', SET,           'three of a kind (eights)'       ),
    ( '8C 7D 6H 5C 4C', STRAIGHT,      'eight-high straight'            ),
    ( 'AC 2D 3H 4C 5C', STRAIGHT,      'five-high straight'             ),
    ( 'AC JD KH TC QC', STRAIGHT,      'ace-high straight'              ),
    ( '8C 6C 5C QC JC', FLUSH,         'queen-high flush'               ),
    ( '8C 8D 8H 6D 6H', FULLHOUSE,     'full house (eights over sixes)' ),
    ( 'QC QD QH QS 6H', QUADS,         'four of a kind (queens)'        ),
    ( 'AH 4H 2H 3H 5H', STRAIGHTFLUSH, 'five-high straight flush'       ),
    ( 'AC JC KC TC QC', STRAIGHTFLUSH, 'royal flush'                    ),
    ( "AH 6D 2H 2S 2C", SET,           'three of a kind (twos)'         ),
    ( "QS JS 9S 7S 3S", FLUSH,         'queen-high flush'               ),
    ( "KC QC 8C 7C 5C", FLUSH,         'king-high flush'                ),
]

FIRST, SECOND, SPLIT = range(3)


class HandTestCase(unittest.TestCase):
    """Tests the hand module"""

    def runTest(self):
        self.test_hands()
        self.test_invalid_hand_string_rep()
        self.test_random_hand()
        self.test_hand_comparisons()
        self.test_internal_analysis_string()

    def test_hands(self):
        for entry in test_hands:
            card_str, type, desc = entry
            h = Hand.from_str(card_str)
            self.assertEquals(str(h).upper(), card_str,   msg = '%s: %s expected %s' % (card_str, str(h), card_str))
            self.assertEquals(h.get_type(), type, msg='%s: %s expected %s' % (card_str, TYPE_NAMES[h.get_type()], TYPE_NAMES[type]))
            self.assertEquals(h.describe(), desc, msg='%s: %s expected %s' % (card_str, h.describe(), desc))

    def test_invalid_hand_string_rep(self):
        self.assertRaises(CardFormatException, Hand.from_str, 'hi there')
        self.assertRaises(HandFormatException, Hand.from_str, 'AS QD')     # not enough cards

    def test_random_hand(self):
        h = Hand.random()
        self.assertTrue(len(h.cards) == 5)

    def _winner(self, s1, s2):
        h1, h2 = Hand.from_str(s1), Hand.from_str(s2)
        if h1 > h2: return FIRST
        if h1 < h2: return SECOND
        return SPLIT

    def test_hand_comparisons(self):
        self.assertEquals(self._winner('AC QD JH 4C 2C', 'QD TC 4H 6S 9D'), FIRST)
        self.assertEquals(self._winner('AC QD JH 4C 2C', 'AD TC 4H 6S 9D'), FIRST)  # test kickers
        self.assertEquals(self._winner('AC QD JH 4C 2C', 'AD 8C QH JS 9D'), SECOND) # test kickers
        self.assertEquals(self._winner('AC QD JH 4C 2C', 'AD TC 4H AS 9D'), SECOND)
        self.assertEquals(self._winner('2C 2D 4H 4C 8C', '2C 2D 4H 4C 8C'), SPLIT)
        self.assertEquals(self._winner('2C 2D 4H 4C 9C', '2C 2D 4H 4C 8C'), FIRST)  # test kickers
        self.assertEquals(self._winner('AC JC KC TC QC', 'AC QD JH 4C 2C'), FIRST)  # royal flush beats everything
        self.assertEquals(self._winner('AC JC KC TC QC', 'AC AD 8H 7C TC'), FIRST)
        self.assertEquals(self._winner('AC JC KC TC QC', 'AC AD 8H 7C 7S'), FIRST)
        self.assertEquals(self._winner('AC JC KC TC QC', '8C 8D 8H 7C TC'), FIRST)
        self.assertEquals(self._winner('AC JC KC TC QC', '8C 7D 6H 5C 4C'), FIRST)
        self.assertEquals(self._winner('AC JC KC TC QC', 'AC 2D 3H 4C 5C'), FIRST)
        self.assertEquals(self._winner('AC JC KC TC QC', 'AC JD KH TC QC'), FIRST)
        self.assertEquals(self._winner('AC JC KC TC QC', '8C 6C 5C QC JC'), FIRST)
        self.assertEquals(self._winner('AC JC KC TC QC', '8C 8D 8H 6D 6H'), FIRST)
        self.assertEquals(self._winner('AC JC KC TC QC', 'QC QD QH QS 6H'), FIRST)
        self.assertEquals(self._winner('AC JC KC TC QC', 'AH 4H 2H 3H 5H'), FIRST)
        self.assertEquals(self._winner('AC JC KC TC QC', 'AC JC KC TC QC'), SPLIT)
        self.assertEquals(self._winner('9C 8D 7H 6C 5C', '8C 7D 6H 5C 4C'), FIRST)  # high card in straights win
        self.assertEquals(self._winner('9C 8C 7C 6C 5C', '8C 7C 6C 5C 4C'), FIRST)  # high card in straight flushes win
        self.assertEquals(self._winner('JC JS TD TH TC', 'QC QD QH QS 6H'), SECOND) # 4-kind beats full house
        self.assertEquals(self._winner('JC JS JD JH TC', 'QC QD QH QS 6H'), SECOND) # higher rank in 4 of a kind wins
        self.assertEquals(self._winner('AC AS AD 6H 6C', 'QC QD QH TS TH'), FIRST)  # higher rank in Fh wins
        self.assertEquals(self._winner('AC AS AD 6H 6C', 'AC AD AH TS TH'), SECOND) # higher rank in Fh wins
        self.assertEquals(self._winner('AC AS AD 6H 6C', 'AC AD AH 6S 6H'), SPLIT)
        self.assertEquals(self._winner('6C TC QC 2C 9C', 'KH 4H 9H JH 8H'), SECOND) # high card in flush wins

    def test_internal_analysis_string(self):
        h = Hand.random()
        s = h._analysis_to_str()
        self.assertTrue(s is not None)
