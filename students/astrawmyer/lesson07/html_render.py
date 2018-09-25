#!/usr/bin/env python3

class Element(object):
    tag = "html"
    indent = "    "
    def __init__(self,content=None):
        self.content = []
    
    def append(self, new_content):
        self.content.append(new_content)
    
    def render(self,file_out,cur_ind=""):
        file_out.write(cur_ind + "<html>")
        for item in self.content:
            file_out.write('{}</html>\n'.format(item))


""" test_element = Element()
test_element.append("This is content.")
test_element.append("This is more content.")
render(test_element,"test_html_output1.html") """