import random
import sys

class Suit(object):
    """Suit of a card"""

    def __init__(self, name):
        self.name = name
        self.mag = 0 #used for defining order of ranks

spade = Suit("Spades")
club = Suit("Clubs")
diamond = Suit("Diamonds")
heart = Suit("Hearts")
suits = [spade, club, diamond, heart]

class Card(object):
    """Typical card that only has a label and a rank"""

    def __init__(self, label):
        self.value = None
        self.suit = None
        self.label = label

    def __str__(self):
        return self.label

class StdCard(Card):
    """A typical card containing a value and suit between 2 and 10"""

    def __init__(self, value, suit):
        Card.__init__(self, "%s of %s" % (value, suit.name))
        self.value = value
        self.suit = suit

class SpcCard(Card):
    """Any special card e.g. picture cards, joker etc"""

    def __init__(self, value, suit, name):
        Card.__init__(self, name)
        self.value = value
        self.suit = suit

class Pile(object):
    """A list of Card objects"""

    def __init__(self):
        self.deck = []

    def add(self, card):
        self.deck.append(card)

    def shuf(self):
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()

    def size(self):
        return len(self.deck)

    def traverse(self):
        for c in self.deck:
            print(c)

class StdDeck(Pile):
    """Standard 52 card deck"""

    def __init__(self):
        Pile.__init__(self)
        values = list(range(2, 11))
        for s in suits:
            for v in values:
                self.add(StdCard(v, s))
            self.add(SpcCard(11, s, "Jack of %s" % s.name))
            self.add(SpcCard(12, s, "Queen of %s" % s.name))
            self.add(SpcCard(13, s, "King of %s" % s.name))
            self.add(SpcCard(14, s, "Ace of %s" % s.name))

class FiveHundredDeck(Pile):
    """Generate a 4 player 500 deck"""

    def __init__(self):
        Pile.__init__(self)
        values = list(range(5, 14)) #generate cards 5-10
        values.append(1)
        for s in suits:
            for v in values:
                self.add(StdCard(v, s))
        self.add(StdCard(4, diamond))
        self.add(StdCard(4, heart))
        self.add(Card("Joker"))

class Game(object):
    """Set of abstract generic rules that should be overwritten
    depending on the game that should be played"""

    def __init__(self, *player):
        assert len(player) > 1 #don't play with yourself
        self.rules = rules

class Player(object):
    """Keeps track of the player's name and cards"""

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.is_dealer = False

    def give(self, card):
        self.hand.append(card)

