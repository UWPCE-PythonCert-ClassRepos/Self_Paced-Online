#!/usr/bin/env python3


def style_tags(keyword_dict):
    style = []
    if keyword_dict is not None:
        for key, value in keyword_dict.items():
            style.append(' {}=\"{}\"'.format(key, value))
    return "".join(style)


class Element:
    '''A class to render an HTML element'''

    tag_name = ''
    indents = 4

    def __init__(self, content=None, **kwargs):
        self.content = []
        if content:
            self.content.append(content)
        self.kwargs = kwargs

    def append(self, content):
        '''Appends strings to content'''
        self.content.append(content)

    def render(self, file_out, cur_ind=""):
        '''Render the HTML File'''

        next_ind = cur_ind + (" " * self.indents)
        element_format = style_tags(self.kwargs)
        file_out.write("{}<{}{}>\n".format(cur_ind, self.tag_name, element_format))
        for item in self.content:
            if isinstance(item, str):
                file_out.write('{}{}\n'.format(next_ind, item))
            else:
                item.render(file_out, next_ind)
        file_out.write("{}</{}>\n".format(cur_ind, self.tag_name))


class Html(Element):
    '''A class for an element with an HTML tag'''

    tag_name = 'html'

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)

    def render(self, file_out, cur_ind=""):
        '''Render HTML tags'''
        file_out.write("{}<!DOCTYPE html>\n".format(cur_ind))
        super().render(file_out, cur_ind)


class Head(Element):
    '''A class for an element with a head tag'''

    tag_name = 'head'

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)


class Body(Element):
    '''A class for an element with a body tag'''

    tag_name = 'body'

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)


class P(Element):
    '''A class for an element with a p tag'''

    tag_name = 'p'

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)


class OneLineTag(Element):
    '''A class for an element meant to appear on one line'''

    tag_name = ''

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)

    def render(self, file_out, cur_ind=""):
        '''Render an element meant to appear on one line'''
        element_format = style_tags(self.kwargs)
        file_out.write("{}<{}{}>".format(cur_ind, self.tag_name, element_format))
        for item in self.content:
            if isinstance(item, str):
                file_out.write('{}'.format(item))
            else:
                item.render(file_out)
        file_out.write("</{}>\n".format(self.tag_name))


class Title(OneLineTag):
    '''A class for an element with a title tag'''

    tag_name = 'title'

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)


class A(OneLineTag):
    '''A class for a tags and links'''

    tag_name = 'a'

    def __init__(self, link, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs['href'] = link


class H(OneLineTag):
    '''A class for h tags'''

    def __init__(self, h_level, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.tag_name = 'h{}'.format(h_level)


class SelfClosingTag(Element):
    '''A class for self closing tags'''

    tag_name = ''

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)

    def render(self, file_out, cur_ind=""):
        '''Render self closing tags'''
        element_format = style_tags(self.kwargs)
        file_out.write("{}<{}{} />\n".format(cur_ind, self.tag_name, element_format))


class Hr(SelfClosingTag):
    '''A class for <hr /> tags'''

    tag_name = 'hr'

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)


class Br(SelfClosingTag):
    '''A class for <br /> tags'''

    tag_name = 'br'

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    '''A class for <meta /> tags'''

    tag_name = 'meta'

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)


class Ul(Element):
    '''A class for an unordered list tag'''

    tag_name = 'ul'

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)


class Li(Ul):
    '''A class for a list item tag'''

    tag_name = 'li'

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
