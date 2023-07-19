```python
import avatar
import instruments
import unlockables
import ai_band
import multiplayer
import song_editor
import gear
import challenges
import concert
import tutorial
import contribution_guidelines
import license

class RockStarAI:
    def __init__(self):
        self.currentUser = None
        self.currentGame = None
        self.availableInstruments = instruments.Instruments()
        self.availableUnlockables = unlockables.Unlockables()
        self.aiBand = ai_band.AIBand()
        self.multiplayerOpponents = multiplayer.Multiplayer()
        self.customSongs = song_editor.SongEditor()
        self.collectedGear = gear.Gear()
        self.dailyChallenges = challenges.Challenges()
        self.concertStatus = concert.Concert()
        self.tutorialProgress = tutorial.Tutorial()
        self.contributionStatus = contribution_guidelines.ContributionGuidelines()
        self.licenseDetails = license.License()

    def createAvatar(self):
        self.currentUser = avatar.createAvatar()

    def playInstrument(self):
        instruments.playInstrument(self.currentUser)

    def unlockItem(self):
        unlockables.unlockItem(self.currentUser)

    def performWithAIBand(self):
        ai_band.performWithAIBand(self.currentUser)

    def competeInMultiplayer(self):
        multiplayer.competeInMultiplayer(self.currentUser)

    def editSong(self):
        song_editor.editSong(self.currentUser)

    def collectGear(self):
        gear.collectGear(self.currentUser)

    def upgradeEquipment(self):
        gear.upgradeEquipment(self.currentUser)

    def takeChallenge(self):
        challenges.takeChallenge(self.currentUser)

    def headlineConcert(self):
        concert.headlineConcert(self.currentUser)

    def startTutorial(self):
        tutorial.startTutorial(self.currentUser)

    def contributeToProject(self):
        contribution_guidelines.contributeToProject(self.currentUser)

if __name__ == "__main__":
    game = RockStarAI()
    game.createAvatar()
    game.startTutorial()
```
