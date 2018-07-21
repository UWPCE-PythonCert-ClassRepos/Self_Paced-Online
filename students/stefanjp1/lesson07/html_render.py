
class Element():
    tag_name = 'html'
    indent = 0
    
    def __init__(self, content=None, **kwargs):
        self.content = []
        if content != None:
            self.content.append(TextWrapper(content))
        self.kwargs = kwargs    
        
    
    def render(self, file_out, cur_ind = ""):
        sub_ind = cur_ind + (" " * self.indent)
        tags = add_tags(self.kwargs)
        
        file_out.write("{}<{}{}>\n".format(cur_ind, self.tag_name, tags))
        for block in self.content:
            block.render(file_out, sub_ind)
        file_out.write("{}</{}>\n".format(cur_ind, self.tag_name))
        

    def append(self, content):
        if isinstance(content, str):
            self.content.append(TextWrapper(content))
        else:
            self.content.append(content)

def add_tags(tags):
    tag_list = []
    
    for k, v in tags.items():
        tag_list.append(" {}=\"{}\"".format(k, v))
        
    return ", ".join(tag_list)
        
    
class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind)
        file_out.write(self.text)


class Html(Element):
    tag_name = 'html'
    
    def render(self, file_out, cur_ind = ""):
        file_out.write("<!DOCTYPE html>\n")
        
        super().render(file_out, cur_ind)
    

class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'
    

class Head(Element):
    tag_name = 'head'
    
    def __init__(self, content=None, **kwargs):
        self.content = []
        if content != None:
            self.content.append(TextWrapper(content))
        self.kwargs = kwargs 


class OneLineTag(Element):
    def render(self, file_out, cur_ind = ""):
        tags = add_tags(self.kwargs)
        
        file_out.write("<{}{}>".format(self.tag_name, tags))
        for block in self.content:
            block.render(file_out)
        file_out.write("</{}>\n".format(self.tag_name))


class Title(OneLineTag):
    tag_name = 'title'

        
class SelfClosingTag(Element):
    tag_name = ''
    
    def __init__(self, content=None, **kwargs):
        if content != None:
            raise TypeError('SelfClosingTag cannot have any content')
        self.kwargs = kwargs

    def render(self, file_out, cur_ind = ""):
        tags = add_tags(self.kwargs)
        
        file_out.write("<{}{} />\n".format(self.tag_name, tags))

class Hr(SelfClosingTag):
    tag_name = 'hr'
    
class Br(SelfClosingTag):
    tag_name = 'br'
    
class A(OneLineTag):
    tag_name = 'a'
    
    def __init__(self, link, content=None, **kwargs):
        self.content = []
        if content != None:
            self.content.append(TextWrapper(content))
        self.kwargs = kwargs  
        self.kwargs['href'] = link
    
        
class Ul(Element):
    tag_name = 'ul'
    

class Li(Element):
    tag_name = 'li'
    
        
class H(OneLineTag):
    tag_name = 'h'
    
    def __init__(self, level, content=None, **kwargs):
        self.level = str(level)
        self.content = []
        if content != None:
            self.content.append(TextWrapper(content))
        self.kwargs = kwargs 
        self.tag_name = self.tag_name + self.level
        
class Meta(SelfClosingTag):
    tag_name = 'meta'
    
    def __init__(self, **kwargs):
        self.kwargs = kwargs