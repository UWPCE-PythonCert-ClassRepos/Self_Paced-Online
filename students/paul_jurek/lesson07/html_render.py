"""advanced html rendering api as part of Lesson07 assingment"""

class Element():
    """creates HTML element and context"""
    tag = ''
    end_character = '\n'

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
        Element.process_content(self.content, file_out=file_out, tag=self.tag, cur_ind=cur_ind, end_character=self.end_character)


    @staticmethod
    def process_content(content, file_out, tag, cur_ind="", end_character="\n"):
        """helper function for render() which allows us to do
        recursive function on content list"""
        file_out.write(f'<{tag}>' + end_character)
        for entry in content:
            if issubclass(type(entry), Element):
                Element.process_content(entry.content, file_out=file_out, tag=entry.tag, end_character=entry.end_character)
            else:
                file_out.write(entry + end_character)
        file_out.write(f'</{tag}>\n')


class Html(Element):
    """html element tag"""
    tag = 'html'


class Body(Element):
    """html element tag"""
    tag = 'body'


class P(Element):
    """html element tag"""
    tag = 'p'


class Head(Element):
    """html element tag for head"""
    tag = 'head'


class OneLineTag(Element):
    """html element tag for head to generate single line tags"""
    tag = 'head'
    end_character = ""

class Title(OneLineTag):
    """html tag for title"""
    tag = 'title'

