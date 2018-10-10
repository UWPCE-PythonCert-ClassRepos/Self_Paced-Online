#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
#  --- Step1-------------------
class Element(object):
    tag = "html"
    ind = '   '
    
    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        print("contents is:", self.contents)
        self.kwargs = kwargs
        print("kwargs are", self.kwargs)
    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, file_out, cur_ind=''):
        # loop through the list of contents:
        open_tag = ["<{}".format(self.tag)]     #added in step 4
        open_tag.append(">\n")                  #added in step 4
        file_out.write("".join(open_tag))        #added in step 4
#        file_out.write("<{}>\n".format(self.tag)) # over written in step4
        for k, v in self.kwargs.items():
            file_out.write(' {}="{}"'.format(k, v))
        file_out.write('>\n')        
        for content in self.contents:
            try:
                content.render(file_out, f'{cur_ind}{self.ind}')
            except AttributeError:
                file_out.write(f'{cur_ind}{self.ind}{str(content)}\n')
        file_out.write(f'{cur_ind}</{self.tag}>\n')
        
    def add_attrs(self, file_out, cur_ind):
        """Add attributes."""
        file_out.write(f'{cur_ind}<{self.tag}')
        for k, v in self.attrs.items():
            file_out.write(' {}="{}"'.format(k, v))    
    
 #  --- Step2-------------------
class Html(Element):     #Common practice of Cap_1 for classes and subclasses
    tag = "html"
    
    def render(self, file_out, cur_ind=''):
        file_out.write(f'{cur_ind}<!DOCTYPE html>\n')
        super().render(file_out, cur_ind)
        
class Body(Element):   #entire contents of an html page subclass
    tag = "body"


class P(Element):   #paragraph element subclass
    tag = "p"


#  --- Step3-/-Step4------------------
class Head(Element):     #Common practice of Cap_1 for classes and subclasses
    tag = "head"

    
class OneLineTag(Element):
    tag = "oneliner"
    def render(self, file_out, cur_ind='', **kwargs):   # Introduce key wordarguments
#    def render(self, file_out):    # Updated above
        def append(self, content, cur_ind):
            raise NotImplementedError         
        file_out.write("<{}>".format(self.tag))
        
        for k, v in self.kwargs.items():    # extract Attributes for test
            file_out.write(' {}="{}"'.format(k, v))
        file_out.write('>\n')
        
        file_out.write(self.contents[0])
        file_out.write("</{}>\n".format(self.tag))
#        file_out.write('\t<' + self.tag +'>' + self.content[0] + '</' + self.tag + 'v>\n') 
#          Note: compression above is equivelant of render class detail above            

class Title(Element):
    tag = "title"
    
#  --- Step5---Self Closing Tag, line Break-/horizontal rule---------------

class SelfClosingTag(Element):
    
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")
 
    def render(self, file_out, cur_ind='', **kwargs):
        file_out.write(cur_ind + f'<{self.tag}')
        for k, v in self.kwargs.items():
            file_out.write(' {}="{}"'.format(k, v))
        file_out.write(' />\n')   


class Hr(SelfClosingTag):   # horizontal rule 
    tag = "hr"

class Br(SelfClosingTag):   # line break
    tag = "br"

#  --- Step6---Link---------------

class A(Element):  # 'Not sure how to include second content "link" in report
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        super().__init__(content, **kwargs)
        
    def render(self, file_out, cur_ind='', **kwargs):  # could not get _Open/_Close_tag to work
        file_out.write(cur_ind + f'<{self.tag}')
        for k, v in self.kwargs.items():
            file_out.write(' {}="{}"'.format(k, v))
        file_out.write(' />\n')       


#  --- Step7---list elements---------------

class Ul(Element):
    tag = "u_list"
    
class Li(Element):
    tag = "l_elem"

#class Header(OneLineTag): #Note: "Header" from instrutions. "H" to match run file
class H(OneLineTag):
    def __init__(self, level, content):
        super().__init__(content)
        self.tag = f'h{level}'
               
        
#  --- Step8---DOC Type---------------
#  insert above:  file_out.write(f'{cur_ind}<!DOCTYPE html>\n')
#  ----------------------------------
class Meta(SelfClosingTag):  #Note: Required to address character set
    def __init__(self, charset):
        self.tag = 'meta' + ' charset="' + charset + '"'
        Element.__init__(self)

#  --- Step9---adding Indentation--------------


