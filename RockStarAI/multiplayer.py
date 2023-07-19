```python
import random
from game_logic import calculate_score, update_game_state
from avatar import Avatar

class Multiplayer:
    def __init__(self):
        self.opponents = []

    def add_opponent(self, opponent):
        self.opponents.append(opponent)

    def remove_opponent(self, opponent):
        self.opponents.remove(opponent)

    def get_opponents(self):
        return self.opponents

    def compete(self, currentUser, song):
        opponent = random.choice(self.opponents)
        user_score = calculate_score(currentUser, song)
        opponent_score = calculate_score(opponent, song)

        if user_score > opponent_score:
            message = "Congratulations! You won the battle against " + opponent.name
            update_game_state(currentUser, "LevelUp")
        else:
            message = "Oh no! " + opponent.name + " won the battle. Better luck next time!"

        return message

multiplayer = Multiplayer()

def competeInMultiplayer(currentUser, song):
    return multiplayer.compete(currentUser, song)
```