"""advanced html rendering api as part of Lesson07 assingment"""

class Element():
    """creates HTML element and context"""
    tag = 'html'

    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, file_out, cur_ind = ""):
        file_out.writelines(self.content)
        