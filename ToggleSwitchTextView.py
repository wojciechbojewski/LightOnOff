from ToggleSwitch import ToggleSwitch


class ToggleSwitchTextView:
    def __init__(self, ts: ToggleSwitch):
        self.ts = ts

    def view(self):
        if self.ts.state:
            print(f"ToggleSwitch is: on")
        else:
            print(f"ToggleSwitch is: off")
