# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 12:23:00 2018

@author: Laura.Fiorentino
"""


class Element(object):
    tag = 'html'
    indent = '  '

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def _open_tag(self, cur_ind=''):
        open_tag = ['{}<{}'.format(cur_ind, self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append('>')
        open_tag = "".join(open_tag)
        return open_tag

    def _close_tag(self, cur_ind=''):
        close_tag = '{}</{}>'.format(cur_ind[:-2], self.tag)
        return close_tag

    def render(self, file_out, cur_ind=''):
        file_out.write(self._open_tag(cur_ind))
        file_out.write('\n')
        new_ind = cur_ind + Element.indent
        for item in self.content:
            try:
                item.render(file_out, new_ind)
            except AttributeError:
                file_out.write(new_ind + item)
            file_out.write('\n')
        file_out.write(self._close_tag(cur_ind=new_ind))


class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind=''):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, cur_ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, file_out, cur_ind=''):
        new_ind = cur_ind + Element.indent
        file_out.write('{} {}{}'.format(self._open_tag(cur_ind=new_ind[:-2]),
                       self.content[0], self._close_tag(cur_ind=new_ind)))
#        file_out.write(self._open_tag(cur_ind=new_ind[:-2]))
#        file_out.write(' ')
#        file_out.write(self.content[0])
#        file_out.write(self._close_tag(cur_ind=new_ind))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=''):
        new_ind = cur_ind + Element.indent
        file_out.write(self._open_tag(cur_ind=new_ind[:-2])[:-1])
        file_out.write(' />')

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h' + str(level)
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    tag = 'meta'
