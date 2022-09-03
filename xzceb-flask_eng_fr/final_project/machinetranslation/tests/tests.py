import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def test1(self): 
        #self.assertEqual(english_to_french(""), "") # null test.
        self.assertEqual(english_to_french("Hello"), "Bonjour")  # test for the translation of the world 'Hello' and 'Bonjour'.

class TestF2E(unittest.TestCase): 
    def test1(self): 
        #self.assertEqual(french_to_english(""), "") # null test.
        self.assertEqual(french_to_english("Bonjour"), "Hello")  # test for the translation of the world 'Hello' and 'Bonjour'.

unittest.main()