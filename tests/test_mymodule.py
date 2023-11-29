import unittest
from mymodule import MyModule


class TestMyModule(unittest.TestCase):

    def test_greeting(self):
        self.assertEqual(MyModule.greeting("John"), "Hello, John")


if __name__ == '__main__':
    unittest.main()
