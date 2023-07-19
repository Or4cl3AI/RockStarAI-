```python
import random
from RockStarAI.avatar import currentUser
from RockStarAI.game_logic import currentGame

concertStatus = {
    "venue": "",
    "fans": 0,
    "performance": 0,
    "success": False
}

def headlineConcert():
    if currentUser["skill_level"] < 5:
        print("You need to be at least level 5 to headline a concert.")
        return

    concertStatus["venue"] = random.choice(currentGame["venues"])
    concertStatus["fans"] = currentUser["fans"]
    concertStatus["performance"] = currentUser["skill_level"] * random.randint(1, 10)

    if concertStatus["performance"] > 50:
        concertStatus["success"] = True
        currentUser["fans"] += concertStatus["performance"]
        print(f"Concert was a success! You gained {concertStatus['performance']} fans.")
    else:
        print("Concert was not a success. Better luck next time.")

    return concertStatus
```