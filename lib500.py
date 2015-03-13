import random
import sys

suits = ["spades", "clubs", "diamonds", "hearts"]


class Card(object):
    """Contains a card's value and suit."""

    def __init__(self, rank, suit):
        self.value = None
        self.rank = rank
        self.suit = suit
        self.label = ""
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

    def __init__(self, player_count):
        if player_count != 4:
            print("%i players is currently unsupported." % player_count)
            sys.exit(1)
        self.deck = []
        ranks = list(range(5, 11))
        ranks.extend([20, 21, 22, 23])
        for s in suits:
            for r in ranks:
                self.deck.append(Card(r, s))
        self.deck.extend([Card(4, "diamonds"), Card(4, "hearts"),
                          Card(99, None)])
        random.shuffle(self.deck)

    def deal(self, player, num):
        for _ in range(num):
            player.give(self.draw())

    def draw(self):
        return self.deck.pop()

    def size(self):
        return len(self.deck)


class Game(object):
    """Mastermind that manages the Game"""

    def __init__(self, player_count):
        self.players = []
        self.kitty = []
        deck = Deck(player_count)
        for i in range(player_count):
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


class Player(object):
    """Keeps track of the player's name and cards"""

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.is_dealer = False

    def give(self, card):
        self.hand.append(card)