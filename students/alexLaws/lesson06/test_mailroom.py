#!/usr/bin/env python3

import mailroom


def test_1():
    '''test the note writing function with a current donation'''
    output = ("Dear Alex,\n\nThank you for your generosity to our cause.\nYour"
              " recent gift of $500 is very helpful. You have now donated a "
              "total of $10,000.\nWe greatly appreciate your contributions!"
              "\n\nThank you!\nAlex Laws")
    assert mailroom.generate_note('Alex', 10000, 500) == output


def test_2():
    '''test the note writing function without a current donation'''
    output = ("Dear Alex,\n\nThank you for your generosity to our cause.\nYou "
              "have now donated a total of $10,000.\nWe greatly appreciate "
              "your contributions!\n\nThank you!\nAlex Laws")
    assert mailroom.generate_note('Alex', 10000) == output


def test_3():
    '''test destination creation without giving a directory (user input req)'''
    output = "alex.txt"
    assert mailroom.generate_destination('alex', 'n') == output


def test_4():
    '''test function that adds donations to existing person'''
    a = {'Ryan Moore': [500, 250]}
    mailroom.add_donation('Ryan Moore', 500, a)
    assert a['Ryan Moore'] == [500, 250, 500]


def test_5():
    '''test function that adds donations to new person'''
    a = {'Ryan Moore': [500, 250]}
    b = {'Ryan Moore': [500, 250], 'John': [1000]}
    mailroom.add_donation('John', 1000, a)
    assert a == b
