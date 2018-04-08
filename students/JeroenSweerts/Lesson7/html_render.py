class Element():
    tagname = 'tag'
    indentation = 4
    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, string=None):
        '''Method that can add another string to the content.'''
        self.content.append(string)

    def render(self, file_out, cur_ind=0):
        '''Method that renders the tag and the strings in the content.'''
        output = "<" + self.tagname + ">\n"
        if len(self.content) > 0:
            output = output + ((cur_ind + self.indentation) * " ")
            for string in self.content:
                output = output + string
            output = output + "\n"
        output = output +  "<\\" + self.tagname + ">\n"
        file_out.write(output)

class Html(Element):
    tagname = 'html'

class Body(Element):
    tagname = 'body'

class P(Element):
    tagname = 'p'
