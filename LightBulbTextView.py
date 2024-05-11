from LightBulb import LightBulb


class LightBulbTextView:
    def __init__(self, lb: LightBulb):
        self.lb = lb

    def view(self):
        if self.lb.state:
            print(f"LightBulb is: on")
        else:
            print(f"LightBulb is: off")
