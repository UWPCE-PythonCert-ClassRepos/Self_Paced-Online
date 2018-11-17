
'''
def colors(fore_color = "black", back_color = "white", link_color = 'blue', visited_color = 'purple'):
    return "colors: {}, {}, {}, {}".format(fore_color, back_color, link_color, visited_color)
'''


from arg_kwarg_lab import colors
from arg_kwarg_lab import color2
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}

def test_1():
    assert colors('red', 'blue', 'yellow', 'chartreuse') == 'colors: red, blue, yellow, chartreuse'

def test_2():
    assert colors(link_color='red', back_color='blue') == 'colors: black, blue, red, purple'

def test_3():
    assert colors('purple', link_color='red', back_color='blue') == 'colors: purple, blue, red, purple'

def test_4():
    assert colors(*regular, **links) == 'colors: red, blue, chartreuse, purple'

def test_5():
    assert color2('red', 'blue', 'yellow', 'chartreuse') == 'colors: red, blue, yellow, chartreuse'

def test_6():
    assert color2(link_color='red', back_color='blue') == 'colors: black, blue, red, purple'

def test_3():
    assert color2('purple', link_color='red', back_color='blue') == 'colors: purple, blue, red, purple'

def test_4():
    assert color2(*regular, **links) == 'colors: red, blue, chartreuse, purple'