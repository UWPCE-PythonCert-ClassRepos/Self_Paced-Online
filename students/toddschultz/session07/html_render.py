class Element:
    tag = 'html'
    indent = ""

    def __init__(self, content=None):
        self.content = [content] if content else []
 
    def append(self, item):
        """ Appends lines to the list of verbiage"""
        self.content.append(item)
        

    def render(self, file_out, cur_ind = ""):
        """Writes verbiage and appropriate tags to the file"""
        file_out.write(f"{cur_ind}{self.indent}<{self.tag}>\n")

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind=cur_ind)
            else:
                file_out.write(f"{cur_ind}{self.indent}{item}\n")
        file_out.write(f"{cur_ind}{self.indent}</{self.tag}>\n")

class P(Element):
    ''' create the p tag '''
    tag = 'p'
    indent = "        "

class Html(Element):
    ''' html tag '''
    tag = 'html'

class Head(Element):
    ''' create the head tag '''
    tag = 'head'

class Body(Element):
    ''' create the body tag '''
    tag = 'body'
    indent = "    "