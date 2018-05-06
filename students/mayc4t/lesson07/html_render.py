#!/usr/bin/env python

class Element:
    tag = 'html'
    ind = 4
    content =""
    leaf_node=False


    def __init__(self, content=None):
        self.sub_elements = []
        if content:
            self.sub_elements = [content]


    def append( self, content ):
        self.sub_elements.append(content)

    def render( self, file_out, cur_ind=''):
        file_out.write("<{}>\n".format(self.tag))
        for idx_elm in self.sub_elements: 
            if self.leaf_node:
                file_out.write(idx_elm)
            else:
                idx_elm.render(file_out, cur_ind)
        file_out.write("</{}>\n".format(self.tag))

    def dump(self):
        print('Element internals: tag=%s, sub_elements=%s' %
                (self.tag, self.sub_elements))


class Html(Element):
    tag = "Html"
    leaf_node=False

class Body(Element):
    tag = "body"
    leaf_node=False

class P(Element):
    tag = 'P'
    leaf_node=True
