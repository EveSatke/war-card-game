from player import Player
from deck import Deck
from card import Card

class WarGame:
    def __init__(self):
        self.main_deck = Deck()
        self.main_deck.shuffle_deck()
        self.player_1 = Player("Player 1")
        self.player_2 = Player("Computer")
        self.round_count = 0
        self.max_rounds = 100 # change for user input

    def deal_cards(self):
        self.player_1.cards = self.main_deck.cards[:26]
        self.player_2.cards = self.main_deck.cards[26:]

    def play_round(self):
        self.round_count += 1
        
        player_1_card = self.player_1.play_card()
        print(f"Player drew {player_1_card}")
        player_2_card = self.player_2.play_card()
        print(f"CPU drew {player_2_card}")
        
        comparison = player_1_card.compare_value(player_2_card)
        if comparison == 0:
            # war
            ...
        elif comparison > 0:
            self.round_outcome(player_1_card, player_2_card, self.player_1)
        else:
            self.round_outcome(player_1_card, player_2_card, self.player_2)

    def game_loop(self):
        while True:
            if self.round_count == self.max_rounds:
                break
            self.play_round()
            print(self)
    
    def round_outcome(self, player_cards, computer_cards, winner):
        winner.cards.append(player_cards)
        winner.cards.append(computer_cards)



    def __repr__(self):
        return f"Player 1 cards: {len(self.player_1.cards)}\nPlayer 2 cards: {len(self.player_2.cards)}\n"
