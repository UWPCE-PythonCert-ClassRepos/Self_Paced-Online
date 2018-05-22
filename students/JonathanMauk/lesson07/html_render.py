class Element:

    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.kwargs = kwargs

    def append(self, content):
        self.content.append(content)
