from unittest import *

import test_card
import test_hand

suite = TestSuite()
suite.addTest(test_card.CardTestCase())
suite.addTest(test_hand.HandTestCase())
TextTestRunner(verbosity=2).run(suite)
