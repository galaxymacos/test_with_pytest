# Run with the command "python -m unittest discover"
from unittest import TestCase


class TryTestCase(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    # def test_always_fails(self):
    #     self.assertTrue(False)
