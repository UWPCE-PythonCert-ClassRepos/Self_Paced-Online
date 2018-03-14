
class Element:
    
    def __init__(self, content=None):
        self.content = content

    def append(self, more_content):
        if self.content is None:
            self.content = []
        self.content.append(more_content)

    def render(self, file_out, cur_ind = ""):

        """
            file_out could be any open, writable file-like object ( i.e. have a write() method ). 
            This is what you get from the open() function – but there are other kinds of file-like objects. 
            The html will be rendered to this file

            cur_ind is a string with the current level of indentation in it: the amount that the entire tag 
            should be indented for pretty printing
        """

        file_out.write('<html>\n')
        file_out.write(cur_ind.join(self.content) + '\n')
        file_out.write('</html>\n')

class Html(Element):
    
    def render(self, file_out, cur_ind = ""):
        file_out.write('<html>\n')
        file_out.write(cur_ind.join(self.content) + '\n')
        file_out.write('</html>\n')

class Body(Element):

    def render(self, file_out, cur_ind = ""):
        file_out.write('<body>\n')
        file_out.write(cur_ind.join(self.content) + '\n')
        file_out.write('</body>\n')

class P(Element):

    def render(self, file_out, cur_ind = ""):
        file_out.write('<p>\n')
        file_out.write(cur_ind.join(self.content) + '\n')
        file_out.write('</p>\n')
