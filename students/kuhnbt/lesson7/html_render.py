from io import StringIO

class Element:
    tag_name = ''
    indentation = 4

    def __init__(self, content = None, **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        self.text = None
        self.keywords = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, cur_ind=4):
        self.text = '<' + self.tag_name 
        if self.keywords:
            for tag, value in self.keywords.items():
                self.text += ' {}="{}"'.format(tag, value)
        + '>\n'
        for element in self.content:
            self.text += (cur_ind + self.indentation) * ' ' 
            if hasattr(element, 'render'):
                f = StringIO()
                element.render(f, cur_ind + element.indentation)
                self.text += f.getvalue() + '\n'
            else:
                self.text += element + '\n'
        self.text += (cur_ind) * ' ' 
        self.text += '</' + self.tag_name + '>'
        file_out.write(self.text)

class Html(Element):
    tag_name = 'html'


class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'


class Head(Element):
    tag_name = 'head'


class OneLineTag(Element):
    def render(self, file_out, cur_ind=4):
        self.text = (cur_ind + self.indentation) * ' '
        self.text = '<' + self.tag_name + '>'
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