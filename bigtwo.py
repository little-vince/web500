"""Purpose is to test the cardlib library before extending it
to the 500 game."""


import cardlib 

class BigTwoDeck(cardlib.Pile):
    """A deck for Big 2"""

    def __init__(self):
        cardlib.Pile.__init__(self)
        values = list(range(3, 11))
        for s in cardlib.suits:
            for v in values:
                self.add(cardlib.StdCard(v, s))
            self.add(cardlib.SpcCard(11, s, "Jack of %s" % s.name))
            self.add(cardlib.SpcCard(12, s, "Queen of %s" % s.name))
            self.add(cardlib.SpcCard(13, s, "King of %s" % s.name))
            self.add(cardlib.SpcCard(14, s, "Ace of %s" % s.name))
            self.add(cardlib.SpcCard(15, s, "2 of %s" % s.name))
        cardlib.diamond.mag = 0
        cardlib.club.mag = 1
        cardlib.heart.mag = 2
        cardlib.spade.mag = 3

    def sort(self):
        self.deck.sort(key=lambda card: 10**card.value + card.suit.mag)

