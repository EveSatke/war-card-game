from card import Card
import random
from colorama import Fore

class Deck:
    SUITS = [f"{Fore.RED}♥️", f"{Fore.BLACK}♠️", f"{Fore.RED}♦️", f"{Fore.BLACK}♣️"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.create_deck()

    def create_deck(self):
        self.cards = []

        for suit in self.SUITS:
            for rank in Deck.RANKS:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        return self.cards.__str__()
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
