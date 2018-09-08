class Element:
    """Creates html code for given inputs"""
    tag = ''

    def __init__(self, content = None):
        if content == None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, some_string):
        self.contents.append(some_string)

    def render(self, file_out, cur_ind=""):
            file_out.write("<{}>\n".format(self.tag))
            for content in self.contents:
                    try:
                        content.render(file_out)
                    except AttributeError:
                        file_out.write(content)
                    file_out.write('\n')
            file_out.write("</{}>\n".format(self.tag))


class Html(Element):
    """Creates html code for given inputs"""
    tag = 'html'


class Body(Element):
    """Subclass of Element with html tag for body"""
    tag = 'body'


class P(Element):
    """Subclass of Element with html tag for paragraph"""
    tag = 'p'


class Head(Element):
    """Subclass of Element with html tag for header"""
    tag = 'head'


class OneLineTag(Element):
    """Subclass of Element with html tag for paragraph"""
    def render(self, file_out, cur_ind=""):
            file_out.write("<{html}>{text}</{html}>\n".format(html=self.tag, text=self.contents[0]))

class Title(OneLineTag):
    """Subclass of OneLineTag used for page title"""
    tag = 'title'