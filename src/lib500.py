import random

suits = ["spades", "clubs", "diamonds", "hearts"]


class Card(object):
    """Contains a card's value and suit."""
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


class Deck(object):
    """A list of Card objects"""
    deck = []

    def __init__(self, six_players):
        if six_players:
            print("6 players is currently unsupported.")
            return 1
        ranks = list(range(5, 11))
        ranks.extend([20, 21, 22, 23])
        for s in suits:
            for r in ranks:
                self.deck.append(Card(r, s))
        self.deck.extend([Card(4, "diamonds"), Card(4, "hearts"),
                         Card(99, None)])
        random.shuffle(self.deck)

    def deal(self, player, num):
        for i in range(num):
            player.give(self.draw())

    def draw(self):
        return self.deck.pop()

    def size(self):
        return len(self.deck)

    def show(self):
        for card in self.deck:
            print(card)


class Game(object):
    players = []
    kitty = []

    def __init__(self, players):
        deck = Deck(players == 6)
        for i in range(players):
            p = Player("Player %i" % (i + 1))
            deck.deal(p, 3)
            self.players.append(p)
        self.kitty.append(deck.draw())
        for p in self.players:
            deck.deal(p, 4)
        self.kitty.append(deck.draw())
        for p in self.players:
            deck.deal(p, 3)
        self.kitty.append(deck.draw())
        """print(deck.size())
        print(len(self.players))
        for p in self.players:
            print(p.name)
            for c in p.hand:
                print(c)"""


class Player(object):
    name = ""
    hand = []
    is_dealer = False

    def __init__(self, name):
        self.name = name

    def give(self, card):
        self.hand.append(card)
