```python
import random
from RockStarAI.avatar import createAvatar
from RockStarAI.instruments import playInstrument
from RockStarAI.unlockables import unlockItem
from RockStarAI.ai_band import performWithAIBand
from RockStarAI.multiplayer import competeInMultiplayer
from RockStarAI.song_editor import editSong
from RockStarAI.gear import collectGear, upgradeEquipment
from RockStarAI.challenges import takeChallenge
from RockStarAI.concert import headlineConcert
from RockStarAI.tutorial import startTutorial

class GameLogic:
    def __init__(self, currentUser, currentGame):
        self.currentUser = currentUser
        self.currentGame = currentGame

    def startGame(self):
        startTutorial(self.currentUser, self.currentGame)

    def playRound(self):
        song = random.choice(self.currentGame.availableSongs)
        score = playInstrument(self.currentUser, song)
        fansGained = score // 100
        self.currentUser.fans += fansGained
        if score >= 500:
            unlockItem(self.currentUser, self.currentGame)
        performWithAIBand(self.currentUser, self.currentGame)
        competeInMultiplayer(self.currentUser, self.currentGame)
        editSong(self.currentUser)
        collectGear(self.currentUser, self.currentGame)
        upgradeEquipment(self.currentUser)
        takeChallenge(self.currentUser, self.currentGame)
        headlineConcert(self.currentUser, self.currentGame)

    def endGame(self):
        if self.currentUser.fans >= 10000:
            print("Congratulations! You're a rockstar legend!")
        else:
            print("Keep practicing and you'll be a rockstar legend in no time!")
```