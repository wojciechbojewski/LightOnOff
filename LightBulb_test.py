import unittest
from LightBulb import LightBulb


class TestLightBulb(unittest.TestCase):
    def test_NewLightBulb_StateFalse(self):
        lightBult = LightBulb()
        self.assertEqual(False, lightBult.state)

    def test_AfterLightOn_StateTrue(self):
        lightBulb = LightBulb()
        lightBulb.on()
        self.assertEqual(True, lightBulb.state)

    def test_AfterLightOff_StateFalse(self):
        lightBulb = LightBulb()
        lightBulb.off()
        self.assertEqual(False, lightBulb.state)
