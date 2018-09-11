def keywords(fore_color="orange", back_color="black", link_color="blue", visited_color="green"):
    return fore_color, back_color, link_color, visited_color


print(keywords('red', 'blue', 'yellow', 'chartreuse'))
print(keywords(link_color='red', back_color='blue'))
print(keywords('purple', link_color='red', back_color='blue'))

regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
print(keywords(*regular, **links))