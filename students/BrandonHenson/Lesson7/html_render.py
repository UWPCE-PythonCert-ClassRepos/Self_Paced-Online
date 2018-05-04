from io import StringIO
class Element:
    tag = " "
    indentation = 0

    def __init__(self, content=None, **attr):
        if content:
            self.content = [content]
            self.data = attr
        else:
            self.content = []


    def append(self,newstring = None):
        self.content.append(newstring)

    def render(self, file_out, cur_ind=''):
        self.add_attrs(file_out, cur_ind)
        file_out.write('>\n')
        #= open('C:\\Users\\Brandon\\Desktop\\Test.txt', 'a')
