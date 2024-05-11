import unittest
from unittest.mock import patch

from LightBulb import LightBulb
from LightBulbTextView import LightBulbTextView


class TestLightBulbTextView(unittest.TestCase):
    @patch("builtins.print")
    def test_PrintsOnOff(self, mock_print):
        lb = LightBulb()
        lbv = LightBulbTextView(lb)
        lb.on()
        lbv.view()
        lb.off()
        lbv.view()

        # Sprawdzanie, czy funkcja print została wywołana dwukrotnie
        self.assertEqual(mock_print.call_count, 2)

        # Sprawdzanie, czy funkcja print została wywołana z odpowiednimi argumentami
        expected_calls = [(("LightBulb is: on",), {}), (("LightBulb is: off",), {})]
        self.assertEqual(mock_print.call_args_list, expected_calls)
