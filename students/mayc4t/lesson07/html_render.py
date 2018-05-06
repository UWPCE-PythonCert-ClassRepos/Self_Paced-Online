#!/usr/bin/env python

class Element:
    tag = 'html'
    ind = 4
    content =""
    leaf_node=False


    def __init__(self, content=None, **kwargs):
        self.sub_elements = []
        if content:
            self.sub_elements = [content]
        
        self.style=''
        for key, value in kwargs.items():
            #print("The value of {} is {}".format(key, value))
            if 'style' in kwargs: self.stl = ' "style={}"'.format(kwargs['style'])
            #print (self.stl)


    def append( self, content ):
        self.sub_elements.append(content)

    def render( self, file_out, cur_ind='', new_line=True):
        if new_line :
            file_out.write("<{}{}>\n".format(self.tag, self.style))
            for idx_elm in self.sub_elements: 
                if self.leaf_node: file_out.write("{}\n".format(idx_elm))
                else: idx_elm.render(file_out, cur_ind)
        else: 
            file_out.write("<{}{}>".format(self.tag, self.style))
            for idx_elm in self.sub_elements:

                if self.leaf_node: file_out.write("{}".format(idx_elm))
                else: idx_elm.render(file_out, cur_ind)
        file_out.write("</{}>\n".format(self.tag))

    def dump(self):
        print('Element internals: tag=%s, sub_elements=%s' %
                (self.tag, self.sub_elements))


class Html(Element):
    tag = "html"
    leaf_node=False

class Body(Element):
    tag = "body"
    leaf_node=False

class P(Element):
    tag = 'p'
    leaf_node=True

class Head(Element):
    tag = "head"
    leaf_node = False

class OneLineTag(Element):
    onelinetag = True
    leaf_node=True
    tag = ""
    def render( self, file_out, cur_ind):
        super().render(file_out, cur_ind, False)

class Title(OneLineTag):
    tag="title"


class SelfClosingTag(Element):
    def __init__self( self, content=None, **kwargs ):

        if self.content is not None:
            raise TypeError
    
    def render( self, file_out, cur_ind='', new_line=True):
        file_out.write("< /{}>\n".format(self.tag))

class Hr(SelfClosingTag):
    tag = "hr"




