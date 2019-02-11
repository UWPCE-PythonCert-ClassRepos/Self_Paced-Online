# Joshua Bone - UW Python 210 - Lesson 9
# 02/10/2019
# Assignment: Mailroom, Object Oriented

from menu_option import MenuOption


def test_token():
    o = MenuOption(None, token="q")
    assert o.token == "q"


def test_desc():
    o = MenuOption(None, desc="Test Description")
    assert o.desc == "Test Description"


def test_evaluate():
    fn = lambda i: "Test"
    o = MenuOption(None, evaluate=fn)
    assert o.evaluate == fn


def test_action():
    fn = lambda i: "Test"
    o = MenuOption(None, action=fn)
    assert o.action == fn


def test_next_menu():
    o = MenuOption("Test Object")
    assert o.next_menu == "Test Object"


def test_hidden():
    o = MenuOption(None, hidden=True)
    assert o.hidden == True


def test_str():
    o = MenuOption(None, "token", "Test Description")
    assert str(o) == "[token]: Test Description"
