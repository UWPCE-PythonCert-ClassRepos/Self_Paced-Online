#!/usr/bin/env python3

class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind)
        file_out.write(self.text)

class Element():
    indent = '    '
    tag = 'html'

    def __init__(self, content=None, **attributes):
        self.content = [content] if content else []
        self.attributes = attributes

    def append(self, content_string):
        self.content.append(content_string)
        # if hasattr(content_string, 'render'):
        #     self.content.append(content_string)
        # else:
        #     self.content.append(TextWrapper(str(content_string)))

    def render(self, file_out, cur_indent=''):

        file_out.write(f'{cur_indent}<{self.tag}{self.attributes_add()}>\n')

        for content in self.content:
            try:
                content.render(file_out, cur_indent + self.indent)
            except AttributeError:
                file_out.write(cur_indent + self.indent + str(content) + '\n')
        file_out.write(f'{cur_indent}</{self.tag}>\n')

    def attributes_add(self):
        
        if self.attributes:#error handling
            attributes = " " + " ".join(f'{key}="{value}"' for key, value in self.attributes.items())
        else:
            attributes = ''
        return attributes


class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_indent=''):
        file_out.write(cur_indent + "<!DOCTYPE html>\n")
        super().render(file_out, cur_indent)


class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineElement(Element):
    def render(self, file_out, cur_indent=''):
        file_out.write(f'{cur_indent}<{self.tag}{self.attributes_add()}> ')

        for content in self.content:
            try:
                content.render(file_out, cur_indent + self.indent)
            except AttributeError:
                file_out.write(str(content) + ' ')

        file_out.write(f'</{self.tag}>\n')

class SelfClosingElement(Element):
    
    # def __init__(self, **attribute):
    #     self.attributes = attribute

    def render(self, file_out, cur_indent=''):
        file_out.write(f'{cur_indent}<{self.tag}{self.attributes_add()} />\n ')

        # for content in self.content:
        #     try:
        #         content.render(file_out, cur_indent + self.indent)
        #     except AttributeError:
        #         file_out.write(str(content) + ' ')
        # file_out.write(f'</{self.tag}>\n')

class Hr(SelfClosingElement):
    tag = 'hr'

class Title(OneLineElement):
    tag = 'title'

class Br(SelfClosingElement):
    tag = 'br'


class A(OneLineElement):
    tag = 'a'

    def __init__(self, link, content):
        super().__init__(content, href=link)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineElement):
    def __init__(self, level, content):
        super().__init__(content)
        self.tag = f'h{level}'


class Meta(SelfClosingElement):
    tag = 'meta'
