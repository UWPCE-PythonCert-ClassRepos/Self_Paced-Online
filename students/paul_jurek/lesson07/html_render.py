"""advanced html rendering api as part of Lesson07 assingment"""

class Element():
    """creates HTML element and context"""
    tag = ''
    end_character = '\n'
    indention = ' ' * 4

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
        file_out.write(self.head_tag)
        for entry in self.content:
            if issubclass(type(entry), Element):
                Element.render(entry, file_out=file_out)
            else:
                file_out.write(entry + self.end_character)
        file_out.write(self.closing_tag)


class Html(Element):
    """html element tag"""
    tag = 'html'

    def _build_head_tag(self, **kwargs):
        """builds head  tag. dynamically builds
        head based on arguments passed in"""
        self.head_tag = f'<!DOCTYPE html>\n<{self.tag}'
        for attribute, value in kwargs.items():
            self.head_tag += f' {attribute}="{value}"'
        self.head_tag += '>' + self.end_character


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
        Element.__init__(self, **kwargs)

    def _build_head_tag(self, **kwargs):
        """builds head  tag. dynamically builds
        head based on arguments passed in"""
        self.head_tag = f'<{self.tag}'
        for attribute, value in kwargs.items():
            self.head_tag += f' {attribute}="{value}"'
        self.head_tag += ' />'

    def _build_closing_tag(self):
        """builds closing tag
        for self closing, we don't need closing so we just do new line"""
        self.closing_tag = '\n'

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

def A(link, content):
    """adapter to call links"""
    return A_Adapter(content=content, href=link)

class A_Adapter(OneLineTag):
    """adapter to enable hyperlinks to use OneLineTag"""
    tag = 'a'

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    """header html tag class"""
    def __init__(self, level, content):
        try:
            self.tag = f'h{level}'
        except ValueError:
            raise ValueError('positive integer should be input for level')
        OneLineTag.__init__(self, content=content)

class Meta(SelfClosingTag):
    """header html tag class"""
    tag = 'meta'