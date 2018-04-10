from io import StringIO

class Element():
    tagname = 'tag'
    indentation = 4
    def __init__(self, content=None, **attributes):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = attributes

    def append(self, string=None):
        '''Method that can add another string to the content.'''
        self.content.append(string)

    def render(self, file_out, cur_ind=0):
        '''Method that renders the tag and the strings in the content.'''
        self.cur_ind = cur_ind
        if self.attributes is None:
            output = (self.cur_ind * " ") + "<" + self.tagname + ">\n"
        else:
            output = (self.cur_ind * " ") + "<" + self.tagname
            for key, value in self.attributes.items():
                output = output + " " + key + "=" + '"' + value + '"'
            output = output + ">\n"
        if len(self.content) > 0:
            for element in self.content:
                if isinstance(element, str):
                    output = output + (2 * self.cur_ind * " ") + element + "\n"
                else:
                    f = StringIO()
                    element.cur_ind = self.cur_ind + element.indentation
                    element.render(f, element.cur_ind)
                    output = output + f.getvalue()
        output = output + (self.cur_ind * " ") + "</" + self.tagname + ">\n"
        file_out.write(output)

class Html(Element):
    tagname = 'html'

class Body(Element):
    tagname = 'body'

class P(Element):
    tagname = 'p'

class Head(Element):
    tagname = 'head'


class OneLineTag(Element):
    def render(self, file_out, cur_ind=0):
        '''Method that renders the tag and the strings in the content.'''
        self.cur_ind = cur_ind
        if self.attributes is None:
            output = (self.cur_ind * " ") + "<" + self.tagname + ">"
        else:
            output = (self.cur_ind * " ") + "<" + self.tagname
            for key, value in self.attributes.items():
                output = output + " " + key + "=" + '"' + value + '"'
            output = output + ">"
        if len(self.content) > 0:
            for element in self.content:
                if isinstance(element, str):
                    output = output + element
                else:
                    f = StringIO()
                    element.cur_ind = self.cur_ind + element.indentation
                    element.render(f, element.cur_ind)
                    output = output + f.getvalue()
        output = output + "</" + self.tagname + ">\n"
        file_out.write(output)

class Title(OneLineTag):
    tagname = 'title'


class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=0):
        '''Method that renders the tag and the strings in the content.'''
        self.cur_ind = cur_ind
        if self.attributes is None:
            output = (self.cur_ind * " ") + "<" + self.tagname + " />\n"
        else:
            output = (self.cur_ind * " ") + "<" + self.tagname
            for key, value in self.attributes.items():
                output = output + " " + key + "=" + '"' + value + '"'
            output = output + " />\n"
        if len(self.content) > 0:
            raise TypeError('You are not allowed to put content in a self closing tag')
        file_out.write(output)

class Hr(SelfClosingTag):
    tagname = 'hr'

class Br(SelfClosingTag):
    tagname = 'br'
