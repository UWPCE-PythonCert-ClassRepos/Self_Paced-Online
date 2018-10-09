class Element:
    tag = 'html'
    indent = "    "
    verbiage = []

    def __init__(self, verbiage=None):
        if verbiage is True:
            self.verbiage = [verbiage]
        else:
            self.verbiage = []
 
    def append(self, text):
        ''' Appends lines to the list of verbiage '''
        self.verbiage.append(text)
        

    def render(self, file_out, cur_ind = ""):
        ''' Writes verbiage and appropriate tags to the file '''
        file_out.write(f"{cur_ind}<{self.tag}>\n")

        for item in range(len(self.verbiage)):
            if isinstance(self.verbiage, Element):
                self.verbiage.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(f"{cur_ind}{self.indent}{self.verbiage[item]}\n")
        file_out.write(f"{cur_ind}</{self.tag}>\n")

class P(Element):
    ''' create the p tag '''
    tag = 'p'

class Html(Element):
    ''' html tag '''
    tag = 'html'

class Head(Element):
    ''' create the head tag '''
    tag = 'head'

class Body(Element):
    ''' create the body tag '''
    tag = 'body'