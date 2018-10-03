import unittest
import employee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.em = employee.Employee('derek', 'yuan', 5000)
    def test_give_default_raise(self):
        salary = self.em.give_raise()
        self.assertEqual(salary, 10000)
    def test_give_custom_raise(self):
        salary = self.em.give_raise(10000)
        self.assertEqual(salary, 15000)

unittest.main()

