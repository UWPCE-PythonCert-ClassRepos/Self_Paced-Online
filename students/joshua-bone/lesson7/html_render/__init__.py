def writeline(file_out, line):
    file_out.write(line + "\n")


class Element:
    tag = "default-tag"
    ind = "  "

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.attributes = {}
        if content:
            self.append(content)
        if kwargs is not None:
            self.attributes.update(kwargs)

    def append(self, content):
        if isinstance(content, (list, tuple)):
            self.content.extend(content)
        else:
            self.content.append(content)

    def open_tag(self):
        s = f"<{self.tag}"
        for a in self.attributes:
            s += f" {a}=\"{self.attributes[a]}\""
        s += ">"
        return s

    def close_tag(self):
        return f"</{self.tag}>"

    def render(self, file_out, cur_ind=""):
        writeline(file_out, cur_ind + self.open_tag())
        for c in self.content:
            new_ind = cur_ind + self.ind
            if issubclass(type(c), Element):
                c.render(file_out, new_ind)
            else:
                writeline(file_out, new_ind + c)
        writeline(file_out, cur_ind + self.close_tag())


class Html(Element):
    tag = "html"

    def render(self, file_out, cur_ind=""):
        writeline(file_out, cur_ind + "<!DOCTYPE html>")
        super(Html, self).render(file_out, cur_ind)


class Head(Element):
    tag = "head"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        s = self.open_tag()
        for c in self.content:
            s += f" {c}"
        s += " " + self.close_tag()
        writeline(file_out, cur_ind + s)


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def append(self, content):
        raise TypeError("Cannot add content to a self-closing tag.")

    def render(self, file_out, cur_ind=""):
        writeline(file_out, cur_ind + self.open_tag())


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(Element):
    tag = "a"

    def __init__(self, link, content):
        super().__init__(content, **{"href": link})


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):
    def __init__(self, size, content):
        self.tag = "h" + str(size)
        super().__init__(content)


class Meta(SelfClosingTag):
    tag = "meta"

    def __init__(self, charset):
        super().__init__(**{"charset": charset})
