from typing import List
from LightBulb import LightBulb
from ToggleSwitch import ToggleSwitch


class Logic:
    def __init__(self, lb: LightBulb, ts: List[ToggleSwitch]):
        self.lightbulb = lb
        self.toggleswitch = ts

    def processing(self):
        shouldLightBeOn = not self.toggleswitch[0].isDown()
        if len(self.toggleswitch) > 1:
            for ts in self.toggleswitch[1:]:
                shouldLightBeOn ^= not ts.isDown()
        if shouldLightBeOn:
            self.lightbulb.on()
        else:
            self.lightbulb.off()
