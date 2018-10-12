class Element:
    tag = 'html'
    indent = ""

    def __init__(self, content=None, **kwargs):
        self.content = [content] if content else []
        self.attributes = kwargs
 
    def append(self, item):
        """ Appends lines to the list of verbiage"""
        self.content.append(item)

    def render(self, file_out, cur_ind = ""):
        """Writes verbiage and appropriate tags to the file"""
        tagstring = (f"{cur_ind}{self.indent}<{self.tag}")
        if self.attributes:
            for key, value in self.attributes.items():
                tagstring += " {}=\"{}\"".format(key, value)
        tagstring += ">\n"
        file_out.write(tagstring)

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind=cur_ind)
            else:
                file_out.write(f"{cur_ind}{self.indent}{item}\n")
        file_out.write(f"{cur_ind}{self.indent}</{self.tag}>\n")

class P(Element):
    ''' create the p tag '''
    tag = 'p'
    indent = "    "

class Html(Element):
    ''' html tag '''
    tag = 'html'

    def render(self, file_out, cur_indent=''):
        file_out.write(cur_indent + "<!DOCTYPE html>\n")
        super().render(file_out, cur_indent)

class Body(Element):
    ''' create the body tag '''
    tag = 'body'
    indent = "    "

class Head(Element):
    ''' create the head tag '''
    tag = 'head'
    indent = "    "

class OneLineTag(Element):
    ''' for items all on one line '''

    def render(self, file_out, cur_ind = ""):
        tagstring = (f"{cur_ind}{self.indent}<{self.tag}")
        if self.attributes:
            for key, value in self.attributes.items():
                tagstring += " {}=\"{}\"".format(key, value)
        tagstring += ">"
        file_out.write(tagstring)
        
        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind=cur_ind)
            else:
                file_out.write(f"{cur_ind}{self.indent}{item}")
        file_out.write(f"{cur_ind}{self.indent}</{self.tag}>\n")

class Title(OneLineTag):
    ''' create the title tag from OneLineTag '''
    tag = 'title'
    indent = "        "

class SelfClosingTag(Element):

    def render(self, file_out, cur_ind = ""):    
        tagstring = (f"{cur_ind}{self.indent}<{self.tag}")
        if self.attributes:
            for key, value in self.attributes.items():
                tagstring += " {}=\"{}\"".format(key, value)
        tagstring += ">\n"
        file_out.write(tagstring)

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind=cur_ind)
            else:
                file_out.write(f"{cur_ind}{self.indent}{item}\n")

class Hr(SelfClosingTag):
    tag = 'hr'
    indent = "    "

class Br(SelfClosingTag):
    tag = 'br'
    indent = "    "

class A(Element):
    tag = 'a'
    indent = "    "
    def __init__(self, link, content):
        super().__init__(content, href=link)

class Ul(Element):
    tag = 'ul'
    indent = "    "

class Li(Element):
    tag = 'li'
    indent = "        "

class H(OneLineTag):
    tag = 'h'
    def __init__(self, level, text):
        super().__init__()

class Meta(SelfClosingTag):
    tag = 'meta'
    indent = "        "
# Tech Debt
#render function
#tests