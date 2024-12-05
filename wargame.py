from player import Player
from deck import Deck
from card import Card
import time
import colorama
from colorama import Fore, Style

class WarGame:
    def __init__(self):
        self.main_deck = Deck()
        self.main_deck.shuffle_deck()
        self.player_1 = Player("Player 1")
        self.player_2 = Player("Computer")
        self.round_count = 0
        colorama.init(autoreset=True)

    def welcome_message(self):
        print(
            f"\n{Style.BRIGHT}{Fore.GREEN}Welcome to War Card Game!\n"
            f"{Style.NORMAL}{Fore.YELLOW}Let's deal the cards...\n"
            )

    def deal_cards(self):
        self.player_1.cards = self.main_deck.cards[:26]
        self.player_2.cards = self.main_deck.cards[26:]

    def is_not_game_end(self):
        user_input = input("Press Enter to drew a card or 'end' to end the game...")
        if user_input == "end":
            return False
        return True
    
    def play_round(self):
        self.round_count += 1
        player_1_card = self.player_1.play_card()
        print(f"\nPlayer drew {player_1_card}")
        player_2_card = self.player_2.play_card()
        print(f"Computer drew {player_2_card}")
        
        round_cards = [player_1_card, player_2_card]
        
        comparison = player_1_card.compare_value(player_2_card)
        if comparison == 0:
            war_cards = self.handle_war()
            round_cards.extend(war_cards)
            war_card_1 = war_cards[-2]
            war_card_2 = war_cards[-1]
            comparison = war_card_1.compare_value(war_card_2)

        if comparison > 0:
            self.round_outcome(round_cards, self.player_1)
        else:
            self.round_outcome(round_cards, self.player_2)

    def game_loop(self):
        while True or self.player_1.cards or self.player_2.cards:
            if not self.is_not_game_end():
                break
            self.play_round()
            print(self)
        self.game_end_message()
    
    def round_outcome(self, round_cards, winner):
        time.sleep(1)
        print(f"\n{Fore.CYAN}{winner.name} won the round!")
        winner.cards.extend(round_cards)
        return winner

    def handle_war(self):
        print(
            "\n{Fore.RED}It's a war!\n"
            "Both players put 3 cards face down and then another card face up.\n"
        )
        war_cards = []
        for _ in range(3):
            war_card_1 = self.player_1.play_card()
            war_card_2 = self.player_2.play_card()
            war_cards.extend([war_card_1, war_card_2])
        
        # Draw the deciding card for the war
        war_card_1 = self.player_1.play_card()
        print(f"\nPlayer drew {war_card_1}")
        war_card_2 = self.player_2.play_card()
        print(f"Computer drew {war_card_2}")
        war_cards.extend([war_card_1, war_card_2])
        
        return war_cards

    def game_end_message(self):
        print("\nGame over!")
        if len(self.player_1.cards) > len(self.player_2.cards):
            print(f"\n{Fore.GREEN}Player won the game! Congratulations!\n")
        else:
            print(f"\n{Fore.RED}Sorry, computer won the game.\n")


    def __repr__(self):
        return f"\nPlayer cards: {len(self.player_1.cards)}\nComputer cards: {len(self.player_2.cards)}\n"
