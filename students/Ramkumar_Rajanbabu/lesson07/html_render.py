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
        self.contents = content
        if self.contents is not None:
            self.contents = [content]
        else:
            self.contents = []
        self.attributes = kwargs
        
    def append(self, new_content):
        """Appends new content to content list."""
        self.contents.append(new_content)
    
    #Step 4
    def _open_tag(self):
        return "".join([f"<{self.tag}", "".join(f' {key}="{value}"' for key, value in self.attributes.items()), ">"])
        
    def _close_tag(self):
        return f"</{self.tag}>"

    def render(self, out_file):      
        """Renders content and tags, then writes to file."""
        #Step 4        
        out_file.write("".join([f"{self._open_tag()}", "\n"]))
        #Loop through the list of contents:
        for content in self.contents:
            try:    
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write("".join([f"{self._close_tag()}", "\n"]))

#Step 2
class Html(Element):
    """Html subclass of Element."""
    tag = "html"
    
    def render(self, out_file):
        out_file.write("<!DOCTYPE html>\n")
        Element.render(self, out_file)

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
    
#Step 4    
class OneLineTag(Element):
    """One line tagging subclass of Element."""
    def render(self, out_file):
        out_file.write("".join([self._open_tag(), self.contents[0], self._close_tag(), "\n"]))
    
    def append(self, new_content):
        """Appends new content to content list and raises error."""
        raise NotImplementedError
        
class Title(OneLineTag):
    """Title subclass of OneLineTag."""
    tag = "title"

#Step 5
class SelfClosingTag(Element):
    
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    
    def render(self, out_file):
        """Renders contents for self closing tags."""
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(tag)
    
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    """Hr subclass of SelfClosingTag."""
    tag = "hr"
    
class Br(SelfClosingTag):
    """Br subclass of SelfClosingTag."""
    tag = "br"

#Step 6
class A(OneLineTag):
    """<a link /a>"""
    
    tag = "a"
    
    def __init__(self, link, content=None, **kwargs):
        kwargs["href"] = link
        super().__init__(content, **kwargs)

#Step 7
class Ul(Element):
    """Unordered list"""
    tag = "ul"
    
class Li(Element):
    """List item"""
    tag = "li"

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = f"h{level}"
        super().__init__(content, **kwargs)

#Step 8
class Meta(SelfClosingTag):
    """<meta />"""
    tag = "meta"