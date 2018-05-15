from args_kwargs_lab import colors, colors_all

# Test colors function using predetermined function calls


def test_1():
    assert colors('red', 'blue', 'yellow', 'chartreuse') == (
        'red', 'blue', 'yellow', 'chartreuse')


def test_2():
    assert colors(link_color='red', back_color='blue') == (
        'white', 'blue', 'red', 'purple')


def test_3():
    assert colors('purple', link_color='red', back_color='blue') == (
        'purple', 'blue', 'red', 'purple')


def test_4():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    colors(*regular, **links) == ('red', 'blue', 'chartreuse', 'purple')

# Test colors_all function using same predetermined function calls


def test_5():
    assert colors_all('red', 'blue', 'yellow', 'chartreuse') == (
        ('red', 'blue', 'yellow', 'chartreuse'), {})


def test_6():
    assert colors_all(link_color='red', back_color='blue') == ((), {
        'link_color': 'red', 'back_color': 'blue'})


def test_7():
    assert colors_all('purple', link_color='red', back_color='blue') == (
        ('purple',), {'link_color': 'red', 'back_color': 'blue'})


def test_8():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    colors_all(*regular, **links) == (
        ('red', 'blue',), {'link_color': 'chartreuse'})
