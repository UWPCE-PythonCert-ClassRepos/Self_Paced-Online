"""renders some simple HTML code"""

class Element():

    tag_name = "html"

    #inster '**kwargs" as optional argument

    def __init__(self, content: str=None):
        self.content = [content] if content else []
        #self.kwargs = kwargs

    def append(self, content):
        #append method that can add another string to the content
        self.content.append(content)

    def render(self, file_out, cur_ind=""):
        
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, "    ")
            else:
                file_out.write(f"<{self.tag_name}>")
                file_out.write(item + "\n")
                file_out.write(f"</{self.tag_name}>")

                
class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, "    ")
            else:
                file_out.write(f"<{self.tag_name}>")
                file_out.write(item + "\n")
                file_out.write(f"</{self.tag_name}>")
            
        
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

    
# from io import StringIO
# el = Element()
# el.append("Some content.")
# el.append("Some more content.")
# el.render(file_out)
