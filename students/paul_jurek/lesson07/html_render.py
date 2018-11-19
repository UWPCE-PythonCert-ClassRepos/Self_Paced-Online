"""advanced html rendering api as part of Lesson07 assingment"""

class Element():
    """creates HTML element and context"""
    tag = ''
    _start_tag = f'<{tag}>'
    _end_tag = f'</{tag}>'

    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, file_out, cur_ind = ""):
        for entry in self.content:
            file_out.write(entry + '\n')
        #file_out.writelines(self.content)

class Html(Element):
    """html element tag"""
    tag = 'html'


class Body(Element):
    """html element tag"""
    tag = 'body'

class P(Element):
    """html element tag"""
    tag = 'p'