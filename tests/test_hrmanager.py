import unittest
from hrmanager import HRManager


class TestHRManager(unittest.TestCase):

    def test_class_type(self):
        # Create an instance of the class
        hrmanager = HRManager()
        self.assertEqual(type(hrmanager), HRManager)

    def test_greet_employees(self):
        employees = [{"name": "John"}, {"name": "Alice"}]
        greetings = HRManager.greet_employees(employees)
        self.assertEqual(greetings, 2)

    def test_that_employee_list_is_empty(self):
        employees = []
        greetings = HRManager.greet_employees(employees)
        self.assertEqual(greetings, 0)

    def test_that_employee_list_has_bad_data(self):
        employees = [{"name": "John"}, {"age": 36}]
        greetings = HRManager.greet_employees(employees)
        self.assertEqual(greetings, 1)


if __name__ == '__main__':
    unittest.main()
