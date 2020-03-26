#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    #
    if s[-2:] == "PM" and s[:2] != "12":
        s = s.replace(s[:2], str(12+int(s[:2])))
    elif s[-2:] == "AM" and s[:2] == "12":
        s = s.replace(s[:2], "00")
    # Write your code here.
    #
    return s[:-2]


s = "01: 05: 45PM"
print(timeConversion(s))
