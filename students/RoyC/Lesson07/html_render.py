#!/usr/bin/env python3

class Element:
    """
    An HTML element represents one level of tag, which can contain more nested elements
    """
    
    tag = ""
    indent = 4
    
    def __init__(self, content=None):
        """
        Optional content is the next element nested under this one
        """
        self.content = []
        if not content is None:
            self.append(content)
        
    def append(self, content):
        """
        Content to be appended is either an Element or a string, which will be used
        to append a new TextElement
        """
        if isinstance(content, str):
            self.content.append(TextEntry(content))
        else:
            self.content.append(content)
        
    def render(self, file_out, cur_ind=""):
        """
        Renders opening tag, followed by nested elements and closing tag
        """
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
    """
    Lowest level of Element, used for plain text line entry
    """

    def __init__(self, text):
        self.text = text
        
    def append(self, content):
        # this is the lowest level Element, append is not applicable
        raise TypeError("TextEntry element does not support lower-level elements")
        
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + self.text + "\n")
    

    

