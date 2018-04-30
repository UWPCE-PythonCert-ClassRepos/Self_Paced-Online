

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
            self.open_tag = '<' + self.tag
            kwargs_string = ''
            for k, v in self.kwargs.items():
                kwargs_string += ' ' + k + '=' + '\'' + v + '\''
            self.open_tag += kwargs_string + '>'
            if self.tag == 'ul':
                self.open_tag += '\n'
        else:
            if self.tag != 'a':
                self.open_tag = '<' + self.tag + '>'
            else:
                self.open_tag = '<' + self.tag
        self.close_tag = '</' + self.tag + '>'
        if self.tag == 'html':
            file_out.write(self.open_tag + '\n')
        elif self.tag == 'ul':
            file_out.write(cur_ind * 2 + self.open_tag)
        elif self.tag == 'li':
            file_out.write(cur_ind * 3 + self.open_tag + '\n')
        elif self.tag == 'a':
            file_out.write(cur_ind * 4 + self.open_tag)
        elif self.tag != 'p':
            file_out.write(cur_ind + self.open_tag + '\n')
        for item in self.content:
            if item is None:
                file_out.write('')
            elif type(item) == str or type(item) == int:
                if self.tag in ('p', ):
                    file_out.write(cur_ind * 2 + self.open_tag + '\n' +
                                   cur_ind * 3 + item + '\n' +
                                   cur_ind * 2 + self.close_tag + '\n')
                elif self.tag == 'body':
                    file_out.write(cur_ind * 2 + item + '\n')
                elif self.tag == 'a':
                    file_out.write(item + self.close_tag + '\n')
                elif self.tag == 'li':
                    file_out.write(cur_ind * 4 + item + '\n')
            else:
                item.render(file_out, cur_ind)
        if self.tag == 'html':
            file_out.write(self.close_tag)
        elif self.tag in ('body', 'head'):
            file_out.write(cur_ind + self.close_tag + '\n')
        elif self.tag == 'ul':
            file_out.write(cur_ind * 2 + self.close_tag + '\n')
        elif self.tag == 'li':
            file_out.write(cur_ind * 3 + self.close_tag + '\n')
        return self.open_tag, self.content, self.close_tag


class Html(Element):
    """renders html"""
    tag = 'html'

    def render(self, file_out, cur_ind=''):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out, cur_ind)


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

    def __init__(self, link, content):
        # self.link = link
        # self.content = content
        Element.__init__(self, content, href=link)


class SelfClosingTag(Element):
    """renders a selfclosingtag"""
    tag = 'sct'

    def append(self):
        print('TypeError! SelfClosingTag cannot have content.')

    def render(self, file_out, cur_ind):
        file_out.write(cur_ind * 2 + '<' + self.tag + ' />\n')
        return '<' + self.tag + ' />'


class Ul(Element):
    """renders a ul"""
    tag = 'ul'


class Li(Element):
    """renders a li element"""
    tag = 'li'


class Hr(SelfClosingTag):
    """renders hr tag"""
    tag = 'hr'


class Br(SelfClosingTag):
    """renders br tag"""
    tag = 'br'


class Meta(SelfClosingTag):
    """renders meta tag"""
    tag = 'meta'


class OneLineTag(Element):
    """renders onelinetag"""
    tag = 'olt'

    def render(self, file_out, cur_ind=''):
        self.open_tag = '<' + self.tag + '>'
        self.close_tag = '</' + self.tag + '>'
        file_out.write(cur_ind * 2 + self.open_tag)
        for item in self.content:
            if type(item) == str:
                file_out.write(item)
        file_out.write(self.close_tag + '\n')
        return self.open_tag, self.content, self.close_tag


class Title(OneLineTag):
    """renders title"""
    tag = 'title'


class H(OneLineTag):
    """renders a header element"""
    tag = 'h'

    def __init__(self, integer, content=None):
        OneLineTag.__init__(self, content)
        self.integer = str(integer)
        self.tag += self.integer
