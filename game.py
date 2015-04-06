class Card:
    def __init__(self, decide):
        self.color = decide[0]
        self.symbol = self.set_symbol(decide)
        self.shading = self.set_shading(decide)
        self.number = len(decide[1])
        self.output = decide

    def set_shading(self, decide):
        if ord(decide[1][0]) < 65:
            return "symbol"
        elif ord(decide[1][0]) < 97:
            return "upper"
        else:
            return "lower"

    def set_symbol(self, decide):
        a_sym = "aA@"
        s_sym = "sS$"

        if decide[1][0] in a_sym:
            return "a"
        elif decide[1][0] in s_sym:
            return "s"
        else:
            return "h"

    def __str__(self):
        return ' '.join(self.output)

    def __repr__(self):
        return str(self)

class ThreeCard:
    def __init__(self, a, b, c):
        self.cards = [a, b, c]

    def is_valid_set(self):
        if len(set(self.cards)) != len(self.cards):
            return False
        for prop in ['number', 'symbol', 'shading', 'color']:
            uniques = set(map((lambda c: getattr(c, prop)), self.cards))
            if len(uniques) == 2:
                return False
        return True

    def conflicts_with(self, other):
        return len(set(self.cards) & set(other.cards)) != 0

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self)

class SetTree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def insert(self, candidate):
        if self.value.conflicts_with(candidate):
            return

        already_has_candidate = False
        for child in self.children:
            child.insert(candidate)
            if child.value == candidate:
                already_has_candidate = True

        if not already_has_candidate:
            self.children.append(SetTree(candidate))

    def height(self):
        return len(self.longest_path())

    def longest_path(self):
        result = [self.value]
        for child in self.children:
            subpath = child.longest_path()
            if len(subpath) >= len(result):
                result = [self.value] + subpath
        return result

    def __str__(self):
        return '<' + str(self.value) + ' ' + str(self.children) + '>'

    def __repr__(self):
        return str(self)

deck = []


def readCards():
    n = int(raw_input())
    for i in xrange(n):
        data = raw_input().strip().split(" ")
        card = Card(data)
        deck.append(card)
    return n

if __name__ == "__main__":
    n = readCards()
    allValidSets = []

    for i in xrange(n-2):
        for j in xrange(i, n-1):
            for k in xrange(j, n):
                c3 = ThreeCard(deck[i], deck[j], deck[k])
                if c3.is_valid_set():
                    allValidSets.append(c3)
    print len(allValidSets)

    best_tree = SetTree(None)
    for root in allValidSets:
        tree = SetTree(root)
        for candidate in allValidSets:
            tree.insert(candidate)
        if tree.height() > best_tree.height():
            best_tree = tree

    print best_tree.height()

    longest_path = best_tree.longest_path()
    for three_set in longest_path:
        print
        for card in three_set.cards:
            print card
