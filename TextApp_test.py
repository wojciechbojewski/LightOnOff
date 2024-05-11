import io
import unittest
from unittest.mock import patch
from TextApp import run


def input_args():
    yield "show"
    yield "switch ts1"
    yield "show"
    yield "exit"


class TestTextApp(unittest.TestCase):
    @patch("builtins.input", side_effect=input_args())
    def test_ShowSwitchTS1ShowExit(self, mock_input):
        expected = (
            "ToggleSwitch is: off\n"
            "ToggleSwitch is: off\n"
            "ToggleSwitch is: off\n"
            "LightBulb is: off\n"
            "ToggleSwitch is: on\n"
            "ToggleSwitch is: off\n"
            "ToggleSwitch is: off\n"
            "LightBulb is: on\n"
        )

        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            run()
            result = fake_out.getvalue()
            self.assertEqual(expected, result)
