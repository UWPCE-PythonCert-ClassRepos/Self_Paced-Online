#!/usr/bin/env python3
"""HTML Render Module

This module contains all of the functions for the HTML Render module
"""


class Element(object):
    """Element class for rendering an HTML element"""
    tag = ''
    indent = '    '

    def __init__(self, content=None, **attrs):
        self.content = [content] if content else []
        self.attrs = attrs

    def append(self, content):
        """Adds a content to the element.

        Args:
            content (str or Element): Content to be appended.
        """
        self.content.append(content)

    def render(self, file_out, cur_ind=''):
        """Renders the tag and strings from the element content.

        Args:
            file_out (file): Writable file-like object to recieve rendered data.
            cur_ind (str, optional): Defaults to ''. Indentation of current element.
        """
        file_out.write(f'{cur_ind}<{self.tag}{self.fmt_attrs()}>\n')

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(cur_ind + self.indent + str(item) + '\n')

        file_out.write(cur_ind + f'</{self.tag}>\n')

    def fmt_attrs(self):
        if self.attrs:
            attrs = ' ' + ' '.join(f'{k}="{v}"' for k, v in self.attrs.items())
        else:
            attrs = ''

        return attrs


class HtmlElement(Element):
    """HTML type Element"""
    tag = 'html'


class BodyElement(Element):
    """Body type Element"""
    tag = 'body'


class ParagraphElement(Element):
    """Paragraph type Element"""
    tag = 'p'


class HeadElement(Element):
    """Head type Element"""
    tag = 'head'


class OneLineElement(Element):
    """One line type Element. Overrides Element.render()"""
    def render(self, file_out, cur_ind=''):
        """Renders the tag and strings from the element content onto one line.

        Args:
            file_out (file): Writable file-like object to recieve rendered data.
            cur_ind (str, optional): Defaults to ''. Indentation of current element.
        """
        file_out.write(f'{cur_ind}<{self.tag}> ')

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(str(item) + ' ')

        file_out.write(f'</{self.tag}>\n')


class TitleElement(OneLineElement):
    """Title type Element"""
    tag = 'title'


class SelfClosingElement(Element):
    """Self-Closing type Element"""
    def __init__(self, content=None, **attrs):
        super().__init__(content=None, **attrs)

    # Overwrite content attribute to prevent use
    @property
    def content(self):
        return None

    @content.setter
    def content(self, value):
        pass

    def render(self, file_out, cur_ind=''):
        """Renders the tag and attrs as self-closing element.

        Args:
            file_out (file): Writable file-like object to recieve rendered data.
            cur_ind (str, optional): Defaults to ''. Indentation of current element.
        """
        file_out.write(f'{cur_ind}<{self.tag}{self.fmt_attrs()} />\n')


class HrElement(SelfClosingElement):
    """hr type self-closing element"""
    tag = 'hr'


class BrElement(SelfClosingElement):
    """br type self-closing element"""
    tag = 'br'


def main():
    """Main function"""
    pass


if __name__ == '__main__':
    main()
