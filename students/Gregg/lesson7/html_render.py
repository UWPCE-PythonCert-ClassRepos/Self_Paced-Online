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
