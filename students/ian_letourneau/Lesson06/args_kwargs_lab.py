#!/usr/bin/env python3
# Ian Letourneau
# 5/11/2018
# A script to test various arg and kwarg functionality


def colors(fore_color='white', back_color='black',
           link_color='blue', visited_color='purple'):
    """A function that returns strings based on given
    parameters and default values"""
    return fore_color, back_color, link_color, visited_color


def colors_all(*args, **kwargs):
    print(args, kwargs)
    return args, kwargs
