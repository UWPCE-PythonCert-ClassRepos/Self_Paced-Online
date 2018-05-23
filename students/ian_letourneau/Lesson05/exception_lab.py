#!/usr/bin/env python3
# Ian Letourneau
# 5/10/2018


def safe_input():
    """ A wrapper function to test the input given by a user. If
    EOFError or KeyboardInteruppt excepttions occure, return 'None'"""
    try:
        input("Please enter something: ")
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None
