
#!/usr/bin/env python3
from io import StringIO
class Element(object):
    tag = "html"
    indent = "    "
    def __init__(self, content=None, **kwargs):
        self.attrs = kwargs
        if content is None:
            self.content = []
        else:
            self.content = [content]
    
    def append(self, new_content):
        self.content.append(new_content)
    
    def render(self, file_out, cur_ind=""):
        # opening tag
        file_out.write('{}<{}'.format(cur_ind, self.tag))
        for key, value in self.attrs.items():
            file_out.write(" {}=\"{}\"".format(key, value))
        file_out.write('>\n')
        # content
        for item in self.content:
            # Checks if a sub element is here. If so, performs recursive render.
            if isinstance(item, Element):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write("{}\n".format(cur_ind + self.indent + item))
        # closing tag
        file_out.write('{}</{}>\n'.format(cur_ind, self.tag))

class Html(Element):
    tag = "html"
    def render(self,file_out, cur_ind=""):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out)

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        # opening tag
        file_out.write('{}<{}'.format(cur_ind, self.tag))
        for key, value in self.attrs.items():
            file_out.write(" {}=\"{}\"".format(key, value))
        file_out.write('>')
        # content
        for item in self.content:
            # Checks if a sub element is here. If so, performs recursive render.
            if isinstance(item, Element):
                item.render(file_out, cur_ind="")
            else:
                file_out.write("{}".format("" + item))
        # closing tag
        file_out.write('{}</{}>\n'.format("", self.tag))

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=""):
        file_out.write('{}<{}'.format(cur_ind, self.tag))
        for key, value in self.attrs.items():
            file_out.write(" {}=\"{}\"".format(key, value))
        file_out.write(' />\n')
        #file_out.write("{}<{} /> \n".format(cur_ind,self.tag))

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content):
        super().__init__(content, href = link)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = ''

    def __init__(self, level, content):
        self.tag = "h" + str(level)
        super().__init__(content)

class Meta(SelfClosingTag):
    tag = 'meta'


def test_render():
    f = StringIO()
    test_render = Body()
    test_render.render(f)
    page = f.getvalue()
    print(page)

test_render()