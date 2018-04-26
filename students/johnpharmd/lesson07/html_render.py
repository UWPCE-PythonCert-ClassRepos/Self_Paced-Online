class Element():
    """renders an html element"""

    tag = ''
    indent = '    '
    attrs = {'text-align': '', 'font-style': ''}

    def __init__(self, content=None, **kwargs):
        self.content = [content]
        self.kwargs = kwargs

    def append(self, new_string):
        return self.content.append(new_string)

    def render(self, file_out, cur_ind=''):
        if self.kwargs:
            kwargs_string = ' '
            self.open_tag = '<' + self.tag
            # kwargs_keys = [key for key in self.kwargs]
            # kwargs_values = [self.kwargs[key] for key in self.kwargs]
            
            # for tup in zip(kwargs_keys, kwargs_values):
            #     for item in tup:
            #         kwargs_string += str(item)
            
            for k, v in self.kwargs.items():
                kwargs_string += k + '=' +  '\'' + v + '\''

            self.open_tag = self.open_tag + kwargs_string + '>'
        else:
            self.open_tag = '<' + self.tag + '>'
        self.close_tag = '</' + self.tag + '>'
        if self.tag == 'html':
            file_out.write(cur_ind + self.open_tag + '\n')
        elif self.tag != 'p':
            file_out.write(cur_ind * 2 + self.open_tag + '\n')
        for item in self.content:
            if item is None:
                file_out.write('')
            elif type(item) == str:
                file_out.write(cur_ind * 3 + self.open_tag + '\n')
                file_out.write(cur_ind * 4 + item + '\n')
                file_out.write(cur_ind * 3 + self.close_tag + '\n')
            else:
                item.render(file_out, cur_ind)
        if self.tag != 'html' and self.tag != 'p':
            file_out.write(cur_ind * 2 + self.close_tag + '\n')
        elif self.tag == 'html':
            file_out.write(cur_ind + self.close_tag)


class Html(Element):
    """renders html"""
    tag = 'html'


class Body(Element):
    """renders body"""
    tag = 'body'


class P(Element):
    """renders p"""
    tag = 'p'


class Head(Element):
    """renders a head element"""
    tag = 'head'


class OneLineTag(Element):
    """renders onelinetag"""
    tag = 'olt'

    def render(self, file_out, cur_ind=''):
        self.open_tag = '<' + self.tag + '>'
        self.close_tag = '</' + self.tag + '>'
        file_out.write(cur_ind * 3 + self.open_tag)
        for item in self.content:
            if type(item) == str:
                file_out.write(item)
        file_out.write(self.close_tag + '\n')


class Title(OneLineTag):
    """renders title"""
    tag = 'title'
