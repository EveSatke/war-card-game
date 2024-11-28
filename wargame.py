from player import Player
from deck import Deck

class WarGame:
    def __init__(self):
        self.main_deck = Deck()
        self.main_deck.shuffle_deck()
        self.player_1 = Player("Player 1")
        self.player_2 = Player("Computer")
        self.round_count = 0

    def deal_cards(self):
        self.player_1.cards = self.main_deck.cards[:26]
        self.player_2.cards = self.main_deck.cards[26:]

    def play_round(self):
        self.round_count += 1
        
        player_1_card = self.player_1.play_card()
        player_2_card = self.player_2.play_card()



    def __repr__(self):
        return f"Player 1 cards: {self.player_1.cards}\nPlayer 2 cards: {self.player_2.cards}"
