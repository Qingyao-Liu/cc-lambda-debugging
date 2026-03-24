import unittest
from lambda_function2 import lambda_handler

class TestLambdaFunction2(unittest.TestCase):
    def test_alpha_translation(self):
        result = lambda_handler({"word": "alpha"})
        self.assertEqual(result['body'], "AlphalphAlpha")
    
    def test_alpha_return_object(self):
        result = lambda_handler({"word": "alpha"})
        self.assertEqual(result, {"statusCode": 200, "body": "AlphalphAlpha"})

    def test_harlem_conversion(self):
        result = lambda_handler({"word": "harlem"})
        self.assertEqual(result['body'], "hAlpharlEchom")
    
    def test_carbon_conversion(self):
        result = lambda_handler({"word": "carbon"})
        self.assertEqual(result['body'], "cAlpharbOscarn")
    
    def test_cicada_conversion(self):
        result = lambda_handler({"word": "cicada"})
        self.assertEqual(result['body'], "cIndiacAlphadAlpha")

    def test_sticks_conversion(self):
        result = lambda_handler({"word": "sticks"})
        self.assertEqual(result['body'], "stIndiacks")
    
    def test_potato_conversion(self):
        result = lambda_handler({"word": "potato"})
        self.assertEqual(result['body'], "pOscartAlphatOscar")
    
    def test_singer_conversion(self):
        result = lambda_handler({"word": "singer"})
        self.assertEqual(result['body'], "sIndiangEchor")
    
    def test_buoyancy_conversion(self):
        result = lambda_handler({"word": "buoyancy"})
        self.assertEqual(result['body'], "bUniformOscarYankeeAlphancYankee")

    def test_cookie_conversion(self):
        result = lambda_handler({"word": "cookie"})
        self.assertEqual(result['body'], "cOscarOscarkIndiaEcho")
    

if __name__ == '__main__':
    unittest.main()