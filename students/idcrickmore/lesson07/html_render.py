"""renders some simple HTML code"""

class Element():

    tag_name = "html"

    def __init__(self, content: str=None, **kwargs):
        self.content = [content] if content else []
        self.attributes = kwargs

    def append(self, content):
        #append method that can add another string to the content
        self.content.append(content)

    def render(self, file_out, cur_ind=""):
        if self.attributes != {}:
            attributes = " ".join([' %s="%s"' % (k, v) for k, v in self.attributes.items()])
            open_tag = f"<{self.tag_name}{attributes}>"
            close_tag = f"</{self.tag_name}>"
            print(open_tag)
            print(close_tag)

        else:
            open_tag = f"<{self.tag_name}>"
            close_tag = f"</{self.tag_name}>"
        # print(open_tag)
        # print(close_tag)
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, "    ")
            else:
                file_out.write(open_tag)
                file_out.write(item + "\n")
                file_out.write(close_tag)


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, "    ")
            else:
                file_out.write(f"<{self.tag_name}>")
                file_out.write(item + "\n")
                file_out.write(f"</{self.tag_name}>")
            
        
class SelfClosingTag(Element):
    #To Do: raise some kind of exception for content
    
    def render(self, file_out, cur_ind=""):
        tag_close = "/"
        print(f"<{self.tag_name}{tag_close}>")
        file_out.write(f"<{self.tag_name}{tag_close}>")
        
        
class Html(Element):
    pass
    
    
class Body(Element):
    tag_name = "body"
    

class P(Element):
    tag_name = "p"

    
class Head(Element):
    tag_name = "head"

    
class Title(OneLineTag):
    tag_name = "title"

    
class Hr(SelfClosingTag):
    tag_name = 'hr'
   
   
class Br(SelfClosingTag):
    tag_name = 'br'
    
 
class A(Element):
    tag_name = 'a'
    
    def __init__(self, link, content):
        Element.__init__(self, content, href=link)
        
        