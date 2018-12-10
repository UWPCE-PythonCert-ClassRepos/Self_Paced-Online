class Element:
    tag = "html"
    indent = "   "

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.attributes = {}
        if content:
            self.content.append(content)
        if kwargs:
            self.attributes = kwargs

    def append(self, content):
        if content:
            self.content.append(content)

    def render(self, file_out, cur_ind=""):
        file_out.write(f"{cur_ind}<{self.tag}{self.render_attributes()}>\n")
        for item in self.content:
            if issubclass(type(item), Element):
                item.render(file_out, cur_ind+self.indent)
            else:
                file_out.write(f"{cur_ind}{self.indent}{item}\n")
        file_out.write(cur_ind+"</"+self.tag+">\n")

    def render_attributes(self):
        res_string = ""
        for attr, value in self.attributes.items():
            if attr == "clas":
                attr = "class"
            res_string += f' {attr}="{value}"'
        return res_string


class Html(Element):
    tag = "html"

    def __init__(self, content=None, ind=3, **kwargs):
        Element.indent = " "*ind
        super().__init__(content, **kwargs)

    def render(self, file_out, cur_ind=""):
        file_out.write(f"{cur_ind}<!DOCTYPE html>\n")
        super().render(file_out, cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        content = " ".join(self.content)
        file_out.write(f"{cur_ind}<{self.tag}{self.render_attributes()}>{content}</{self.tag}>\n")


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError("'SelfClosingTag' object cannot have any content")
        super().__init__(content, **kwargs)

    def append(self, content):
        raise TypeError("'SelfClosingTag' object cannot have any content")

    def render(self, file_out, cur_ind=""):
        file_out.write(f"{cur_ind}<{self.tag}{self.render_attributes()} />\n")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content):
        super().__init__(content, href=link)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):
    def __init__(self, level, content, **kwargs):
        self.tag = f"h{int(level)}"
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    tag = "meta"
