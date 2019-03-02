# Joshua Bone - UW Python 210 - Lesson 9
# 02/10/2019
# Assignment: Mailroom, Object Oriented

import pytest
from menu import Menu
from menu_option import MenuOption


def test_title():
    m = Menu("Test Menu")
    assert m.title == "Test Menu"


def test_instr():
    m = Menu("Test Menu", "Test Instructions")
    assert m.instr == "Test Instructions"


def test_add_option():
    m = Menu()
    o1 = MenuOption(Menu("m1"))
    m.add_option(o1)
    assert m.options == (o1,)
    o2 = MenuOption(Menu("m2"))
    m.add_option(o2)
    assert m.options == (o1, o2)


def test_add_options_list():
    m = Menu()
    olist = [MenuOption(Menu("m1")), MenuOption(Menu("m2"))]
    m.add_options(olist)
    assert m.options == tuple(olist)


def test_add_options_tuple():
    m = Menu()
    otuple = (MenuOption(Menu("m1")), MenuOption(Menu("m2")))
    m.add_options(otuple)
    assert m.options == otuple


def test_evaluate_option():
    m = Menu("Test Main Menu")
    next_menu = Menu("Test Next Menu")
    eval_fn = lambda i: i == "token"
    action_fn = lambda i: "Test Fn"
    m.add_option(MenuOption(next_menu, evaluate=eval_fn, action=action_fn))

    action_result, menu_result = m.evaluate("token")

    assert action_result == "Test Fn"
    assert menu_result == next_menu


def test_evaluate_default():
    next_menu = Menu("Test Next Menu")
    eval_fn = lambda i: i == "token"
    action_fn = lambda i: "Test Fn"
    m = Menu("Test Main Menu", 
             default=MenuOption(next_menu, evaluate=eval_fn, action=action_fn))
    m.add_option(MenuOption(Menu("m1")))
    
    action_result, menu_result = m.evaluate("test token")

    assert action_result == "Test Fn"
    assert menu_result == next_menu

   
