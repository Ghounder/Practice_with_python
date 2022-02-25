from cgitb import reset
import unittest
import is_prime
import palindrome


class Testprime(unittest.TestCase):

    def test_prime(self):
        self.assertEqual(is_prime.is_prime(78),False)
        self.assertEqual(is_prime.is_prime(11),True)
        self.assertEqual(is_prime.is_prime(72342342),False)
        self.assertEqual(is_prime.is_prime(658),False)
        self.assertEqual(is_prime.is_prime(8),False)
    
    def test_palindrome(self):
        self.assertEqual(palindrome.is_palindrome("ada"),True)
        self.assertEqual(palindrome.is_palindrome("adaaaada"),True)
        self.assertEqual(palindrome.is_palindrome("tree"),False)
        self.assertEqual(palindrome.is_palindrome("231132"),True)
        self.assertEqual(palindrome.is_palindrome("..."),True)
        self.assertEqual(palindrome.is_palindrome("AlA"),True)


if __name__ == "__main__":
    unittest.main()
