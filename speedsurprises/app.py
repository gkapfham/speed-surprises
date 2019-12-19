#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys



def process_input(a, b, operation):

   """Perform operation on *a* and *b* depending on input provided.

   :param a: integer value

   :param b: integer value

   """

   if operation == "add":

       return a + b

   if operation == "subtract":

       return a - b

   if operation == "multiple":

       return a * b

   if operation == "divide":

       if b == 0:

           return "Invalid Input"

       return a / b



if __name__ == "__main__":

   "Run as a script"

   print(process_input(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]))
