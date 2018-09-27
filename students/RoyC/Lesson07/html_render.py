#!/usr/bin/env python3

class Element:

    tag = ""
    indent = 4
    
    def __init__(self, content=None):
        self.content = []
        if not content is None:
            self.append(content)
        
    def append(self, content):
        if isinstance(content, str):
            self.content.append(TextEntry(content))
        else:
            self.content.append(content)
        
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}>\n".format(self.tag))
        sub_ind = cur_ind + (Element.indent * ' ')
        for entry in self.content:
            entry.render(file_out, cur_ind + self.indent * " ")
        file_out.write(cur_ind + "<\{}>\n".format(self.tag))
        
class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"
    
class P(Element):
    tag = "p"
 
class TextEntry(Element):

    def __init__(self, text):
        self.text = text
        
    def append(self, content):
        pass
        
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + self.text + "\n")
    

    

