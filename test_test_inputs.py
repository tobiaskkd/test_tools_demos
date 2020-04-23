import unittest, string
from random import randint
from test_inputs import TestInputs


class TestTestInputs(unittest.TestCase):

    # Instance of PasswordGenerator class with default values
    # length=10, characters=True, numbers=True, specialChar=True, uppercase=True, lowercase=True
    test_inputs = TestInputs()
    test_inputs.setup_method()

    def test_constructor(self):
        self.assertIsInstance(self.test_inputs, TestInputs)

    def test_test_inputs(self):
        for test_case in [''.join([string.ascii_letters[randint(0, len(string.ascii_letters)-1)] for i in range(randint(0, len(string.ascii_letters)-1))]) for i in range(10)]:
            print(test_case)
            self.assertTrue(self.test_inputs.test_inputs(test_case), True)

    test_inputs.teardown_method()

if __name__ == "__main__":
    unittest.main()