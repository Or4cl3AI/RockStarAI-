```python
class Unlockable:
    def __init__(self, name, type, description, unlock_condition):
        self.name = name
        self.type = type
        self.description = description
        self.unlock_condition = unlock_condition
        self.is_unlocked = False

    def check_unlock(self, user):
        if eval(self.unlock_condition):
            self.is_unlocked = True
            user.availableUnlockables.append(self)
            return "UnlockSuccess"
        return "UnlockFailed"

availableUnlockables = [
    Unlockable("Leather Jacket", "clothes", "A cool leather jacket for your avatar.", "user.fan_count >= 1000"),
    Unlockable("Fender Stratocaster", "instrument", "A classic guitar for your rock performances.", "user.skill_level['guitar'] >= 5"),
    Unlockable("Madison Square Garden", "venue", "A legendary venue for your concerts.", "user.concert_count >= 10"),
    Unlockable("Bohemian Rhapsody", "bonus song", "Unlock this Queen classic to play in the game.", "user.song_count >= 50"),
    # Add more unlockables as needed
]

def unlockItem(user, unlockable_name):
    for unlockable in availableUnlockables:
        if unlockable.name == unlockable_name:
            return unlockable.check_unlock(user)
    return "UnlockableNotFound"
```