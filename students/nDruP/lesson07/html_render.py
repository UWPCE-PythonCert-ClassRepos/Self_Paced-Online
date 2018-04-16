class Element:
    tag = "html"
    indent = 1

    def __init__(self, content=None, **kwargs):
        self.substance = () if content is None else (content,)
        self.attributes = kwargs

    def render(self, file_out, cur_ind=""):
        file_out.write(self.open_tag_str(cur_ind)+'\n')
        for x in self.substance:
            if issubclass(type(x), Element):
                x.indent = self.indent + 1
                x.render(file_out, cur_ind)
            elif x:
                file_out.write((cur_ind*(self.indent+1))+str(x)+'\n')
                
        file_out.write((self.indent*cur_ind)+"</"+self.tag+">\n")

    def append(self, text):
        mutable_content = list(self.substance)
        mutable_content.append(text)
        self.substance = tuple(mutable_content)

    def open_tag_str(self, cur_ind=""):
        token = (self.indent*cur_ind)+'<'+self.tag
        if self.attributes:
            for attr, value in self.attributes.items():
                token += ' '+attr+'="'+value+'"'
        token += ">"
        return token


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        file_out.write(self.open_tag_str(cur_ind) + ' ')
        for x in self.substance:
            file_out.write(str(x)+' ')
        file_out.write("</"+self.tag+">\n")


class SelfClosingTag(Element):
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def render(self, file_out, cur_ind=""):
        file_out.write(self.open_tag_str(cur_ind)+'\n')

    def open_tag_str(self, cur_ind=""):
        token = (self.indent*cur_ind)+'<'+self.tag
        if self.attributes:
            for attr, value in self.attributes.items():
                token += ' '+attr+'="'+value+'"'
        token += " \>"
        return token


class Html(Element):
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind*self.indent+"<!DOCTYPE html>\n")
        Element.render(self, file_out, cur_ind)
    pass


class Head(Element):
    tag = "head"
    pass


class Body(Element):
    tag = "body"
    pass


class H(OneLineTag):
    def __init__(self, size, content=None, **kwargs):
        self.tag = 'h'+str(size)
        OneLineTag.__init__(self, content, **kwargs)

    
class P(Element):
    tag = "p"
    pass


class Ul(Element):
    tag = "ul"
    pass


class Li(Element):
    tag = "li"
    pass


class Title(OneLineTag):
    tag = "title"
    pass


class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content):
        self.attributes = {"href":link}
        self.substance = () if content is None else (content,)        
    pass

class Hr(SelfClosingTag):
    tag = "hr"
    pass

class Br(SelfClosingTag):
    tag = "br"
    pass


class Meta(SelfClosingTag):
    tag = "meta"
    pass
