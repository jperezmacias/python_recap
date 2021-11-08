#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The goal of this script is to use the assert and add the try catch clauses.

__docformat__ = 'reStructuredText'
__all__ = [
    'getSum'
]

def getSum(X: int, Y: int) -> int:
    """ This function sums the two numbers and checks if they are between 1 and 40.
    :param X: a number.
    :type X: int
    :param Y: a number.
    :type Y: int
    :return result: the sum if the condition is met.
    :rtype result: int
    """
    try:
        temp1 = (X >= 1 & X <= 40)
        temp2 = (Y >= 1 & Y <= 40)

        assert ((temp1 & temp2) == 1, "Input does not meet requirements")
        result = X + Y

    except Exception as e:
        result = -1
        print(e)

    return result
