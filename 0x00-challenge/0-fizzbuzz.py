#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuz)"."""
    import sys


if len(sys.argv) != 2:
    sys.exit(1)
if not sys.argv[1].isdigit():
    sys.exit(1)
if int(sys.argv[1]) < 1:
    sys.exit(1)

for i in range(1, int(sys.argv[1]) + 1):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if not output:
        output = i
    print(output, end=" ")
print()
