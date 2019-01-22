from io import StringIO


class Element:
    tag=""
    tab_indent = "\t"

    def __init__(self, content_list="", **kwargs):
        self.content_list = [content_list]
        self.kwargs = kwargs

    def append(self, list_item):
        self.content_list.append(list_item)

    def render(self, file_out, cur_ind=""):
        if self.kwargs=={}:
            file_out.write(cur_ind + f"<{self.tag}>")
        else:
            style_list = ' '.join(f'{k}="{v}"' for k, v in self.kwargs.items())
            file_out.write(cur_ind + f"<{self.tag} {style_list}>")
        counter = 0
        #obj + str
        for mc in self.content_list:
            if type(mc) != str:  # washes out to tags
                mc.render(file_out, cur_ind + self.tab_indent)
            else:
                file_out.write(mc)
            file_out.write('\n')
            counter = counter + 1
        file_out.write(cur_ind + f"</{self.tag}>")


def render_page(HtmlPage, filename, indent=None):
    f = StringIO() # StringIO object (like a file, but in memory) to render to memory
    if indent is None:
        HtmlPage.render(f)
    else:
        HtmlPage.render(f, indent)
    print(f.getvalue())
    with open(filename, 'w') as outfile:
        outfile.write(f.getvalue())


class A(Element):
    tag = 'a'

    def __init__(self, link, content):
        super().__init__(content, href=link)


class Html(Element):
    tag="html"

    def render(self, file_out, cur_ind=""):
        file_out.write("<!DOCTYPE html>\n")
        super().render(file_out, cur_ind)


class Body(Element):
    tag="body"


class P(Element):
    tag="p"


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def __init__(self, content=""):
        self.content = content

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + f"<{self.tag}> {self.content} </{self.tag}>")


class H(OneLineTag):
    def __init__(self, num ,content):
        self.tag = 'h' + str(num)
        OneLineTag.__init__(self, content)

class Title(OneLineTag):
    tag = 'title'


class Singleton(Element):
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + f"<{self.tag} />")


class SelfClosingTag(Element):
    def __init__(self, content="", **kwargs):
        self.content = content
        self.kwargs = kwargs

    def render(self, file_out, cur_ind=''):
        if self.kwargs == {}:
            file_out.write(f"{cur_ind}<{self.tag} />\n")
        else:
            style_list = ' '.join(f'{k}="{v}"' for k, v in self.kwargs.items())
            file_out.write(cur_ind + f"<{self.tag} {style_list}/>")



class Hr(SelfClosingTag):
    tag="hr"


class Br(SelfClosingTag):
    tag="br"


class Meta(SelfClosingTag):
    tag = 'meta'

class Ul(Element):
    tag="ui"


class Li(Element):
    tag="li"

