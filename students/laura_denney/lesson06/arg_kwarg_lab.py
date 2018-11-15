def colors(fore_color = "black", back_color = "white", link_color = 'blue', visited_color = 'purple'):
    return "colors: {}, {}, {}, {}".format(fore_color, back_color, link_color, visited_color)

def color2(*args, **kwargs):
    print ("args: " , args)
    print ("kwargs: " , kwargs)
    return "colors: ", args, kwargs.values()