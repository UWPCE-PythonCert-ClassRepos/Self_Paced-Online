

def key_words(
    fore_color="white",
    back_color="black",
    link_color="blue",
    visited_color="purple"):
    colors = "{}, {}, {}, {}".format(
        fore_color,
        back_color,
        link_color,
        visited_color)
    return colors


def args_kwargs(*args, **kwargs):
    colors = "{}, {}".format(args, kwargs)
    print(colors)
    return colors
