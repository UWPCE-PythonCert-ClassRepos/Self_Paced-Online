"""a set of classes to render html pages – in a “pretty printed” way"""


class Element(object):
    tag_name = 'html'
    indentation = 4

    def __init__(self, init_content=None):
        self.content = []
        if not(init_content is None):
            self.append(init_content)

    def append(self, new_content):
        try:
            assert(isinstance(new_content, str))
            self.content.append(new_content)
        except AssertionError as E:
            raise(TypeError('Invalid conent. Content must be a string'))

    def render(self, file_out, current_indent=0):
        start_tag = "<{}>".format(self.tag_name)
        end_tag = "</{}>".format(self.tag_name)
        content_string = f'{self.indentation*" "}{"".join(self.content)}'
        render_list = [start_tag, content_string, end_tag]
        render_string = f'{current_indent*" "}\n'.join(render_list)
        file_out.write(render_string)
