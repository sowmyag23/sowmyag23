# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z3sCOw5xFrDa5BbCxolSaH67Rk86OdJQ
"""

def add_numbers(a, b):
  return a + b

if __name__ == "__main__":
  a = float(input("Enter the first number: "))
  b = float(input("Enter the second number: "))

  sum = add_numbers(a, b)
  print("The sum of {0} and {1} is {2}".format(a, b, sum))