from io import StringIO

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
        self.cur_ind = cur_ind
        output = (self.cur_ind * " ") + "<" + self.tagname + ">\n"
        if len(self.content) > 0:
            for element in self.content:
                if isinstance(element, str):
                    output = output + (2 * self.cur_ind * " ") + element + "\n"
                if isinstance(element, Body):
                    f_body = StringIO()
                    element.cur_ind = self.cur_ind + element.indentation
                    element.render(f_body, element.cur_ind)
                    output = output + f_body.getvalue()
                    #output = output.strip()
                if isinstance(element, P):
                    f_p = StringIO()
                    element.cur_ind = self.cur_ind + element.indentation
                    element.render(f_p, element.cur_ind)
                    output = output + f_p.getvalue()
                    #output = output.strip()
            #output = output + "\n"
        output = output + (self.cur_ind * " ") + "</" + self.tagname + ">\n"
        file_out.write(output)

class Html(Element):
    tagname = 'html'

class Body(Element):
    tagname = 'body'

class P(Element):
    tagname = 'p'
