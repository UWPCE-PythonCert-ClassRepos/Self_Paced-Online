#-------------------------------------------------#
# Title: HTML Renderer
# Dev:   LDenney
# Date:  November 14, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 11/14/18, Started HTML Renderer Work
#-------------------------------------------------#

class Element(object):
    tag_name = "html"
    indent = "    "

    def __init__(self, content = None, **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        if kwargs:
            self.attributes = kwargs
        else:
            self.attributes = None

    def __str__(self):
        return self.content, self.attributes

    def append(self,something):
        self.content.append(something)

    @staticmethod
    def dic_to_tuple(dic):
        tupl = ()
        try:
            for key,value in dic.items():
                tupl += (key,)
                tupl += (value,)
            return tupl
        except AttributeError:
            return None

    def render(self, file_out, cur_ind= ""):
        attr_tupl = Element.dic_to_tuple(self.attributes)
        try:
            tag_str = "{}<{} " + " ".join(['{}="{}"'] * len(self.attributes)) + ">\n"
            file_out.write(tag_str.format(cur_ind, self.tag_name, *attr_tupl))
        except AttributeError:
            file_out.write("{}<{}>\n".format(cur_ind,self.tag_name))
        except TypeError:
            file_out.write("{}<{}>\n".format(cur_ind,self.tag_name))
        for element_content in self.content:
            if type(element_content) is str:
                file_out.write('{}{}\n'.format(cur_ind +self.indent,element_content))
            else: element_content.render(file_out, cur_ind + self.indent)
        file_out.write("{}</{}>\n".format(cur_ind,self.tag_name))

#Step 2
class Html(Element):
    tag_name = "html"

    def render(self, file_out, cur_ind = ""):
        file_out.write("{}<!DOCTYPE html>\n".format(cur_ind))
        Element.render(self, file_out, cur_ind)

class Body(Element):
    tag_name = "body"

class P(Element):
    tag_name = "p"

#Step 3
class Head(Element):
    tag_name = "head"

class OneLineTag(Element):

    def render(self, file_out, cur_ind = ""):
        tempstr = "{}<{}> {} </{}>\n".format(cur_ind,self.tag_name, self.content[0], self.tag_name)
        file_out.write(tempstr)

class Title(OneLineTag):
    tag_name = "title"

#Step 5
class SelfClosingTag(Element):
    def __init__(self, content = None, **kwargs):
        if content:
            raise TypeError
            print("SelfClosingTag cannot have content")
        else:
            Element.__init__(self, content, **kwargs)

    def render(self, file_out, cur_ind = ""):
        attr_tupl = Element.dic_to_tuple(self.attributes)
        try:
            tag_str = "<{} " + " ".join(['{}="{}"'] * len(self.attributes)) + " />\n"
            file_out.write(tag_str.format(self.tag_name, *attr_tupl))
        except AttributeError:
            file_out.write("<{} />\n".format(self.tag_name))
        except TypeError:
            file_out.write("<{} />\n".format(self.tag_name))

class Hr(SelfClosingTag):
    tag_name = 'hr'

class Br(SelfClosingTag):
    tag_name = 'br'

#Step 6
class A(Element):
    tag_name = 'a'

    def __init__(self, link, content):
        Element.__init__(self, content, href= link)

#Step 7
class Ul(Element):
    tag_name ='ul'

class Li(Element):
    tag_name = 'li'

class H(OneLineTag):

    def __init__(self, int, content=None):
        self.tag_name = 'h{}'.format(str(int))
        OneLineTag.__init__(self,content)

#Step 8
class Meta(SelfClosingTag):
    tag_name = 'meta'