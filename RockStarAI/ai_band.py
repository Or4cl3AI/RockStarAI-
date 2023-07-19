```python
import random
from RockStarAI.avatar import currentUser
from RockStarAI.game_logic import currentGame

class AIBand:
    def __init__(self):
        self.performance_data = {
            'guitar': 0,
            'bass': 0,
            'drums': 0,
            'keyboard': 0,
            'vocals': 0
        }

    def perform(self):
        for instrument in self.performance_data:
            self.performance_data[instrument] = random.randint(50, 100)

    def react_to_user_performance(self):
        user_performance = currentUser['skill_level']
        for instrument in self.performance_data:
            if user_performance > 70:
                self.performance_data[instrument] += 10
            elif user_performance < 30:
                self.performance_data[instrument] -= 10

    def get_performance_data(self):
        return self.performance_data

aiBand = AIBand()

def performWithAIBand():
    aiBand.perform()
    aiBand.react_to_user_performance()
    currentGame['ai_band_performance'] = aiBand.get_performance_data()
```