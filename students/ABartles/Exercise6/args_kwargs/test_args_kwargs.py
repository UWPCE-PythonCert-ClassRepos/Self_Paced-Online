from args_kwargs import key_words
from args_kwargs import args_kwargs


regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}


def test_1():
    key_words('red', 'blue', 'yellow', 'chartreuse') is "red, blue, yellow, chartreuse"


def test_2():
    key_words(link_color='red', back_color='blue') is "white, blue, red, purple"


def test_3():
    key_words('purple', link_color='red', back_color='blue') is "purple, blue, red purple"


def test_4():
    key_words(*regular, **links) is "red, blue, chartreuse, purple"


def test_5():
     args_kwargs('red', 'blue', 'yellow', 'chartreuse') is ('red', 'blue', 'yellow', 'chartreuse'), {}


def test_6():
    args_kwargs(link_color='red', back_color='blue') is "white, blue, red, purple"


def test_7():
    args_kwargs('purple', link_color='red', back_color='blue') is "purple, blue, red, purple"


def test_8():
    args_kwargs(*regular, **links) is "red, blue, chartreuse, purple"
