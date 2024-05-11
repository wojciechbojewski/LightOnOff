import unittest
from unittest.mock import patch

from ToggleSwitch import ToggleSwitch
from ToggleSwitchTextView import ToggleSwitchTextView


class TestToggleSwitchTextView(unittest.TestCase):
    @patch("builtins.print")
    def test_PrintsOnOff(self, mock_print):
        ts = ToggleSwitch()
        tsv = ToggleSwitchTextView(ts)
        ts.switch()
        tsv.view()
        ts.switch()
        tsv.view()

        # Sprawdzanie, czy funkcja print została wywołana dwukrotnie
        self.assertEqual(mock_print.call_count, 2)

        # Sprawdzanie, czy funkcja print została wywołana z odpowiednimi argumentami
        expected_calls = [
            (("ToggleSwitch is: on",), {}),
            (("ToggleSwitch is: off",), {}),
        ]
        self.assertEqual(mock_print.call_args_list, expected_calls)
