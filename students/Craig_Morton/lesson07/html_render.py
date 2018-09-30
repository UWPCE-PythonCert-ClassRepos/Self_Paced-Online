# ------------------------------------------------- #
# Title: Lesson 7, pt 1/2, html render
# Dev:   Craig Morton
# Date:  9/14/2018
# Change Log: CraigM, 9/14/2018, html render
# ------------------------------------------------- #


class Element:
    """Base Class for HTML tags"""
    def __init__(self, tag_name='element', content=None, **kwargs):
        if content is None:
            self.content = list()
        else:
            self.content = [content]
        tag_style = ''
        if 'style' in kwargs:
            tag_style = ' style="{style}"'.format(style=kwargs['style'])
        self.tag_open = "<{tag}{tag_style}>".format(tag=tag_name, tag_style=tag_style)
        self.tag_close = "</{tag}>".format(tag=tag_name)

    def append(self, content):
        self.content.append(content)

    def render(self, file_out, cur_ind="", one_line_tag=False):
        file_out.write(cur_ind + self.tag_open)
        if not one_line_tag:
            file_out.write('\n')
        for content in self.content:
            if type(content) == str:
                file_out.write(content)
            else:
                content.render(file_out, cur_ind + "   ")
            if not one_line_tag:
                file_out.write('\n')
        if not one_line_tag:
            file_out.write('\n' + cur_ind)
        file_out.write(self.tag_close)


class Html(Element):
    def __init__(self, content=None, **kwargs):
        Element.__init__(self, tag_name="html", content=content, **kwargs)

    def render(self, file_out, cur_ind="", one_line_tag=False):
        file_out.write('<!DOCtype html>\n')
        Element.render(self, file_out, cur_ind=cur_ind, one_line_tag=one_line_tag)


class Body(Element):
    def __init__(self, content=None, **kwargs):
        Element.__init__(self, tag_name="body", content=content, **kwargs)


class Head(Element):
    def __init__(self, content=None, **kwargs):
        Element.__init__(self, tag_name="head", content=content, **kwargs)


class OneLineTag(Element):
    def __init__(self, tag_name, content=None, **kwargs):
        Element.__init__(self, tag_name=tag_name, content=content, **kwargs)

    def render(self, file_out, cur_ind=""):
        Element.render(self, file_out=file_out, cur_ind=cur_ind, one_line_tag=True)


class P(OneLineTag):
    def __init__(self, content=None, **kwargs):
        OneLineTag.__init__(self, tag_name="p", content=content, **kwargs)


class Title(OneLineTag):
    def __init__(self, content=None, **kwargs):
        OneLineTag.__init__(self, tag_name="title", content=content, **kwargs)


class SelfClosingTag(Element):
    def __init__(self, tag_name, content=None, **kwargs):
        if content is not None:
            raise TypeError
        Element.__init__(self, tag_name=tag_name, content=None, **kwargs)
        self.tag_open = self.tag_open[:-1] + "/>"

    def append(self, content):
        raise TypeError

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + self.tag_open)


class Hr(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        SelfClosingTag.__init__(self, 'hr', content=content, **kwargs)


class Br(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        SelfClosingTag.__init__(self, 'br', content=content, **kwargs)


class A(OneLineTag):
    def __init__(self, link, content=None, **kwargs):
        OneLineTag.__init__(self, tag_name='a', content=content, **kwargs)
        self.tag_open = '{tag} href="{link}">'.format(tag=self.tag_open[:-1], link=link)


class Ul(Element):
    def __init__(self, content=None, **kwargs):
        Element.__init__(self, 'ul', content=content, **kwargs)


class Li(Element):
    def __init__(self, content=None, **kwargs):
        Element.__init__(self, 'li', content=content, **kwargs)


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        if 1 <= level <= 6:
            OneLineTag.__init__(self, tag_name='h{}'.format(level), content=content, **kwargs)
        else:
            raise AttributeError('h{} is not valid html'.format(level))


class Meta(SelfClosingTag):
    def __init__(self, charset, **kwargs):
        SelfClosingTag.__init__(self, 'meta', **kwargs)
        self.tag_open = '{tag} charset="{charset}"/>'.format(tag=self.tag_open[:-2], charset=charset)

