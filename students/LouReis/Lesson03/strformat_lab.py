#!/usr/bin/env python3
# strformat_lab.py
# Coded by LouReis

# Task 1
# Write a format string that will take the following four element tuple:
#        ( 2, 123.4567, 10000, 12345.67)
#        and produce:
#        'file_002 :   123.46, 1.00e+04, 1.23e+04'

"file_{:0>3d}:  {:.2f}, {:.2e}, {:.2e}".format(2,123.4567, 10000, 12345.67)

# Task 2
# Using your results from Task One, repeat the exercise, but this time
# using an alternate type of format string (hint: think about alternative
# ways to use .format() (keywords anyone?), and also consider f-strings if
# you’ve not used them already).

sample = [2, 123.4567, 10000, 12345.67]
f"file_{sample[0]:0>3d}:  {sample[1]:.2f}, {sample[2]:.2e}, {sample[3]:.2e}"
