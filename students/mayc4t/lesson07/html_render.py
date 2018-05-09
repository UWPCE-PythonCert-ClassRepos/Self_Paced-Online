#!/usr/bin/env python

class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, cur_ind='', new_line=True):
        out_str = self.text
        if new_line:
            out_str = "%s\n" % out_str
        file_out.write(out_str)

class Element:
    tag = 'html'
    ind = 4
    content =""


    def __init__(self, content=None, **kwargs):
        self.sub_elements = []
        if content and isinstance(content, str):
            self.sub_elements = [TextWrapper(content)]
        elif content:
            self.sub_elements = [content]
        
        self.attributes = ''
        for key, value in kwargs.items():
            self.attributes = '%s %s="%s"' % (self.attributes, key, value)


    def append( self, content ):
        if isinstance(content, str):
            self.sub_elements.append(TextWrapper(content))
        else:
            self.sub_elements.append(content)

    def render(self, file_out, cur_ind='', new_line=True):
        if new_line :
            file_out.write("<{}{}>\n".format(self.tag, self.attributes))
        else: 
            file_out.write("<{}{}>".format(self.tag, self.attributes))
        for idx_elm in self.sub_elements: 
            idx_elm.render(file_out, cur_ind, new_line)
        file_out.write("</{}>\n".format(self.tag))

    def dump(self):
        print('Element internals: tag=%s, sub_elements=%s' %
                (self.tag, self.sub_elements))


class Html(Element):
    tag = "html"
    def render(self, file_out, cur_ind='', new_line=True):
        file_out.write("<!DOCTYPE html>\n")
        super().render(file_out, cur_ind, new_line)

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    onelinetag = True
    tag = ""
    def render(self, file_out, cur_ind, parent_new_line):
        super().render(file_out, cur_ind, False)

class Title(OneLineTag):
    tag="title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs ):
        super().__init__()
        if content is not None:
            raise TypeError
    
    def render( self, file_out, cur_ind='', new_line=True):
        file_out.write("<{}{} />\n".format(self.tag, self.attributes))

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "hr"

class A(Element):
    tag = 'a'
    def __init__(self, link, content, **kwargs):
        super().__init__(content)
        self.link = link 

    def render( self, file_out, cur_ind='', new_line=True):
        file_out.write('<{} href="{}">{}</{}>\n'.format(
            self.tag, self.link, self.sub_elements[0].text,
            self.tag))

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = 'h'
    def __init__(self, level, content):
        super().__init__(content)
        self.tag += str(level)

class Meta(SelfClosingTag):
    tag='meta'
    def __init__(self, charset):
        super().__init__()
        self.tag += "charset={}".format(charset)

