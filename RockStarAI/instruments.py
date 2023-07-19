```python
class Instrument:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

class Guitar(Instrument):
    def __init__(self):
        super().__init__("Guitar", "Intermediate")

class Bass(Instrument):
    def __init__(self):
        super().__init__("Bass", "Beginner")

class Drums(Instrument):
    def __init__(self):
        super().__init__("Drums", "Advanced")

class Keyboard(Instrument):
    def __init__(self):
        super().__init__("Keyboard", "Intermediate")

class Vocals(Instrument):
    def __init__(self):
        super().__init__("Vocals", "Beginner")

availableInstruments = [Guitar(), Bass(), Drums(), Keyboard(), Vocals()]

def playInstrument(user, instrument):
    if instrument not in availableInstruments:
        return "Invalid instrument"
    else:
        user.currentInstrument = instrument
        return "Now playing " + instrument.name
```