class Element (object):
    tag_name = ""
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.attr_dict = kwargs
        self.attr_str = ""
        for k, v in self.attr_dict.items():
            self.attr_str = self.attr_str+("{}= '{}' ".format(k, v))
        if content is not None:
            self.content.append(content)

    def append(self, content):
        """add another string to the content"""
        self.content.append(content)

    def render(self, file_out, cur_ind=""):
        """renders tag and strings in the content"""
        if self.tag_name == "html":
            file_out.write("<!DOCTYPE html>\n")
        if self.attr_str == "":
            file_out.write("{}<{tag}>\n".format(cur_ind, tag=self.tag_name))
            prev_ind = cur_ind
            cur_ind += self.indent
        else:
            file_out.write("{}<{tag} {attr}>\n".format(cur_ind, tag=self.tag_name,
                                                       attr=self.attr_str))
            prev_ind = cur_ind
            cur_ind += self.indent
        for i in self.content:
            try:
                i.render(file_out, cur_ind)
            except AttributeError:
                file_out.write("{}{}\n".format(cur_ind, i))
        file_out.write("{}</{tag}>\n".format(prev_ind, tag=self.tag_name))


class Html (Element):
    tag_name = 'html'


class Body (Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'


class Head(Element):
    tag_name = 'head'


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        for i in self.content:
            file_out.write("{}<{tag}> {} </{tag}>\n".format(cur_ind, i,
                                                            tag=self.tag_name))


class Title(OneLineTag):
    tag_name = 'title'


class SelfClosingTag(Element):

    def render(self, file_out, cur_ind=""):
        """renders tag and strings in the content"""
        if self.attr_dict == {}:
            file_out.write("{}<{tag} />\n".format(cur_ind, tag=self.tag_name))
        else:
            file_out.write("{}<{tag} {attr}/>\n".format(cur_ind, tag=self.tag_name,
                                                        attr=self.attr_str))
        if self.content != []:
            raise TypeError('unexpected content with SelfClosingTag')


class Hr(SelfClosingTag):
    tag_name = "hr"


class Br(SelfClosingTag):
    tag_name = "br"


class Meta(SelfClosingTag):
    tag_name = "meta"


class A(Element):
    """subclass for anchor (link) element"""
    tag_name = 'a'

    def __init__(self, link, content):
        Element.__init__(self, content=None)
        self.attr_str = "href={}".format(link)
        self.content = []
        for k, v in self.attr_dict.items():
            self.attr_str = self.attr_str+("{}= '{}' ".format(k, v))
        if content is not None:
            self.content.append(content)


class Ul(Element):
    tag_name = "ul"


class Li(Element):
    tag_name = "li"


class H(OneLineTag):
        def __init__(self, level, content, **kwargs):
            super().__init__()
            self.tag_name = 'h{}'.format(level)
            self.content = []
            self.attr_dict = kwargs
            self.attr_str = ""
            for k, v in self.attr_dict.items():
                self.attr_str = self.attr_str+("{}= '{}' ".format(k, v))
            if content is not None:
                self.content.append(content)
