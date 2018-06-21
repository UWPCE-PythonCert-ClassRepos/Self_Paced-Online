#!/usr/bin/env python3
import sys


# Format string per the exercise definition
def task_one(input_string):
    string_format = "file_{:03d}: {:.2f}, {:.2e}, {:.2e}"
    return string_format.format(*input_string)


random_strings = (2, 123.4567, 10000, 12345.67)

print(task_one(random_strings))
