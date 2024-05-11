import unittest
from ToggleSwitch import ToggleSwitch


class TestToggleSwitch(unittest.TestCase):
    def test_NewSwitch_IsDown(self):
        toggle = ToggleSwitch()
        self.assertEqual(True, toggle.isDown())

    def test_AfterOneSwitch_IsUp(self):
        toggle = ToggleSwitch()
        toggle.switch()
        self.assertEqual(False, toggle.isDown())
