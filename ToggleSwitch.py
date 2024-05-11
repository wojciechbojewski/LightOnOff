class ToggleSwitch:
    def __init__(self):
        self.state = False

    def isDown(self):
        return not self.state

    def switch(self):
        self.state = not self.state
