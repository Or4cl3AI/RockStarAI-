```python
class Avatar:
    def __init__(self, name, look, instrument):
        self.name = name
        self.look = look
        self.instrument = instrument
        self.level = 1
        self.fans = 0

    def customize_look(self, new_look):
        self.look = new_look

    def change_instrument(self, new_instrument):
        self.instrument = new_instrument

    def level_up(self):
        self.level += 1

    def gain_fans(self, new_fans):
        self.fans += new_fans

def createAvatar(name, look, instrument):
    return Avatar(name, look, instrument)
```