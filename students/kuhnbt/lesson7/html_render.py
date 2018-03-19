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

    def __init__(self, content = None, keywords = None):
        if content:
            self.content = [content]
        else:
            self.content = []
        self.text = None
        self.keywords = keywords

    def append(self, new_content):
        """Add content (str or Element) to an element"""
        self.content.append(new_content)

    def render(self, file_out, cur_ind=0):
        self.text = cur_ind * ' ' + '<' + self.tag_name 
        self.add_keywords()
        self.text += '>\n'
        for element in self.content:
            self.get_text(element, cur_ind)
        self.text += (cur_ind) * ' ' 
        self.text += '</' + self.tag_name + '>'
        file_out.write(self.text)

    def get_text(self, element, cur_ind):
        if hasattr(element, 'render'):
            f = StringIO()
            element.render(f, cur_ind + self.indentation)
            self.text += f.getvalue() + '\n'
        else:
            self.text += (self.indentation + cur_ind) * ' ' + element + '\n'
    
    def add_keywords(self):
        if self.keywords:
            for tag, value in self.keywords.items():
                self.text += ' {}="{}"'.format(tag, value)

class Html(Element):
    tag_name = 'html'

    def render(self, file_out, cur_indent=0):
        self.text = '<!DOCTYPE html>\n'
        file_out.write(self.text)
        Element.render(self, file_out, 0)


class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'


class Head(Element):
    tag_name = 'head'
    def __init__(self, content = None, keywords = None):
        self.content = Charset()
        Element.__init__(self, self.content)

class OneLineTag(Element):
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
    def __init__(self, content = None, keywords = None):
        Element.__init__(self, content, keywords)
        if self.content:
            raise TypeError('Self closing tags cannot contain content')
    def render(self, file_out, cur_ind=0):
        self.text = (cur_ind + self.indentation) * ' '
        self.text += '<' + self.tag_name
        self.add_keywords()        
        self.text += ' />'
        file_out.write(self.text)

class A(OneLineTag):
    tag_name = 'a'
    def __init__(self, link, content):
        OneLineTag.__init__(self, content = content, keywords = {'href':link})

class Ul(Element):
    tag_name = 'ul'

class Li(OneLineTag):
    tag_name = 'li'

class Header(OneLineTag):
    def __init__(self, level, content):
        self.tag_name = 'h' + str(level)
        OneLineTag.__init__(self, content)

class Charset(SelfClosingTag):
    def __init__(self, content = None, keywords = {'charset':'UTF-8'}):
        self.tag_name = 'meta'
        self.keywords = keywords
        self.indentation = 0
        SelfClosingTag.__init__(self, content, keywords)


