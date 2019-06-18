#HTML Renderer

#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    """Main Class"""
    
    tag = "html"
    
    def __init__(self, content=None, **kwargs):
        """Initializer"""
        
        self.contents = [content] if content else [] #List comprehension solves NoneType
        self.attributes = kwargs
        
    def append(self, new_content):
        """Appends new content to content list."""
        self.contents.append(new_content)

    def render(self, out_file):      
        """Renders content and tags, then writes to file."""
        #Step 4
        out_file.write("<{}".format(self.tag))
        for key, value in self.attributes.items():
           out_file.write(' {}="{}"'.format(key, value))
        out_file.write(">\n")
        
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
    """Html subclass of Element."""
    tag = "html"

class Body(Element):
    """Body subclass of Element."""
    tag = "body"

class P(Element):
    """P subclass of Element."""
    tag = "p"
    
#Step 3
class Head(Element):
    """Head subclass of Element."""
    tag = "head"
    
class OneLineTag(Element):
    """One line tagging subclass of Element."""
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
    
    def append(self, new_content):
        """Appends new content to content list and raises error."""
        raise NotImplementedError
        
class Title(OneLineTag):
    """Title subclass of OneLineTag."""
    tag = "title"
    
#Step 5
class SelfClosingTag(Element):
    
    def render(self, out_file):
        """Renders contents for self closing tags."""
        out_file.write("<{}".format(self.tag))
        for key, value in self.attributes.items():
           out_file.write(' {}="{}"'.format(key, value))
        if self.contents:
            raise TypeError
        out_file.write(" />")
        

class Hr(SelfClosingTag):
    """Hr subclass of SelfClosingTag."""
    tag = "hr"
 
    
#class Br(SelfClosingTag):
#    """Hr subclass of SelfClosingTag."""
#    tag = "br"