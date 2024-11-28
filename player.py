class Player:
   def __init__(self, name):
    self.name = name
    self.cards = []

    def play_card(self):
        if self.cards:
            return self.cards.pop(0)
        return None