import unittest
from ToggleSwitch import ToggleSwitch
from LightBulb import LightBulb
from Logic import Logic


class TestLogic(unittest.TestCase):
    def test_OneSwitchScenario(self):
        ts1 = ToggleSwitch()
        lb1 = LightBulb()
        logic = Logic(lb1, [ts1])
        ts1.switch()
        logic.processing()
        self.assertEqual(True, lb1.state)

    def test_TwoSwitchesScenario(self):
        ts1 = ToggleSwitch()
        ts2 = ToggleSwitch()
        lb1 = LightBulb()
        logic = Logic(lb1, [ts1, ts2])
        ts1.switch()
        logic.processing()
        ts2.switch()
        logic.processing()
        self.assertEqual(False, lb1.state)

    def test_ThreeSwitchesScenario(self):
        ts1 = ToggleSwitch()
        ts2 = ToggleSwitch()
        ts3 = ToggleSwitch()
        lb1 = LightBulb()
        logic = Logic(lb1, [ts1, ts2, ts3])
        ts1.switch()
        logic.processing()
        ts2.switch()
        logic.processing()
        ts3.switch()
        logic.processing()
        self.assertEqual(True, lb1.state)
