

class Card:
    def __init__(self, decide):
        self.color = decide[0]
        self.symbol = set_symbol()
        self.shading = set_shading()
        self.number = len(decide[1])

    def set_shading():
        if ord(decide[1][0]) < 65:
            self.shading = "symbol"
        elif ord(decide[1][0]) < 97:
            self.shading = "upper"
        else:
            self.shading = "lower"

    def set_symbol():
        a_sym = "aA@"
        s_sym = "sS$"

        if decide[1][0] in a_sym:
            self.symbol = "a"
        elif decide[1][0] in s_sym:
            self.symbol = "s"
        else:
            self.symbol = "h"

deck = []

def readCards():
    n = int(raw_input())
    for i in xrange(n):
        data = raw_input().split(" ")
        card = Card(data)
        deck.append(card)

def is_valid_set(cards):
    for prop in ['number', 'symbol', 'shade', 'color']:
        uniques = set(map((lambda c: getattr(c, prop)), cards))
        if len(uniques) == 2:
            return False
    return True
