class Element:
    tag = "html"
    indent = "   "

    def __init__(self, content=None, **kwargs):
        """
        initialize the Element instance
        
        :param content: optional input, string to create single line of content
        """
        self.content = []
        self.attrs = {}
        if content:
            self.content.append(content)
        if kwargs:
            self.attrs = kwargs

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
        file_out.write(cur_ind+"<"+self.tag)
        for attr, value in self.attrs.items():
            if attr == "clas":
                attr = "class"
            file_out.write(" "+attr+'="'+value+'"')
        file_out.write(">"+'\n')
        for item in self.content:
            if issubclass(type(item), Element):
                item.render(file_out, cur_ind+"   ")
            else:
                file_out.write(cur_ind+self.indent+item+'\n')
        file_out.write(cur_ind+"</"+self.tag+">"+'\n')


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def append(self, content):
        """
        append if content is currently blank, otherwise do nothing (do not update or add)
        
        :param content: 
        :return: 
        """
        if not self.content:
            self.content.append(content)

    def render(self, file_out, cur_ind=""):
        """
        render OneLineTag instance
        
        :param file_out: 
        :param cur_ind: 
        :return: 
        """
        content = "" if not self.content else self.content[0]
        file_out.write(cur_ind+"<"+self.tag+">"+content+"</"+self.tag+">"+'\n')


class Title(OneLineTag):
    tag = "title"
