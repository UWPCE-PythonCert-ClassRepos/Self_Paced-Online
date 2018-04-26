#!/usr/bin/env python3

# file: html_render.py

class Element:
    tag = 'element'

    def __init__(self, content=None):       # wird erzeugt und kann schon content uebergeben 
                                            # bekommen, siehe Step2 body.append(hr.P("blabla...")
        self.content = [content] if content else []
    
    def append(self, stuff):
        self.content.append(stuff)

    def render(self, io, ind):
        io.write('<{}>\n'.format(self.tag))
            
        for i in self.content:
            if hasattr(i, 'render'):
                i.render(io, ind)
            else:
                line = '{}{}\n'.format(ind, i)
                io.write(line)
        io.write('</{}>\n'.format(self.tag))
        

class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class Title(Element):
    tag = 'title'



class OneLineTag(Element):
    pass 







