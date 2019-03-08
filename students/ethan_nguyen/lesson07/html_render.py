#!/usr/bin/env python3


class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind)
        file_out.write(self.text)

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "  "

    def __init__(self, content=None):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):

        out_file.write("{}<{}>\n".format(cur_ind, self.tag))

        for content in self.contents:    
            #try:
            if isinstance(content, Element):
                content.render(out_file, cur_ind + self.indent)
            else:
            #except AttributeError:
                out_file.write(cur_ind + self.indent + content)
            
            out_file.write("\n")

        out_file.write("{}</{}>\n".format(cur_ind, self.tag))
        out_file.write("\n")

"""Sub class from Element but override the render method"""
class OneLineTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        
        self.attributes = kwargs
    
    def _open_tag(self):
        return "<{}".format(self.tag)

    def _close_tag(self):
        return "</{}>".format(self.tag)

    def render(self, out_file, cur_ind=""):
        # loop through the list of contents:
        out_file.write(cur_ind + self._open_tag())
        
        if not self.attributes:
            out_file.write(">")

        for key, value in self.attributes.items():
            out_file.write(' {}="{}"'.format(key,value))

        out_file.write(self.contents[0])
        out_file.write(self._close_tag())

    #    out_file.write("<{}>".format(self.tag)) 
    #    out_file.write(self.contents[0])
    #    out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError

class A(OneLineTag):

    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Title(OneLineTag):

    tag = "title"

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
        #    self.contents = [content]
            super().__init__(content=content, **kwargs)

class Html(Element):

    def __init__(self, content=None):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def render(self, out_file, cur_ind=""):
        out_file.write("{}<{}>\n".format(cur_ind,"!DOCTYPE html"))
        super().render(out_file, cur_ind)

class Body(Element):
    tag = 'body'
    def __init__(self, content=None):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]


class P(Element):
    tag = 'p'
    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
    
        self.attributes = kwargs

    def render(self, out_file, cur_ind=""):

        out_file.write("{}<{}".format(cur_ind, self.tag))
        
        for key, value in self.attributes.items():
            out_file.write(' {}="{}"'.format(key,value))

        out_file.write(">\n")

        for content in self.contents:    
            #out_file.write("{}<{}>\n".format(cur_ind, self.tag))
            #try:
            if isinstance(content, Element):
                content.render(out_file, cur_ind,)
            else:
            #except AttributeError:
                out_file.write(cur_ind + self.indent + content)
            out_file.write("\n{}</{}>".format(cur_ind, self.tag))
            #out_file.write("\n")
        

class Ul(Element):

    tag = "ul"

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

        self.attributes = kwargs

    def render(self, out_file, cur_ind=""):

        out_file.write("{}<{}".format(cur_ind, self.tag))
        
        for key, value in self.attributes.items():
            out_file.write(' {}="{}"'.format(key,value))

        out_file.write(">\n")

        for content in self.contents:    
            #try:
            if isinstance(content, Element):
                content.render(out_file, cur_ind)
            else:
            #except AttributeError:
                out_file.write(self.tag + content)
        out_file.write("{}</{}>\n".format(cur_ind, self.tag))

class Li(Element):

    tag = 'li'

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

        self.attributes = kwargs

    def render(self, out_file, cur_ind=""):

        out_file.write("{}<{}".format(cur_ind, self.tag))
        
        for key, value in self.attributes.items():
            out_file.write(' {}="{}"'.format(key,value))

        out_file.write(">\n")

        for content in self.contents:    
            if isinstance(content, Element):
                content.render(out_file, cur_ind)
            else:
                out_file.write(cur_ind + content)
            out_file.write("\n")
        out_file.write("{}</{}>\n".format(cur_ind, self.tag))

class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):

        self.tag = "h" + str(level)
        if content is None:
            self.contents = []
        else:
        #    self.contents = [content]
            super().__init__(content=content, **kwargs)


class Head(Element):
    tag = 'head'

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
        #    self.contents = [content]
            super().__init__(content=content, **kwargs)


class SelfClosingTag(Element):
    
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def _open_tag(self):
        return "<{}\n".format(self.tag)

    def _close_tag(self):
        return "/{}>\n".format(self.tag)

    def render(self, out_file, cur_ind=""):
        # loop through the list of contents:
        out_file.write(cur_ind + self._open_tag())
        #out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind)
            except AttributeError:
                out_file.write(cur_ind + content)
                out_file.write("\n")
        out_file.write(cur_ind + self._close_tag())
        #out_file.write("\n")

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Hr(SelfClosingTag):
    
    tag = "hr"

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
    
        self.attributes = kwargs

    def render(self, outfile, cur_ind=""):

        tag = self._open_tag()[:-1] 

        for key, value in self.attributes.items():
            tag = tag + ' {}="{}"'.format(key,value)

        tag = cur_ind + tag + " />\n"
        outfile.write(tag)


class Br(SelfClosingTag):
    
    tag = "br"

    def render(self, outfile, cur_ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        outfile.write(cur_ind + tag)


class Meta(SelfClosingTag):

    tag = "meta"

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

        self.attributes = kwargs

    def render(self, out_file, cur_ind=""):

        tag = self._open_tag()[:-1] 
        for key, value in self.attributes.items():
            tag = tag + ' {}="{}"'.format(key,value)
            
        tag =  cur_ind + tag + " />\n"
        out_file.write(tag)
