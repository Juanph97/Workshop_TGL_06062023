# Write a Python function called is_palindrome that checks if a given word is a
# palindrome. The function should have proper error handling and be tested with
# unittest.

import unittest
from function import reverse_string

def is_palindrome(palabra):
    palabra = palabra.lower().replace(" ", "")
    reverse = reverse_string(palabra)
    print (reverse)
    return palabra == reverse

class TestIsPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("son robos o sobornos"))
        self.assertTrue(is_palindrome("Ojo rojo"))
        self.assertFalse(is_palindrome("Tog gun lab"))
        self.assertFalse(is_palindrome("software"))
        self.assertTrue(is_palindrome("Amo la paloma"))

        

if __name__ == '__main__':
    unittest.main()