# lesson 07 html render
# !/usr/bin/env python3


# Step 1
class Element(object):
    def __init__(self, content=None, **kwargs):
        self.tag_name = ""
        self.kwargs = ""
        self.indent = "    "
        if kwargs != {}:
            for key in kwargs:
                self.kwargs += " " + str(key) + "=" + "'" + str(kwargs[key]) + "'"            
        if content is None:
            self.content = []
        else:
            self.content = [content]
    def __repr__(self):
        full_string = ""
        full_string += "<" + self.tag_name + self.kwargs + ">"
        full_string += "\n"
        for c in self.content:
            full_string += str(c)
            full_string += "\n"
        full_string += "</" + self.tag_name + ">"
        return full_string
    def append(self, new_content):
        self.content.append(new_content)
    def render(self, out_file, cur_ind=""):
        cur_ind += self.indent
        out_file.write(cur_ind + "<" + self.tag_name + self.kwargs + ">")
        out_file.write("\n")
        for c in self.content:
            out_file.write(cur_ind + str(c))
            out_file.write("\n")
        out_file.write(cur_ind + "</" + self.tag_name + ">")

# Step 2
class Html(Element):
    def __init__(self, content=None, **kwargs):
        super(Html, self).__init__(content=content, **kwargs)
        self.tag_name = "html"
    def render(self, out_file, cur_ind=""):
        cur_ind += self.indent
        out_file.write("<!DOCTYPE html>\n")
        out_file.write("<" + self.tag_name + ">")
        out_file.write("\n")
        for c in self.content:
            out_file.write(cur_ind + str(c))
            out_file.write("\n")
        out_file.write("</" + self.tag_name + ">")


class Body(Element):
    def __init__(self, content=None, **kwargs):
        super(Body, self).__init__(content=content, **kwargs)
        self.tag_name = "body"

class P(Element):
    def __init__(self, content=None, **kwargs):
        super(P, self).__init__(content=content, **kwargs)
        self.tag_name = "p"

# Step 3
class Head(Element):
    def __init__(self, content=None, **kwargs):
        super(Head, self).__init__(content=content, **kwargs)
        self.tag_name = "head"
 
class OneLineTag(Element):
    def __repr__(self):
        full_string = ""
        full_string += "<" + self.tag_name + ">"
        for c in self.content:
            full_string += str(c)
        full_string += "</" + self.tag_name + ">"
        return full_string
    def render(self, out_file, cur_ind=""):
        cur_ind += self.indent
        out_file.write(cur_ind + "<" + self.tag_name + ">")
        for c in self.content:
            out_file.write(str(c))
        out_file.write("</" + self.tag_name + ">")

class Title(OneLineTag):
    def __init__(self, content=None, **kwargs):
        super(Title, self).__init__(content=content, **kwargs)
        self.tag_name = "title"

# Step 5
class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        super(SelfClosingTag, self).__init__(content=content, **kwargs)
        if self.content: raise TypeError
    def __repr__(self):
        full_string = ""
        full_string += "<" + self.tag_name + self.kwargs + " />"
        return full_string
    def render(self, out_file, cur_ind=""):
        cur_ind += self.indent
        out_file.write(cur_ind + "<" + self.tag_name + self.kwargs + " />")

        
class Hr(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        super(Hr, self).__init__(content=content, **kwargs)
        self.tag_name = "hr"

class Br(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        super(Br, self).__init__(content=content, **kwargs)
        self.tag_name = "br"

# Step 6
class A(Element):
    def __init__(self, link, content=None, **kwargs):
        super(A, self).__init__(content=content, **kwargs)
        self.tag_name = "a"
        self.link = link
    def __repr__(self):
        full_string = ""
        full_string += "<" + self.tag_name + " href=" + self.link + ">"
        for c in self.content:
            full_string += str(c)
        full_string += "</" + self.tag_name + ">"
        return full_string
    def render(self, out_file, cur_ind=""):
        cur_ind += self.indent
        out_file.write(cur_ind + "<" + self.tag_name + " href=" + self.link + ">")
        for c in self.content:
            out_file.write(str(c))
        out_file.write(cur_ind + "</" + self.tag_name + ">")

# Step 7
class Ul(Element):
    def __init__(self, content=None, **kwargs):
        super(Ul, self).__init__(content=content, **kwargs)
        self.tag_name = "ul"

class Li(Element):
    def __init__(self, content=None, **kwargs):
        super(Li, self).__init__(content=content, **kwargs)
        self.tag_name = "li"

class H(OneLineTag):
    def __init__(self, intg, content=None, **kwargs):
        super(H, self).__init__(content=content, **kwargs)
        self.tag_name = "h"
        self.intg = intg
    def __repr__(self):
        full_string = ""
        full_string += "<" + self.tag_name + str(self.intg) + ">"
        for c in self.content:
            full_string += str(c)
        full_string += "</" + self.tag_name + str(self.intg) + ">"
        return full_string
    def render(self, out_file, cur_ind=""):
        cur_ind += self.indent
        out_file.write(cur_ind + "<" + self.tag_name + str(self.intg) + ">")
        for c in self.content:
            out_file.write(cur_ind + str(c))
        out_file.write(cur_ind + "</" + self.tag_name + str(self.intg) + ">")

# Step 8
class Meta(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        super(Meta, self).__init__(content=content, **kwargs)
        self.tag_name = "meta"
        self.kwargs = ""
        if kwargs != {}:
            for key in kwargs:
                self.kwargs += " " + str(key) + "=" + "'" + str(kwargs[key]) + "'"            
        if content is None:
            self.content = []
        else:
            self.content = [content]
    def __repr__(self):
        full_string = ""
        full_string += "<" + self.tag_name + self.kwargs + " />"
        return full_string