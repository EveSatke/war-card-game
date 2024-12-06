class Card:

    RANKS = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 12,
        "A": 13,
    }

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def compare_value(self, other: "Card"):
        return Card.RANKS[self.rank] - Card.RANKS[other.rank]

    def __str__(self):
        return f"{self.rank} {self.suit}"

    def __repr__(self):
        return f"Rank= {self.rank} Suit= {self.suit}"
