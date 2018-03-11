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

    def append(self, s):
        """Adds a string to the element content"""
        self.content.append(s)

    def render(self, file_out, cur_ind=''):
        """Renders the tag and strings from the element content"""
        file_out.write(cur_ind + f'<{self.tag}>\n')

        for item in self.content:
            file_out.write(cur_ind + self.indent + item + '\n')

        file_out.write(cur_ind + f'<\\{self.tag}>\n')


def main():
    """Main function"""
    pass


if __name__ == '__main__':
    main()
