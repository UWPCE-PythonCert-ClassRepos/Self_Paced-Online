# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  23-Mar-2018
# ------------------------------------------- #

# Create an Element class


class Element():
    ''' Element class for rendering an html element '''

    # Class attributes
    tag_name = ''
    indent = '    '  # 4 spaces

    def __init__(self, content=None, **kwargs):
        ''' initialize the Element object/instance '''
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.kwargs = kwargs

    def append(self, content):
        ''' store content to self.content list '''
        self.content.append(content)

    def render(self, file_out, cur_ind=''):
        ''' render the tag and the strings in the content '''
        file_out.write('{}<{}{}>\n'.format(cur_ind, self.tag_name, self.set_attr()))

        '''for attr in self.kwargs:
            file_out.write(' {}="{}"'.format(attr, self.kwargs[attr]))
        file_out.write('>\n')'''

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write('{}{}{}\n'.format(cur_ind, self.indent, item))

        file_out.write('{}</{}>\n'.format(cur_ind, self.tag_name))

    def set_attr(self):
        if self.kwargs:
            for k, v in self.kwargs.items():
                attr, val = k, v
            return ' {}="{}"'.format(attr, val)
        else:
            return ''


class Html(Element):
    ''' <html> tag '''
    # Class attributes
    tag_name = 'html'
    doc_type = '<!DOCTYPE html>'

    def render(self, file_out, cur_ind=''):
        ''' render the html tag '''

        file_out.write('{}\n'.format(self.doc_type))
        super().render(file_out, cur_ind='')


class Body(Element):
    ''' <body> tag '''
    tag_name = 'body'


class P(Element):
    ''' <p> tag '''
    tag_name = 'p'


class Head(Element):
    ''' <head> tag '''
    tag_name = 'head'


class OneLineTag(Element):
    ''' subclass of Element to render everything on one line '''

    def render(self, file_out, cur_ind=''):
        ''' render one line tag '''
        file_out.write('{}<{}>'.format(cur_ind, self.tag_name))

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(item)
        file_out.write('</{}>\n'.format(self.tag_name))


class Title(OneLineTag):
    ''' subclass of OneLineTag class '''
    tag_name = 'title'


class SelfClosingTag(Element):
    ''' render tags like <hr/> and <br/> '''

    ''' this does not work, and not sure why
    def __init__(self, content=None, **kwargs):
        super().__init__(content=None, **kwargs)
        if self.content is not None:
            raise TypeError('Self closing tags cannot have any content.') '''

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def render(self, file_out, cur_ind=''):
        ''' render self closing tags '''
        file_out.write('{}<{}{}/>\n'.format(cur_ind, self.tag_name, self.set_attr()))


class Hr(SelfClosingTag):
    ''' <hr/> tag '''
    tag_name = 'hr'


class Br(SelfClosingTag):
    ''' <br/> tag '''
    tag_name = 'br'


class A(Element):
    ''' <a> tag '''
    tag_name = 'a'

    def __init__(self, link, content):
        super().__init__(content, href=link)


class Ul(Element):
    ''' <ul> tag '''
    tag_name = 'ul'


class Li(Element):
    ''' <li> tag '''
    tag_name = 'li'


class H(OneLineTag):
    ''' header (<h1>, <h2>...) tags '''
    tag_name = 'h'

    def __init__(self, h_size, content, **kwargs):
        super().__init__(content, **kwargs)
        self.h_size = h_size
        self.tag_name = '{}{}'.format(self.tag_name, self.h_size)


class Meta(SelfClosingTag):
    ''' <meta> tag '''
    tag_name = 'meta'
