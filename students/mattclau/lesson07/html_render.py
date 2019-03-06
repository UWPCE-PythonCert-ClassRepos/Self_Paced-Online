'Main class to hold html elements'
class Element:

    'class attribute to store html tags'
    tag = 'html'

    indent = '\t'

    def __init__(self, content=None, **kwargs):
        'initialize Element with the content to be stored as a list, default list starts with the content passed in'
        if content is None:
            self.content = []
        else:
            self.content = [content]
        if kwargs is not None:
            self.attribs = kwargs
        else: self.attribs = {}


    def append(self, new_text):
        'append method that appends new text to the element class'
        self.content.append(new_text)

    def add_attributes(self):

        attributes = ''

        for key, value in self.attribs.items():
            attributes += key
            attributes += '="'
            attributes += value +'"'

        return attributes


    def render(self, out_file, cur_ind = ''):
        'renders the content of the element to a file with appropriate tags'

        #add attributes to go inside tag if they exist
        if self.attribs != {}:
            out_file.write(f'{cur_ind}<{self.tag} {self.add_attributes()}>\n')
        else:
            out_file.write(f'{cur_ind}<{self.tag}>\n')

        for item in self.content:
            try:
                item.render(out_file, cur_ind+self.indent)
            except AttributeError:
                out_file.write(cur_ind+self.indent+item)

            out_file.write('\n')

        out_file.write(f'{cur_ind}</{self.tag}>')


class Body(Element):
    tag = 'body'

class Html(Element):
    tag = 'html'

    #override render to add doctype tag at top of file then call element render for rest of file
    def render(self, out_file):
        out_file.write(f'<!DOCTYPE html>\n')

        Element.render(self, out_file, '')

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    'class to render all on 1 line'
    def render(self, out_file, indent = ''):

        if self.attribs != {}:
            out_file.write(f'{indent}<{self.tag} {self.add_attributes()}>')
        else:
            out_file.write(f'{indent}<{self.tag}>')

        for item in self.content:
            try:
                item.render(out_file,indent)
            except AttributeError:
                out_file.write(item)

        out_file.write(f'</{self.tag}>')

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):

    #override init to raise error if content passed
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError('Self closing tags cannot have content')
        if kwargs is not None:
            self.attribs = kwargs
        else: self.attribs = {}

    def render(self, out_file, indent = ''):
        'renders the content of the element to a file with appropriate tags'

        #add attributes to go inside tag if they exist
        if self.attribs != {}:
            out_file.write(f'{indent}<{self.tag} {self.add_attributes()} />')
        else:
            out_file.write(f'{indent}<{self.tag} />')


class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'

    #override init to handle links
    def __init__(self, link, content):
        'initialize Element with the content to be stored as a list, default list starts with the content passed in'
        super().__init__(content, href=link)

class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = 'h'

    #override init to allow various headers
    def __init__(self, level, content=None, **kwargs):
        'initialize Element with the content to be stored as a list, default list starts with the content passed in'
        if content is None:
            self.content = []
        else:
            self.content = [content]
        if kwargs is not None:
            self.attribs = kwargs
        else: self.attribs = {}

        #set tag to level
        self.tag = 'h' + str(level)

class Meta(SelfClosingTag):
    tag = 'meta'


def main():
    pass

if __name__ == '__main__':
    main()
