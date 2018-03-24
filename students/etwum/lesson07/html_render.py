
class Element:

    tag_name = ""

    indentation = " "

    def __int__(self, content = None):
        self.content = content
        pass

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, cur_ind=""):

