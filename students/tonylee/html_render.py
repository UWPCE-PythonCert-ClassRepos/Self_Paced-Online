class Element:

    # Class Attributes
    tag = ""
    indent = "  "

    def __init__(self, content=None, **style):
        self.content = [content] if content else []
        self.styles = style


    def append(self, words):
        self.content.append(words)

    def render(self, fileout, cur_ind=""):
        fileout.write(cur_ind + "<{}".format(self.tag))

        for key, value in self.styles.items():
            fileout.write(' {}="{}"'.format(key,value))
        fileout.write(">\n")

        for item in self.content:
            if isinstance(item, Element):
                item.render(fileout, cur_ind + self.indent)
            else: # output the content
                fileout.write(cur_ind + self.indent + item)
                fileout.write("\n")

        fileout.write(cur_ind + "</{}>\n".format(self.tag))

class Html(Element):
    tag = 'html'

    def render(self, fileout, cur_ind=""):
        fileout.write("<!DOCTYPE html>\n")
        Element.render(self, fileout, cur_ind="")

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class SelfClosingTag(Element):

    def __init__(self, **style):
        ''' SelfClosingTag no content required '''
        self.styles = style

    def render(self, fileout, cur_ind=""):
        fileout.write(cur_ind + "<{}".format(self.tag))
        for key, value in self.styles.items():
            fileout.write(' {}="{}"'.format(key,value))
        fileout.write(" />\n")

class OneLineTag(Element):

    def render(self, fileout, cur_ind=""):
        ''' Makes this Element all in one line '''
        fileout.write(cur_ind + "<{}".format(self.tag))
        for key, value in self.styles.items():
            fileout.write(' {}="{}"'.format(key,value))
        fileout.write(">")
        for item in self.content:
            if isinstance(item, Element):
                item.render(fileout, cur_ind + self.indent)
            else: # output the content
                fileout.write(item)

        fileout.write("</{}>\n".format(self.tag))

class Title(OneLineTag):
    tag = 'title'

class Meta(SelfClosingTag):
    tag = 'meta'

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(Element):
    tag = 'a'

    def __init__(self, link, content):
        Element.__init__(self, content, href=link)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):

    def __init__(self, size, content, **style):
        OneLineTag.__init__(self, content, **style)
        self.size = size
        self.tag = "h{}".format(size)
