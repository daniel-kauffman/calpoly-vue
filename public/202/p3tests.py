# Name:         
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set III
# Term:         Spring 2021

import unittest

import pset3
from pset3 import ListNode  # only allowed use of from ... import


class TestMul(unittest.TestCase):

    def test_mul_1(self):
        self.assertEqual(pset3.mul(-2, -3), 6)

    def test_mul_2(self):
        pass

    def test_mul_3(self):
        pass

    def test_mul_4(self):
        pass

    def test_mul_5(self):
        pass




class TestExp(unittest.TestCase):

    def test_exp_1(self):
        self.assertEqual(pset3.exp(-2, 3), -8)




class TestFac(unittest.TestCase):

    def test_fac_1(self):
        self.assertEqual(pset3.fac(5), 120)




class TestFibonacci(unittest.TestCase):

    def test_fibonacci_1(self):
        self.assertEqual(pset3.fibonacci(8, 0, 1), 13)




class TestMakeSubstring(unittest.TestCase):

    def test_make_substring_1(self):
        self.assertEqual(pset3.make_substring("COMPUTER", 0, 10, 3), "CPE")




class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome_1(self):
        self.assertEqual(pset3.is_palindrome("tacocat"), True)

    def test_is_palindrome_2(self):
        self.assertEqual(pset3.is_palindrome("palindrome"), False)




class TestSwapChars(unittest.TestCase):

    def test_swap_chars_1(self):
        self.assertEqual(pset3.swap_chars("AaBbCcD"), "aAbBcCD")




class TestLength(unittest.TestCase):

    def test_length_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset3.length(head), 3)




class TestFindMax(unittest.TestCase):

    def test_find_max_1(self):
        head = ListNode(2, ListNode(3, ListNode(4, ListNode(1, None))))
        self.assertEqual(pset3.find_max(head), 4)




class TestReverse(unittest.TestCase):

    def test_reverse_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset3.reverse(head, None),
                         ListNode(3, ListNode(2, ListNode(1, None))))




class TestNestingDollConstructor(unittest.TestCase):

    def test_nesting_doll_constructor_1(self):
        doll = pset3.NestingDoll(3)
        self.assertEqual(doll.inner.inner.inner, None)




class TestNestingDollEquals(unittest.TestCase):

    def test_nesting_doll_equals_1(self):
        self.assertEqual(pset3.NestingDoll(1), pset3.NestingDoll(1))

    def test_nesting_doll_equals_2(self):
        self.assertNotEqual(pset3.NestingDoll(1), pset3.NestingDoll(2))




class TestNestingDollString(unittest.TestCase):

    def test_nesting_doll_string_1(self):
        self.assertEqual(str(pset3.NestingDoll(3)), "((8))")


if __name__ == "__main__":
    unittest.main()
