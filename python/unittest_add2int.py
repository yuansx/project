import unittest
from unittest_func_class import add2int
import unittest_func_class as func

class FuncClassTestCase(unittest.TestCase):
    def test_add2int(self):
        sum = add2int(1, 2)
        self.assertEqual(sum, 3)

    def test_city_country(self):
        res = func.cityCountry('shenzhen', 'China')
        self.assertNotEqual(res, 'Shenzhen,China')

    def test_positive_number(self):
        self.assertTrue(func.isPositiveNumber(1))
    
    def test_inpositive_number(self):
        self.assertFalse(func.isPositiveNumber(-1))

unittest.main()

