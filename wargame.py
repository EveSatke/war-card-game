from player import Player
from deck import Deck

class WarGame:
    def __init__(self):
        self.main_deck = Deck()
        self.main_deck.shuffle_deck()
        self.player_1 = Player("Player 1")
        self.player_2 = Player("Computer")

    def deal_cards(self):
        self.player_1.cards = self.main_deck.cards[:26]
        self.player_2.cards = self.main_deck.cards[26:]

    def __repr__(self):
        return f"Player 1 cards: {len(self.player_1.cards)}\nPlayer 2 cards: {len(self.player_1.cards)}"
