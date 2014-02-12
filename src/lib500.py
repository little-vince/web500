class Card(object):
    value = None

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self._gen_label()

    def _gen_label(self):
        rank_dict = {20: "Jack", 21: "Queen", 21: "King", 21: "Ace"}
        if self.rank <= 10:
            self.label = ("%s of %s" % (self.rank, self.suit.capitalize()))
        else:
            self.label = ("%s of %s" % (rank_dict[self.rank], self.suit
                .capitalize()))
