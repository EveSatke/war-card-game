from card import Card

class Deck:
    def __init__(self):
        self.create_deck()

    def create_deck(self):
        self.deck = []
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))
