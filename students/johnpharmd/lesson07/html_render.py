

class Element():
    """renders an html element"""

    tag = ''
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.content = [content]
        self.kwargs = kwargs

    def append(self, new_string):
        return self.content.append(new_string)

    def render(self, file_out, cur_ind=''):
        if self.kwargs:
            kwargs_string = ' '
            self.open_tag = '<' + self.tag
            for k, v in self.kwargs.items():
                kwargs_string += k + '=' + '\'' + v + '\''
            self.open_tag += kwargs_string + '>'
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
                file_out.write(cur_ind * 3 + self.open_tag + '\n' +
                               cur_ind * 4 + item + '\n' +
                               cur_ind * 3 + self.close_tag + '\n')
            else:
                item.render(file_out, cur_ind)
        if self.tag != 'html' and self.tag != 'p':
            file_out.write(cur_ind * 2 + self.close_tag + '\n')
        elif self.tag == 'html':
            file_out.write(cur_ind + self.close_tag)
        return self.open_tag, self.content, self.close_tag


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


class A(Element):
    """renders an anchor"""
    tag = 'a'

    def __init__(self, link='', content=None):
        self.link = link
        self.content = [content]
        super().__init__()


class SelfClosingTag(Element):
    """renders a selfclosingtag"""
    tag = 'sct'

    def append(self):
        print('TypeError! SelfClosingTag cannot have content.')

    def render(self, file_out, cur_ind):
        file_out.write(cur_ind * 3 + '<' + self.tag + ' />\n')
        return '<' + self.tag + ' />'


class Hr(SelfClosingTag):
    """renders hr tag"""
    tag = 'hr'


class Br(SelfClosingTag):
    """renders br tag"""
    tag = 'br'


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
        return self.open_tag, self.content, self.close_tag


class Title(OneLineTag):
    """renders title"""
    tag = 'title'
