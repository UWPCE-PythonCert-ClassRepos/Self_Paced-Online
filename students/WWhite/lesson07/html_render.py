/>:class Element:
    indentation = "  "
    tag_class = ""
    attributes = ""

    def __init__(self, content=None, **kwargs):
        if content:
            self.content = [content]
            for key, value in kwargs.items():
                self.attributes += ' {}="{}"'.format(key, value)
        else:
            self.content = []

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + '<{}'.format(self.tag_class) + self.attributes+'>'+"\n")
        for x in self.content:
            if type(x) is str:
                file_out.write(cur_ind + x +"\n")

            elif hasattr(x, 'render'):
                x.render(file_out, cur_ind+self.indentation)

        file_out.write(cur_ind +'</{}>'.format(self.tag_class) +"\n")

    def append(self, append_content):
        self.content.append((append_content))


# subclassess
class Html(Element):
    tag_class = "html"

    def render(self, file_out, cur_ind=""):
        file_out.write("<!DOCTYPE html>\n")
        super(Html, self).render(file_out, cur_ind)


class Body(Element):
    tag_class = "body"


class P(Element):
    tag_class = "p"


class Head(Element):
    tag_class = "head"


class Ul(Element):
    tag_class = "ul"


class Li(Element):
    tag_class = "li"


class OneLineTag(Element):   
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind+"<{}".format(self.tag_class) + self.attributes + ">"+"</{}>\n".format(self.tag_class))


class Title(OneLineTag):
    tag_class = "title"


class H(OneLineTag):
    tag_class = "h"

    def __init__(self, headerLevel, content=None):
        self.tag_class += str(headerLevel)
        super(H, self).__init__(content)


class SelfClosingTag(Element):   
    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError("Element cannot have content!")
        else:
            for key, value in kwargs.items():
                self.attributes += ' {}="{}"'.format(key, value)

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind+"<{}".format(self.tag_class) + self.attributes + "/>\n")


class Hr(SelfClosingTag):
    tag_class = "hr"


class Br(SelfClosingTag):
    tag_class = "br"


class Meta(SelfClosingTag):
    tag_class = "meta"


class A(Element):
    tag_class = "a"

    def __init__(self, href=None, content=None):
        if content:
            self.content = [content]
            self.attributes = ' href="'+href+'"'
