class Element(object):
    """renders an html element"""

    tag = ''
    indent = 0

    def __init__(self, content=None):
        self.content = content
