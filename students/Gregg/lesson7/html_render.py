"""a set of classes to render html pages – in a “pretty printed” way"""

from io import StringIO
from collections import deque
import logging


class Element(object):
    """an element of an html document

    can have content added in the form of other elemets or strings
    can render itself to a file like object"""

    tag_name = 'html'
    indentation = 4

    def __init__(self, init_content=None):
        self.contents = []
        if not(init_content is None):
            self.append(init_content)


    def append(self, new_content):
        """add content to the element"""
        if hasattr(new_content, 'render'):
            self.contents.append(new_content)
        else:
            try:
                self.contents.append(str(new_content))
            except AssertionError as E:
                raise(TypeError(
                    'Invalid conent. Content must be convertible to a string  '
                    'or an object with render method'
                ))

    def render(self, file_out, current_indent=0):
        """generate a string with pretty indentation and write it to file out"""
        tag_indent_str = current_indent*' '
        start_tag = "{}<{}>".format(tag_indent_str, self.tag_name)
        end_tag = "{}</{}>".format(tag_indent_str, self.tag_name)
        rendered_content_list = []#deque()
        content_indent = current_indent+self.indentation
        for content in self.contents:
            try:
                f = StringIO()
                content.render(f, content_indent)
                content_string = f.getvalue()
            except AttributeError as E:
                #print('{} is not renderable'.format(str(content)))
                #logging.exception(E)
                content_string = f'{content_indent*" "}{content}'
            rendered_content_list.append(content_string)
        rendered_content_string = '\n'.join(rendered_content_list)
        render_string = '{}\n{}\n{}'.format(
            start_tag, rendered_content_string, end_tag
        )
        # f'{current_indent*" "}\n'.join(rendered_content_list)
        file_out.write(render_string)


class Html(Element):
    tag_name = 'html'

class Body(Element):
    tag_name = 'body'

class P(Element):
    tag_name = 'p'


