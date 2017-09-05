from hand import *


n = 100

if n < 0:
    n = 100

for i in range(n):
    h = Hand.random()
    h.cards.sort()
    h.cards.reverse()
    print '( "%s", %20s, "%s" )' % (str(h), TYPE_NAMES[h.get_type()], h.describe())
