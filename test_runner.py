import unittest

from tests.rest_country import test_rest_country

class MyTestSuite(unittest.TestCase):
    def test_Issue(self):
        api_test = unittest.TestSuite() 
        api_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_rest_country.TestRestCountry), 
        ])

        runner1=unittest.TextTestRunner()
        runner1.run(api_test)

if __name__ == "__main__":
    unittest.main(exit=False)