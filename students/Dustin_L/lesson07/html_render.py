#!/usr/bin/env python3
"""HTML Render Module

This module contains all of the functions for the HTML Render module
"""


class Element(object):
    """Element class for rendering an HTML element"""
    tag = ''
    indent = '    '

    def __init__(self, content=None):
        self.content = [content] if content else []

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
        file_out.write(cur_ind + f'<{self.tag}>\n')

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(cur_ind + self.indent + str(item) + '\n')

        file_out.write(cur_ind + f'<\\{self.tag}>\n')


class HtmlElement(Element):
    """HTML type Element"""
    tag = 'html'


class BodyElement(Element):
    """Body type Element"""
    tag = 'body'


class ParagraphElement(Element):
    """Paragraph type Element"""
    tag = 'p'


def main():
    """Main function"""
    pass


if __name__ == '__main__':
    main()
