# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:40:45 2015

@author: Lukas Gartmair
"""

import unittest


def add(a,b):
    return a+b

class MyTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,2),3)

def main():
    unittest.main()

if __name__ == '__main__':
    main()