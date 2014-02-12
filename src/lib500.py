import random

suits = ["spades", "clubs", "diamonds", "hearts"]


class Card(object):
    value = None
    label = None
    rank = None

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self._gen_label()

    def _gen_label(self):
        rank_dict = {
            20: "Jack",
            21: "Queen",
            22: "King",
            23: "Ace"
        }
        if self.rank <= 10:
            self.label = ("%s of %s" % (self.rank, self.suit.capitalize()))
        elif self.rank == 99:
            self.label = "Joker"
        else:
            self.label = ("%s of %s" % (rank_dict[self.rank],
                                        self.suit.capitalize()))

    def __str__(self):
        return self.label


def _gen_deck(six_players):
    if six_players:
        print("6 players is currently unsupported.")
        return 1
    ranks = list(range(5, 11))
    ranks.extend([20, 21, 22, 23])
    deck = []
    for s in suits:
        for r in ranks:
            deck.append(Card(r, s))
    deck.extend([Card(4, "diamonds"), Card(4, "hearts"), Card(99, None)])
    random.shuffle(deck)
