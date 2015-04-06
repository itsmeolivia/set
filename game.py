class Card:
    def __init__(self, decide):
        self.color = decide[0]
        self.symbol = set_symbol(decide)
        self.shading = set_shading(decide)
        self.number = len(decide[1])
        self.output = decide

    def set_shading(self, decide):
        if ord(decide[1][0]) < 65:
            self.shading = "symbol"
        elif ord(decide[1][0]) < 97:
            self.shading = "upper"
        else:
            self.shading = "lower"

    def set_symbol(self, decide):
        a_sym = "aA@"
        s_sym = "sS$"

        if decide[1][0] in a_sym:
            self.symbol = "a"
        elif decide[1][0] in s_sym:
            self.symbol = "s"
        else:
            self.symbol = "h"


class ThreeCard:
    def __init__(self, a, b, c):
        self.cards = [a, b, c]

    def is_valid_set(self):
        for prop in ['number', 'symbol', 'shade', 'color']:
            uniques = set(map((lambda c: getattr(c, prop)), self.cards))
            if len(uniques) == 2:
                return False
        return True

deck = []

def readCards():
    n = int(raw_input())
    for i in xrange(n):
        data = raw_input().split(" ")
        card = Card(data)
        deck.append(card)
    return n

if __name__ == "__main__":
    n = readCards()
    allValidSets = []

    for i in xrange(n-2):
        for j in xrange(1, n-1):
            for k in xrange(2, n):
                c3 = ThreeCard(deck[i], deck[j], deck[k])
                if c3.is_valid_set():
                    allValidSets.append(c3)
    print len(allValidSets)


    print count_total
    print disjoint_total
