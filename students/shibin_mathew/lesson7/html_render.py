class Element:
    indentation = " "
    tag = ""

    def __init__(self, content=None, **kwargs):
        self.kwargs = kwargs
        if content is None:
            self.content = []
        else:
            self.content = [content]


    def append(self, string):
            self.content.append(string)

    def render(self, fileout, cur_ind="  "):
        try:
            fileout.write(cur_ind + f'{"<"}{self.tag}{" "}')
            for i, j in self.kwargs.items():
                fileout.write(' {}="{}"'.format(i,j))
            fileout.write(">\n")
            #
            for obj in self.content:
                if isinstance(obj, Element):
                    obj.render(fileout, cur_ind + self.indentation)
                else:
                    fileout.write(cur_ind + f' {obj}')
                    fileout.write("\n")
            fileout.write(cur_ind + "</{}>\n".format(self.tag))
        except IOError:
            print("Could not open the file "+fileout+'.txt')


class Html(Element):
    tag = 'html'

    def render(self, fileout, cur_ind="  "):
        try:
            fileout.write("<!DOCTYPE html>\n")
            Element.render(self, fileout, cur_ind="")
        except IOError:
            print("Could not open the file "+fileout+'.txt')


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, fileout, cur_ind="  "):
        try:
            fileout.write(cur_ind + f'{"<"}{self.tag}{" "}')
            for i, j in self.kwargs.items():
                fileout.write(f'{i} {"="} {j}')
            fileout.write(">")
            for obj in self.content:
                if isinstance(obj, Element):
                    obj.render(fileout, cur_ind + self.indentation)
                else:
                    fileout.write(cur_ind + f' {obj}')
            fileout.write(cur_ind + "</{}>\n".format(self.tag))
        except IOError:
            print("Could not open the file "+fileout+'.txt')


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("Self closing tag cannot have any content. Please remove them and try again!")
        else:
            self.kwargs = kwargs

    def render(self, fileout, cur_ind="  "):
        try:
            fileout.write(cur_ind + f'{"<"}{self.tag}{" "}')
            for i, j in self.kwargs.items():
                fileout.write(f'{i} {"="} {j}')
            fileout.write(" />\n")
        except IOError:
            print("Could not open the file "+fileout+'.txt')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class Meta(SelfClosingTag):
    tag = 'meta'


class A(Element):
    tag = 'a'

    def __init__(self, link, content):
        Element.__init__(self, content, href=link)

    def render(self, fileout, cur_ind = "  "):
        try:
            fileout.write(cur_ind + f'{"<"}{self.tag}{" "}')
            for i, j in self.kwargs.items():
                fileout.write(f'{i} {"="} {j}')
            fileout.write(" />")
        except IOError:
            print("Could not open the file "+fileout+'.txt')


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, level, content, **kwargs):
        OneLineTag.__init__(self, content, **kwargs)
        self.level = level
        self.tag = f'{"h"}{level}'

