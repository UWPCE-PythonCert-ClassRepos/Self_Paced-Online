"""advanced html rendering api as part of Lesson07 assingment"""

class Element():
    """creates HTML element and context"""
    tag = ''

    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)
        self._start_tag = f'<{self.tag}>'
        self._end_tag = f'</{self.tag}>'

    def append(self, content):
        self.content.append(content)

    def render(self, file_out, cur_ind = ""):
        """initiaties the processing of element tree"""
        Element.process_content(self.content, file_out=file_out, cur_ind=cur_ind)


    @staticmethod
    def process_content(content, file_out, cur_ind=""):
        """helper function for render() which allows us to do
        recursive function on content list"""
        for entry in content:
            if issubclass(type(entry), Element):
                Element.process_content(entry.content, file_out=file_out)
            else:
                file_out.write(entry + '\n')


class Html(Element):
    """html element tag"""
    tag = 'html'


class Body(Element):
    """html element tag"""
    tag = 'body'

class P(Element):
    """html element tag"""
    tag = 'p'