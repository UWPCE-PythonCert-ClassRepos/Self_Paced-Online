#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


class Element:
    tag = "html"
    indent = "  "


    def __init__(self, content=None, **kwargs): #**kwargs for key:value pairs("id = 'text'")
        self.kwargs = kwargs

        if content is None:
            self.contents = []
        else: 
            self.contents = [content]
        

    def append(self, new_content):
        self.contents.append(new_content)


    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind+f"<{self.tag}")
        for key, value in self.kwargs.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(">\n")
                       
        for content in self.contents:
            if hasattr(content, 'render'):
                content.render(out_file, cur_ind+self.indent)
            else:
                out_file.write(cur_ind+self.indent+content)
                out_file.write("\n")
        out_file.write(cur_ind+f"</{self.tag}>\n")      

                
class Html(Element):
    tag = "html"
    

    def render(self, out_file, cur_ind=""):
        out_file.write(f"<!DOCTYPE html>\n")
        Element.render(self, out_file, cur_ind="")
        
       
class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind+f"<{self.tag}>{self.contents[0]}</{self.tag}>\n")

      
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"
       

class SelfClosingTag(Element):

    def __init__(self, content = None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag cannot have any content")
        super().__init__(content = content, **kwargs)


    def append(self, new_content):
        raise TypeError("You cannot add any content to a SelfClosingTag")
   

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind+f"<{self.tag}")
        for key, value in self.kwargs.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(f" />\n")
            
          
class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(Element):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link  
        super().__init__(content, **kwargs)

 
class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"

 
class H(OneLineTag):

    def __init__(self, level, content = None, **kwargs):
        
        super().__init__(content, **kwargs)
        self.level = level
        self.tag = f"h{self.level}"


class Meta(SelfClosingTag):
    tag = "meta"




