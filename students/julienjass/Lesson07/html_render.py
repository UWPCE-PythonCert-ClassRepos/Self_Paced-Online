#!/usr/bin/env python3

class Element:
    """Base Class of the HTML Render"""
    tag = 'html'
    ind = 0

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        if content != None:
            self.content = [content]
        if kwargs:
            self.attrs = kwargs
        else:
            self.attrs = None

    def append(self, new_content):
        """Add content to Element"""
        self.content.append(new_content)

    def add_newlines(self):
        """Loop thru self.content and insert newlines"""
        if any(isinstance(line, str) for line in self.content):
            content_copy = self.content[:]
            for i in range(len(content_copy)-1):
                next_index = i + 1
                if isinstance(content_copy[i], object) and not isinstance(content_copy[i], str):
                    pass
                elif not isinstance(content_copy[next_index], str):
                    self.content.insert(next_index, '\n')
        if isinstance(self.content[-1], str):
            self.content.append('\n')

    def render(self, out_file, **kwargs):
        """Render content and attributes with correct level of indentation"""
        self.add_newlines()
        if 'indent' in kwargs:
            indent = kwargs['indent']
        else:
            indent = self.ind
        if self.attrs:
            attr_string = ''
            for key, value in self.attrs.items():
                attr_string += str('{}="{}" '.format(key, value))
            out_file.write(f'{" "*indent}<{self.tag} {attr_string.strip()}>\n')
        else:
            out_file.write(f'{" "*indent}<{self.tag}>\n')
        for line in self.content:
            if isinstance(line, str):
                out_file.write(f'{" "*(indent+4)}{line}')
            elif isinstance(line, object):
                line.render(out_file, indent=indent+4)
        out_file.write(f'{" "*indent}</{self.tag}>\n')
        return out_file

class OneLineTag(Element):
    """SubClass without newlines between content and kwargs"""
    def render(self, out_file, **kwargs):
        if 'indent' in kwargs:
            indent = kwargs['indent']
        else:
            indent = self.ind
        if self.attrs:
            attr_string = ''
            for key, value in self.attrs.items():
                attr_string += str('{}="{}" '.format(key, value))
            out_file.write(f'{" "*indent}<{self.tag} {attr_string.strip()}>')
        else:
            out_file.write(f'{" "*indent}<{self.tag}>')
        for line in self.content:
            if isinstance(line, str):
                out_file.write(f'{line}')
            elif isinstance(line, object):
                line.render(out_file, indent=indent+4)
        out_file.write(f'</{self.tag}>\n')
        return out_file

class SelfClosingTag(Element):
    """SubClass without newlines and without closing tag"""
    def __init__(self, **kwargs):
        if 'content' in kwargs:
            raise ValueError('No content is allowed in self-closing tags')
        if kwargs:
            self.attrs = kwargs
        else:
            self.attrs = None

    def render(self, out_file, **kwargs):
        if 'indent' in kwargs:
            indent = kwargs['indent']
        else:
            indent = self.ind
        if self.attrs:
            attr_string = ''
            for key, value in self.attrs.items():
                attr_string += str('{}="{}" '.format(key, value))
            out_file.write(f'{" "*indent}<{self.tag} {attr_string.strip()} />\n')
        else:
            out_file.write(f'{" "*indent}<{self.tag} />\n')
        return out_file


class Html(Element):
    ind = 0
    def render(self, out_file, **kwargs):
        out_file.write(f'<!DOCTYPE html>\n')
        Element.render(self, out_file, **kwargs)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class Title(OneLineTag):
    tag = 'title'


class Hr(SelfClosingTag):
    tag = 'hr'


class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content):
        super().__init__(content, href=link)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    tag = 'h'
    def __init__(self, level, content):
        self.tag = f'h{level}'
        super().__init__(content)


class Meta(SelfClosingTag):
    tag = 'meta'
