#!/usr/bin/env python3

class Element(object):
    tag = "html"
    indent = "    "
    def __init__(self,content=None, **kwargs):
        self.attrs = kwargs
        if content is None:
            self.content = []
        else:
            self.content = [content]
    
    def append(self, new_content):
        self.content.append(new_content)
    
    def render(self,file_out,cur_ind=""):
        # opening tag
        file_out.write('{}<{}'.format(cur_ind,self.tag))
        for key, value in self.attrs.items():
            file_out.write(" {}=\"{}\"".format(key, value))
        file_out.write('>\n')
        # content
        for item in self.content:
            # Checks if a sub element is here. If so, performs recursive render.
            if isinstance(item, Element):
                item.render(file_out, cur_ind="    ")
            else:
                file_out.write("{}\n".format("    " + item))
        # closing tag
        file_out.write('{}</{}>\n'.format(cur_ind,self.tag))



#subclasses for part 2
class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

# Subclasses for part 3

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self,file_out,cur_ind=""):
        # opening tag
        file_out.write('{}<{}>'.format(cur_ind,self.tag))
        # content
        for item in self.content:
            # Checks if a sub element is here. If so, performs recursive render.
            if isinstance(item, Element):
                item.render(file_out, cur_ind="    ")
            else:
                file_out.write("{}".format("    " + item))
        # closing tag
        file_out.write('{}</{}>\n'.format(cur_ind,self.tag))

class Title(OneLineTag):
    tag = "title"
