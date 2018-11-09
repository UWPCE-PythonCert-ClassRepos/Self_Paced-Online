#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    tag = "html"


    def __init__(self, content=None, **kwargs ): #**kwargs key:value pairs("id = 'text'")
        self.kwargs = kwargs
        if content is None:
            self.contents = []
        else: 
            self.contents = [content]
        

    def append(self, new_content):
        self.contents.append(new_content)


    def render(self, out_file):
        if self.kwargs == {}:
            out_file.write(f"<{self.tag}>\n")
        else:
            out_file.write("<{}".format(self.tag))
            for key, value in self.kwargs.items():
                # out_file.write(f"<{self.tag} {key}='{value}'>\n")
                out_file.write(' {}="{}"'.format(key,value))
            out_file.write(f">\n")
                

        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write(f"</{self.tag}>")

        

    
class Html(Element):
    tag = "html"



class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write(f"<{self.tag}>{self.contents[0]}</{self.tag}>\n")
        
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
   
    def render(self, out_file):
        if self.kwargs == {}:
            out_file.write(f"<{self.tag} />\n")
        else:
            out_file.write(f"<{self.tag}")
            for key, value in self.kwargs.items():
                out_file.write(f' {key}="{value}"')
            out_file.write(f" />\n")
        

        





class Hr(SelfClosingTag):
    tag = "hr"




class Br(SelfClosingTag):
    tag = "br"


# Hr(width=400)
# To get this result:

# <hr width="400" />

#  def __init__(self, content=None, **kwargs ): #**kwargs key:value pairs("id = 'text'")
#         self.kwargs = kwargs
#         if content is None:
#             self.contents = []
#         else: 
#             self.contents = [content]


