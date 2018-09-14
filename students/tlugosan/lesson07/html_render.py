#!/usr/bin/env python3


class Element(object):
    tag_name = "html"
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.kwargs = ""
        # style="text-align: center; font-style: oblique;"
        if self.kwargs != {}:
            for k in kwargs:
                self.kwargs += ' ' + str(k) + '=' + '"' + str(kwargs[k]) + '"'
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, cur_ind=''):
        cur_ind += self.indent
        open_tag = "<{}{}>\n".format(self.tag_name, self.kwargs)
        end_tag = "</{}>".format(self.tag_name)
        file_out.write(cur_ind + open_tag)
        for each_content in self.content:
            try:
                each_content.render(file_out, cur_ind)
            except AttributeError:
                file_out.write(self.indent + cur_ind + str(each_content))
            file_out.write('\n')

        file_out.write(cur_ind + end_tag)


class Html(Element):
    tag_name = 'html'

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)

    def render(self, file_out, cur_ind=''):
        file_out.write('<!DOCTYPE html>\n')
        open_tag = "<{}{}>\n".format(self.tag_name, self.kwargs)
        end_tag = "</{}>".format(self.tag_name)
        file_out.write(cur_ind + open_tag)
        for each_content in self.content:
            try:
                each_content.render(file_out)
            except AttributeError:
                file_out.write(str(each_content))
            file_out.write('\n')

        file_out.write(cur_ind + end_tag)


class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'


class Head(Element):
    tag_name = 'head'


class OneLineTag(Element):
    tag_name = ''

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)

    def append(self, content):
        raise NotImplementedError

    def render(self, file_out, cur_ind=''):
        cur_ind += self.indent
        open_tag = "<{}{}>".format(self.tag_name, self.kwargs)
        end_tag = "</{}>".format(self.tag_name)
        file_out.write(cur_ind + open_tag)
        for each_content in self.content:
            try:
                each_content.render(file_out)
            except AttributeError:
                file_out.write(str(each_content))

        file_out.write(cur_ind + end_tag)


class Title(OneLineTag):
    tag_name = 'title'


class SelfClosingTag(Element):
    tag_name = ''

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content.")
        super().__init__(content, **kwargs)

    def append(self, content):
        raise TypeError("you can't add content to a SelfClosingTag")

    def render(self, file_out, cur_ind=''):
        cur_ind += self.indent
        open_tag = "<{}{}/>".format(self.tag_name, self.kwargs)
        file_out.write(cur_ind + open_tag)
#        file_out.write('\n')
        for each_content in self.content:
            try:
                each_content.render(file_out)
            except AttributeError:
                file_out.write(str(each_content))
                file_out.write('\n')
#        file_out.write('\n')


class Hr(SelfClosingTag):
    tag_name = 'hr'


class Br(SelfClosingTag):
    tag_name = 'br'


class A(OneLineTag):
    tag_name = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        self.tag_name = 'h' + str(level)
        super().__init__(content, **kwargs)


class Ul(Element):
    tag_name = 'ul'


class Li(Element):
    tag_name = 'li'


class Meta(SelfClosingTag):
    tag_name = 'meta'

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content.")
        super().__init__(content, **kwargs)



