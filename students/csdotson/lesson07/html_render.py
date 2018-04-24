class Element:
    """Create an Element class for rendering an html element"""
    tag_name = 'html'
    indentation = "    "

    def __init__(self, content=None):
        self.content = content

    def append(self, content_to_add):
        if self.content == None:
            self.content = content_to_add
        else:
            self.content += (" " + content_to_add)

    def render(self, file_out, cur_ind=""):
        tag_details = {'opening': "<"+self.tag_name+">", 'closing': "</"+self.tag_name+">", 'content': self.content}
        html_output = "{opening}\n{content}\n{closing}".format(**tag_details)
        file_out.write(html_output)


class HtmlElement(Element):
    tag_name = 'html'


class BodyElement(Element):
    tag_name = 'body'


class ParaElement(Element):
    tag_name = 'p'



# An HTML element usually consists of a start tag and end tag, with the content inserted in between
# <tagname>Content goes here...</tagname>
