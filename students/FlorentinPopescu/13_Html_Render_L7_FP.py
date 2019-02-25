# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 2019
@author: Florentin Popescu
"""
#===================LESSON_07====================

#================================================
# Part 1: HTML renderer
#================================================
class Element(object):
    tag = 'html'
    indent = "    "


#================================================    
# STEP 1
#------------------------------------------------    
    def __init__(self, content = None, **kwargs):
        self.contents = content
        
        if not self.contents:
            self.contents = []
        else:
            self.contents = [content]
        
        self.attributes = kwargs
        
#------------------------------------------------
    def append(self, new_content):
            self.contents += [new_content]
           
#------------------------------------------------
    def _open_tag(self):
        return "".join([f"<{self.tag}", "".join(f" {key}='{value}'" for key, value in self.attributes.items()), ">"])

#------------------------------------------------
    def _close_tag(self):
        return f"</{self.tag}>"

#------------------------------------------------
    def render(self, out_file, null_indent = ""):
        if self.tag == "html": 
            try:
                out_file.write("<!DOCTYPE html>\n")
            except IOError as io_err:
                print(f"I/O error({io_err.errno}): {io_err.strerror}")
                
        out_file.write("".join([f"{null_indent}{self._open_tag()}", "\n"]))
            
        for content in self.contents:
            try:
                content.render(out_file, "".join([null_indent, self.indent]))
            except (AttributeError, TypeError):
                out_file.write("".join([null_indent, self.indent, content]))
            except Exception as e:
                import sys, traceback, pbd
                raise type(e)("".join(str(e), f"happens in 'render'").with_traceback(sys.exc_info()))  
                traceback.print_stack()
                print(repr(traceback.extract_stack()))  
                print(repr(traceback.format_stack()))
                pbd.post_mortem()
          
        out_file.write("".join(["\n", null_indent, self._close_tag(), "\n"]))
 
           
#================================================
# STEP 2
#------------------------------------------------
class Html(Element):
    tag = "html"

#------------------------------------------------
class Body(Element):
    tag = "body"

#------------------------------------------------
class P(Element):
    tag = "p"


#================================================
# STEP 3
#------------------------------------------------
class Head(Element):
    tag = "head"


#================================================
# STEP 4
#------------------------------------------------
class OneLineTag(Element):
    def render(self, out_file, null_indent = ""):
        out_file.write("".join([f"{null_indent}{self._open_tag()}", self.contents[0], self._close_tag(), "\n"]))

    def append(self, content):
        raise NotImplementedError

#------------------------------------------------
class Title(OneLineTag):
    tag = "title"


#================================================
# STEP 5
#------------------------------------------------
class SelfClosingTag(Element):
    def __init__(self, content = None, **kwargs):
        if content:
            raise TypeError("SelfClosingTag cannot have content")
        super().__init__(content = content, **kwargs)

    def render(self, out_file, null_indent = ""):
        tag = "".join([self._open_tag()[ :-1], " />\n"])
        
        out_file.write("".join([f"{null_indent}{tag}", "\n"]))
        
        for content in self.contents:
            try:
                content.render(out_file)
            except (AttributeError, TypeError):
                out_file.write("".join([content, "\n"]))
            except Exception as e:
                import sys, traceback, pbd
                raise type(e)("".join(str(e), f"happens in 'render'").with_traceback(sys.exc_info()))  
                traceback.print_stack()
                print(repr(traceback.extract_stack()))  
                print(repr(traceback.format_stack()))
                pbd.post_mortem()
                    
        out_file.write("".join([f"{null_indent}{tag}", "\n"]))
    
    def append(self, *args): 
        raise TypeError("You cannot add content to SelfClosingTag")

#------------------------------------------------
class Hr(SelfClosingTag):
    #<hr />
    tag = "hr"

#------------------------------------------------
class Br(SelfClosingTag):
    #<br />
    tag = "br"


#================================================
# STEP 6
#------------------------------------------------
class A(OneLineTag):
    #<a link /a> 
    tag = "a"
    def __init__(self, link, content = None, **kwargs):
        kwargs["href"] = link
        super().__init__(content = content, **kwargs)


#================================================
# STEP 7
#------------------------------------------------
class Ul(Element):
    #Un-ordered list
    tag = "ul"

#------------------------------------------------
class Li(Element):
    #List item
    tag = "li"

#------------------------------------------------
class H(OneLineTag):
    def __init__(self, level, content = None, **kwargs):
        self.tag = f"h{level}"
        super().__init__(content = content, **kwargs)


#================================================
# STEP 8
#------------------------------------------------
class Meta(SelfClosingTag):
    #<meta />
    tag ="meta"


#================================================
#--------------- END ----------------------------
#================================================

