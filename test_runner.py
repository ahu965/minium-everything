import unittest

from testcase.first_case import FirstTest

if __name__ == "__main__":
    loaded_suite = unittest.TestLoader().loadTestsFromTestCase(FirstTest)
    unittest.TextTestRunner().run(loaded_suite)
