"""Hi Natasha and Rob, I didn't totally understand the note in the 
assignment about submitting attributes to the constructor for an Element
 class. I understand the point about how passing a reserved word like class
would cause an error, but the assigment description seemed to suggest 
using **kwargs to collect user-defined attributes, which I don't think
would solve the problem because a user could still pass a reserved word. 
Then in the run_html_render script the code passes strings of attributes 
which doesn't match what was talked about in the assignment description.
Anyway, I decided to require the user to pass a dict of strings which 
seemed to me like the simplest solution. Let me know if I totally 
missed the point!"""

from io import StringIO


class Element:
    """Base class for Html elements

    Attributes:
        tag_name(str): type of Html tag
        indentation(int): number of spaces the content of a tag should
            be indented
        content(list containing str and Element objects): content of
            the tag
        keywords(dict): pairs of attributes/values for the tag
    """
    tag_name = ''
    indentation = 4

    def __init__(self, content=None, keywords=None):
        if content:
            self.content = [content]
        else:
            self.content = []
        self.text = None
        if keywords and type(keywords) != dict:
            raise TypeError('Keywords must be in dictionary format')
        self.keywords = keywords

    def append(self, new_content):
        """Add content (str or Element) to an element"""
        if type(new_content) == str or isinstance(new_content, Element):
            self.content.append(new_content)
        else:
            raise TypeError('Element content must be str or Element')

    def render(self, file_out, cur_ind=0):
        """Render text representation of Element and write to file_out"""
        self.text = cur_ind * ' ' + '<' + self.tag_name
        self.add_keywords()
        self.text += '>\n'
        for element in self.content:
            self.get_text(element, cur_ind)
        self.text += cur_ind * ' '
        self.text += '</' + self.tag_name + '>'
        file_out.write(self.text)

    def get_text(self, element, cur_ind):
        """Return string representation of an element"""
        if hasattr(element, 'render'):
            f = StringIO()
            element.render(f, cur_ind + self.indentation)
            self.text += f.getvalue() + '\n'
        else:
            self.text += (self.indentation + cur_ind) * ' ' + element + '\n'

    def add_keywords(self):
        """Return string representaion of keywords for Element"""
        if self.keywords:
            for tag, value in self.keywords.items():
                self.text += ' {}="{}"'.format(tag, value)


class Html(Element):
    """Class for basic Html tags """
    tag_name = 'html'

    def render(self, file_out, cur_indent=0):
        """Render Html tag and standard DOCTYPE string"""
        self.text = '<!DOCTYPE html>\n'
        file_out.write(self.text)
        Element.render(self, file_out, 0)


class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'


class Head(Element):
    tag_name = 'head'

    def __init__(self, content=None, keywords=None):
        Element.__init__(self, content, keywords)


class OneLineTag(Element):
    """Class for tags that start and end on one line"""
    def render(self, file_out, cur_ind=0):
        self.text = cur_ind * ' '
        self.text += '<' + self.tag_name
        self.add_keywords()
        self.text += '>'
        for element in self.content:
            if hasattr(element, 'render'):
                f = StringIO()
                element.render(f, 0)
                self.text += f.getvalue()
            else:
                self.text += element
        self.text += '</' + self.tag_name + '>'
        file_out.write(self.text)


class Title(OneLineTag):
    tag_name = 'title'


class SelfClosingTag(Element):
    """Class for tags that close themselves and have no pair"""
    indentation = 0

    def __init__(self, content=None, keywords=None):
        Element.__init__(self, content, keywords)
        if self.content:
            raise TypeError('Self closing tags cannot contain content')

    def render(self, file_out, cur_ind=0):
        self.text = (cur_ind + self.indentation) * ' '
        self.text += '<' + self.tag_name
        self.add_keywords()
        self.text += ' />'
        file_out.write(self.text)


class Hr(SelfClosingTag):
    tag_name = 'hr'


class Br(SelfClosingTag):
    tag_name = 'br'


class A(OneLineTag):
    tag_name = 'a'

    def __init__(self, link, content):
        OneLineTag.__init__(self, content=content, keywords={'href': link})


class Ul(Element):
    tag_name = 'ul'


class Li(OneLineTag):
    tag_name = 'li'


class H(OneLineTag):
    def __init__(self, level, content):
        self.tag_name = 'h' + str(level)
        OneLineTag.__init__(self, content)


class Meta(SelfClosingTag):
    def __init__(self, content=None, charset='UTF-8'):
        self.tag_name = 'meta'
        self.keywords = {"charset":charset}
        self.indentation = 0
        SelfClosingTag.__init__(self, content, self.keywords)

