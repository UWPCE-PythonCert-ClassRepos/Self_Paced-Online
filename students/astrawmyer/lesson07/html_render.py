#!/usr/bin/env python3

class Element(object):
    tag = "html"
    indent = "    "
    def __init__(self,content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
    
    def append(self, new_content):
        self.content.append(new_content)
    
    def render(self,file_out,cur_ind=""):
        #opening tag
        file_out.write('{}<{}>\n'.format(cur_ind,self.tag))
        #content
        for item in self.content:
            print(item)
            if isinstance(item, Element):
                item.render(file_out)
            else:
                file_out.write("{}\n".format(item))
        #closing tag
        file_out.write('{}</{}>\n'.format(cur_ind,self.tag))



#subclasses for part 2
class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"


""" test_element = Element()
test_element.append("This is content.")
test_element.append("This is more content.")
test_element.render(test_element,"test_html_output1.html") """

