class Element:
    tag = "html"
    indent = "   "

    def __init__(self, content=None, **kwargs):
        """
        initialize the Element instance
        
        :param content: optional input, string to create single line of content
        """
        self.content = []
        self.attributes = {}
        if content:
            self.content.append(content)
        if kwargs:
            self.attributes = kwargs

    def append(self, content):
        """
        append another line to content
        
        :param content: string to append
        :return: none
        """
        if content:
            self.content.append(content)

    def render(self, file_out, cur_ind=""):
        """
        render Element instance
        
        :param file_out: object to write rendering to
        :param cur_ind: indentation level to apply to each line
        :return: none
        """
        file_out.write(f"{cur_ind}<{self.tag}{self.render_attributes()}>\n")
        for item in self.content:
            if issubclass(type(item), Element):
                item.render(file_out, cur_ind+"   ")
            else:
                file_out.write(f"{cur_ind}{self.indent}{item}\n")
        file_out.write(cur_ind+"</"+self.tag+">\n")

    def render_attributes(self):
        res_string = ""
        for attr, value in self.attributes.items():
            if attr == "clas":
                attr = "class"
            res_string+=(f' {attr}="{value}"')
        return res_string


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        """
        render OneLineTag instance
        
        :param file_out: 
        :param cur_ind: 
        :return: 
        """
        content = " ".join(self.content)
        file_out.write(f"{cur_ind}<{self.tag}{self.render_attributes()}>{content}</{self.tag}>\n")


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        """
        initialize the SelfCLosingTag element
        
        :param content: 
        :param kwargs: 
        """
        if content or kwargs:
            raise TypeError("'SelfClosingTag' object cannot have any content")
        super().__init__()

    def append(self, content):
        """
        raise error if user tries to add content to a SelfClosingTag
        
        :param content: 
        :return: 
        """
        raise TypeError("'SelfClosingTag' object cannot have any content")

    def render(self, file_out, cur_ind=""):
        """
        render SelfClosingTag instance
        
        :param file_out: 
        :param cur_ind: 
        :return: 
        """
        file_out.write(f"{cur_ind}<{self.tag}{self.render_attributes()} />\n")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content):
        """
        initialize the anchor element
        
        :param link: 
        :param content: 
        """
        self.content = [content]
        self.attributes = {"href": link}
