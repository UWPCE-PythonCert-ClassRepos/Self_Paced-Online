class Element:
    
    #Top level tag name is html. Derived elements should have a class variable
    #that overrides this top level name
    tag = "html"
    #Indent is the number of spaces to indent different elements
    indent = 4
    
    def __init__(self, content=None):
        #The instance variable contents is a list of strings or other
        #html elements
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
            
    def append(self,content):
        self.contents.append(content)

    def render(self, outfile, cur_ind=0):
        
        indent_str = cur_ind * self.indent * ' '
        outfile.write("{}<{}>\n".format(indent_str, self.tag))
        for content in self.contents:
            outfile.write("{}{}{}\n".format(
                        indent_str, self.indent * ' ',content))
        outfile.write("{}</{}>".format(indent_str, self.tag))


class HTML(Element):
     tag = "html"
   
    
class Body(Element):
    tag = "body"
    
    
class P(Element):
    tag = "p"