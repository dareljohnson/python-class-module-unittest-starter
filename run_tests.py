import unittest
import xmlrunner
from colorama import init, Fore

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add tests to the test suite
    suite.addTests(loader.discover('./tests', pattern='test_*.py'))

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    result = runner.run(suite)
    if result.wasSuccessful():
        print(Fore.GREEN + 'All tests passed!' + Fore.RESET)
    else:
        print(Fore.RED + 'Some tests failed.' + Fore.RESET)