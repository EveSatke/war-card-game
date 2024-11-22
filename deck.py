from card import Card
import random

class Deck:
    SUITS = ["Hearts", "Spades", "Diamonds", "Clubs"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.create_deck()

    def create_deck(self):
        self._cards = []

        for suit in Deck.SUITS:
            for rank in Deck.RANKS:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        return self._cards.__str__()
    
    def shuffle_deck(self):
        random.shuffle(self.cards)

    @property
    def deck(self):
        return self._cards
            
