#!/usr/bin/env python

# -*- coding: utf-8 -*-

import unittest

from speedsurprises.app import process_input



class TestApp(unittest.TestCase):

   """Test the mathematical operations app

   """

   def setUp(self):

       "This runs before the test cases are executed"

       self.a = 10

       self.b = 5

       self.c = 15


   def test_0010_add(self):

       "Test add operation"

       result = process_input(self.a, self.b, "add")

       self.assertEqual(result, 15)


   # def test_0010_sub(self):
   #
   #     "Test add operation"
   #
   #     result = process_input(self.a, self.b, "subtract")
   #
   #     self.assertEqual(result, 5)
   #
   #
   # def test_0015_add(self):
   #
   #     "Test add operation"
   #
   #     result = process_input(self.a, self.c, "add")
   #
   #     self.assertEqual(result, 25)



def suite():

   "Test suite"

   suite = unittest.TestSuite()

   suite.addTests(

       unittest.TestLoader().loadTestsFromTestCase(TestApp)

   )

   return suite



if __name__ == "__main__":

   unittest.TextTestRunner(verbosity=2).run(suite())
