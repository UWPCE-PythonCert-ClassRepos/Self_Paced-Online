# Description: html render
# Author: Andy Kwok
# Last Updated: 08/29/2018
# ChangeLog: Initialization

import sys

class Element:
    tag = 'html'
    
    def __init__(self, content = None, **kwargs):
        self.content = [content] if content else []
        self.indent = "    "
        self.kwargs = kwargs

    def append(self, add_text):
        self.content.append(add_text)
             
    def render(self, file_out, cur_ind = ''):
        cur_ind = self.indent        
        if self.kwargs == {}:
            file_out.write('<' + self.tag + '>\n') 
        else:
            for keys, value in self.kwargs.items():
                file_out.write('<' + self.tag + ' ' + keys + '="' + value + '">\n')
        for insert_text in self.content:
            if isinstance(insert_text, str):
                file_out.write(self.indent + insert_text + '\n')
            else:
                insert_text.render(file_out) 
        file_out.write('</' + self.tag + '>\n')     

class Html(Element):
    tag = 'html'
    def render(self, file_out, cur_ind = ''):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out, cur_ind = '')
    

class Body(Element):
    tag = 'body'
    pass    

class P(Element):
    tag = 'p'
    pass

class Head(Element):
    tag = 'head'
    pass
    
class OneLineTag(Element):
    def render(self, file_out):
        file_out.write('<' + self.tag + '>' + self.content[0] + '</' + self.tag + '>\n')
    
class Title(OneLineTag):
    tag = 'title'
    pass
    
class SelfClosingTag(Element):
    def render(self, file_out):
        file_out.write('<' + self.tag + ' />\n')
        try:
            if self.content:
                self.content + ' '
        except:
            print('TypeError.....')
            sys.exit(1)
            
                
class Hr(SelfClosingTag):
    tag = 'hr'
    pass

class A(Element):
    tag = 'a'
    def __init__(self, link, content):
        kwargs = {'href': link}
        Element.__init__(self, content, **kwargs)  

class Ul(Element):
    tag = 'ul'
    pass

class Li(Element):
    tag = 'li'
    pass
    
class H(OneLineTag):
    def __init__(self, num ,content):
        self.tag = 'h' + str(num)
        OneLineTag.__init__(self, content)
 
class Meta(SelfClosingTag):
    def __init__(self, charset):
        self.tag = 'meta' + ' charset="' + charset + '"'
        Element.__init__(self)
    pass
