#!/usr/bin/env python3

class Element:

    tag = "html"
    indent = 4
    
    def __init__(self, content=None):
        self.content = []
        if not content is None:
            self.content.append(content)
        
    def append(self, content):
        self.content.append(content)
        
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}>\n".format(self.tag))
        sub_ind = cur_ind + (Element.indent * ' ')
        for entry in self.content:
            file_out.write(sub_ind + entry + "\n")
        file_out.write(cur_ind + "<\{}>".format(self.tag))