```python
class Gear:
    def __init__(self, name, type, upgrade_level=0):
        self.name = name
        self.type = type
        self.upgrade_level = upgrade_level

    def upgrade(self):
        self.upgrade_level += 1
        return self.upgrade_level

class GearCollection:
    def __init__(self, user):
        self.user = user
        self.collection = []

    def collect_gear(self, gear):
        self.collection.append(gear)

    def upgrade_gear(self, gear_name):
        for gear in self.collection:
            if gear.name == gear_name:
                gear.upgrade()
                return True
        return False

def collectGear(user, gear):
    user.gear_collection.collect_gear(gear)

def upgradeEquipment(user, gear_name):
    success = user.gear_collection.upgrade_gear(gear_name)
    if success:
        message = f"UpgradeSuccess: {gear_name} has been upgraded!"
    else:
        message = f"UpgradeFailure: {gear_name} not found in your collection."
    return message
```