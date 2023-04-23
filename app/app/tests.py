"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc 

class CalcTestCase(SimpleTestCase):
    """Test the calc module. """

    def test_add_numbers(self):
        """Testing add number agains"""
        res = calc.add(5,6)
        self.assertEqual(res,11)

    def test_sunstract_numbers(self):
        """Testing sunstract numbers"""
        res = calc.substract(10,15)

        self.assertEqual(res,5)