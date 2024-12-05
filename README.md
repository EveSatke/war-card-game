# War Card Game

## Requirements

### Gameplay Mechanics

- Implement the basic rules of the classic War card game:
  - Players split the deck evenly at the start of the game
  - Each player reveals the top card of their deck
  - The player with the higher card value wins the round and collects both cards
  - In case of a tie, initiate a "war" where players place additional 3 cards face down and then compare another card
  - The game ends when one player collects all the cards or a set number of rounds are played

### Deck and Card Management

- Use a standard 52-card deck (no jokers)
- Ensure that the deck is shuffled at the beginning of the game

### Players

- Support two players:
  - Player 1 (User-controlled)
  - Player 2 (Automated)

### Game Modes

- Include a "Quick Mode" where the game ends after a set number of rounds, showing the player with the most cards as the winner
- Optionally, allow players to play until one person collects all the cards

### Scoring

- Keep track of the number of cards each player holds
- Display the current score after each round

### User Interaction

- Provide a simple text-based interface for the game
- Add a delay between actions to make it more readable
- Let players start a new game, see round outcomes, and check the current score

### Randomization

- Randomly shuffle the deck at the start to ensure fairness

### Error Handling

- Handle invalid inputs
