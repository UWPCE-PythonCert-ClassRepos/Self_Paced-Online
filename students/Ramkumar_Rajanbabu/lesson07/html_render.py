#HTML Renderer

#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    
    tag = "html"
    
    def __init__(self, content=None, **kwargs):
        self.contents = [content] if content else [] #List comprehension solves NoneType
        self.kwargs = kwargs
        
    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        #Loop through the list of contents:        
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            try:    
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

#Step 2
class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"
    
#Step 3
class Head(Element):
    tag = "head"
    
class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
    
    def append(self, new_content):
        raise NotImplementedError
        
class Title(OneLineTag):
    tag = "title"
    
#Step 5