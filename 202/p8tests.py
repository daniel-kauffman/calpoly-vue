# Name:         
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VIII
# Term:         Spring 2021

import re
import unittest

import pset8


def search(pattern: str, text: str) -> str:
    """
    Given a regular expression (pattern) and string (text) to search, return
    the substring found that conforms to the pattern.

    Do not modify this function.
    """
    return re.search(pattern, text).group()  # only use of |re| module




class TestParseTerm(unittest.TestCase):

    def test_parse_term_1(self):
        pattern = pset8.parse_term()
        self.assertEqual(search(pattern, "Sprint Fall '20"),
                         "Fall '20")




class TestParseTime(unittest.TestCase):

    def test_parse_time_1(self):
        pattern = pset8.parse_time()
        self.assertEqual(search(pattern, "123 12:01:59PM 123"),
                         "12:01:59PM")




class TestParseDate(unittest.TestCase):

    def test_parse_time_1(self):
        pattern = pset8.parse_date()
        self.assertEqual(search(pattern, "January February 1, 2020 2021"),
                         "February 1, 2020")




class TestParseName(unittest.TestCase):

    def test_parse_name_1(self):
        pattern = pset8.parse_name()
        self.assertEqual(search("Name: Samuel L. Jackson"),
                         "Samuel L. Jackson")




class TestParseMath(unittest.TestCase):

    def test_parse_math_1(self):
        pattern = pset8.parse_math()
        self.assertEqual(search("_ 12 + 34.5 _"),
                         "12 + 34.5")


if __name__ == "__main__":
    unittest.main()
