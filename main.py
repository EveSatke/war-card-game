from wargame import WarGame

def main():
    game = WarGame()
    game.welcome_message()
    game.deal_cards()
    game.game_loop()

if __name__ == "__main__":
    main()
