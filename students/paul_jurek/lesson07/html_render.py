"""advanced html rendering api as part of Lesson07 assingment"""

class Element():
    """creates HTML element and context"""
    tag = ''
    end_character = '\n'

    def __init__(self, content=None, **kwargs):
        self.content = []
        if content:
            self.content.append(content)
        self._build_head_tag(**kwargs)
        self._build_closing_tag()

    def append(self, content):
        self.content.append(content)

    def _build_head_tag(self, **kwargs):
        """builds head  tag. dynamically builds
        head based on arguments passed in"""
        self.head_tag = f'<{self.tag}'
        for attribute, value in kwargs.items():
            self.head_tag += f' {attribute}="{value}"'
        self.head_tag += '>' + self.end_character

    def _build_closing_tag(self):
        """builds closing tag"""
        self.closing_tag = f'</{self.tag}>\n'

    def render(self, file_out, cur_ind = ""):
        """initiaties the processing of element tree"""
        Element.process_content(content=self.content, file_out=file_out, head_tag=self.head_tag, closing_tag=self.closing_tag, cur_ind=cur_ind, end_character=self.end_character)

    @staticmethod
    def process_content(content, file_out, head_tag, closing_tag, cur_ind="", end_character="\n"):
        """helper function for render() which allows us to do
        recursive function on content list"""
        file_out.write(head_tag)
        for entry in content:
            if issubclass(type(entry), Element):
                Element.process_content(entry.content, file_out=file_out, head_tag=entry.head_tag, closing_tag=entry.closing_tag, end_character=entry.end_character)
            else:
                file_out.write(entry + end_character)
        file_out.write(closing_tag)


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

class SelfClosingTag(Element):
    """html slef closing tag"""
    tag = 'title'
    end_character = ""

    def __init__(self, content=None, **kwargs):
        if content:
            raise ValueError('Content input not allowed for SelfClosingElements')
        Element.__init__(self)

    def _build_head_tag(self):
        """builds head  tag. dynamically builds
        head based on arguments passed in"""
        self.head_tag = f'<{self.tag} />'

    def _build_closing_tag(self):
        """builds closing tag
        for self closing, we don't need closing so we just do new line"""
        self.closing_tag = '\n'

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'