class Element:
    # attributes
    tag_name = "html"
    indent = "    "

    # init method
    def __init__(self, content=None, **attributes):
        self.attributes = attributes
        if content:
            self.contents = [content]
        else:
            self.contents = []

    # append method
    def append(self, new_content):
        self.contents.append(new_content)

    # render method
    def render(self, out_file, cur_ind=""):
        # Loop through the list of contenst:
        out_file.write(cur_ind + self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(self.indent + cur_ind + content)
                out_file.write("\n")
        out_file.write(cur_ind + self._close_tag())
        out_file.write("\n")

    def format_attributes(self):
        if self.attributes:
            myattr = ""
            for k, v in self.attributes.items():
                mystr = '{}="{}"'.format(k, v)
                myattr += " " + mystr
        else:
            myattr = ''
        return myattr

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag_name)]
        open_tag.append(self.format_attributes())
        open_tag.append(">")
        mystr = ("".join(open_tag))
        return mystr

    def _close_tag(self):
        close_tag = "</{}>".format(self.tag_name)
        return close_tag


class Html(Element):
    tag_name = 'html'
    def render(self, out_file, cur_ind=""):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'


class Head(Element):
    tag_name = 'head'


class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "".join([self._open_tag(), self.contents[0]]))
        out_file.write(self._close_tag())
        out_file.write("\n")

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag_name = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, outfile, cur_ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        outfile.write(cur_ind + tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Hr(SelfClosingTag):
    tag_name = "hr"


class Br(SelfClosingTag):
    tag_name = "br"


class A(OneLineTag):
    tag_name = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul(Element):
    tag_name = 'ul'


class Li(Element):
    tag_name = 'li'


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        super().__init__(content)
        self.tag_name = 'h{}'.format(level)


class Meta(SelfClosingTag):
    tag_name = 'meta'
