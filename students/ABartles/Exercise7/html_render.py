

class Element():
    tag = ""

    def __init__(self, content=None, **kwargs):
        self.attr = kwargs
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, str):
        self.content.append(str)

    def _open_tag(self, close=False, cur_ind=""):
        open_tag = ["{}<{}".format(cur_ind, self.tag)]
        for k, v in self.attr.items():
            open_tag.append(" {}='{}'".format(k, v))
        if close is False:
            open_tag.append(">")
        else:
            open_tag.append("/>")
        open_tag_str = "".join(open_tag)
        return open_tag_str

    def _close_tag(self, cur_ind=""):
        close_tag = "{}</{}>".format(cur_ind, self.tag)  # curind
        return close_tag

    def render(self, file_out, cur_ind=""):
        file_out.write(self._open_tag(False, cur_ind))
        file_out.write("\n")
        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write("{} ".format(item))
                file_out.write("\n")
        file_out.write(self._close_tag(cur_ind))
        file_out.write("\n")


class Html(Element):
    tag = "html"
    # ind = ""

    def render(self, file_out, cur_ind=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, cur_ind)


class Body(Element):
    tag = "body"
    # ind = "    "


class P(Element):
    tag = "p"
    # ind = "        "


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        file_out.write(self._open_tag(False, cur_ind))
        file_out.write("{}. ".format(self.content[0]))
        file_out.write(self._close_tag(cur_ind))
        file_out.write("\n")


class Title(OneLineTag):
    tag = "Title"


class SelfClosingTag(Element):
    def __init__(self, **kwargs):
        self.attr = kwargs

    def append(self, str):
        raise TypeError("No content allowed with self closing tags.")

    def render(self, file_out, cur_ind=""):
        file_out.write(self._open_tag(True, cur_ind))
        file_out.write("\n")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(Element):
    tag = "a"

    def __init__(self, link, content=None):
        self.link = link
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def render(self, file_out, cur_ind=""):
        file_out.write("{}<{} href='{}'>".format(cur_ind, self.tag, self.link))
        file_out.write("\n")
        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write("{} ".format(item))
                file_out.write("\n")
        file_out.write(self._close_tag(cur_ind))
        file_out.write("\n")


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        self.tag = ("h{}".format(level))
        self.attr = kwargs
        if content is None:
            self.content = []
        else:
            self.content = [content]


class Meta(SelfClosingTag):
    tag = "meta"
