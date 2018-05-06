"""renders some simple HTML code"""

class Element():

    tag_name = "html"

    #content=None is supposed to be the 'initializer signature' ???

    def __init__(self, content: str=None):
        self.content = [content] if content else []

    def append(self, content):
        #append method that can add another string to the content
        self.content.append(content)

    def render(self, file_out, cur_ind=""):
        file_out.write(f"<{self.tag_name}>")
        for item in self.content:
            file_out.write(item + "\n")
        file_out.write(f"</{self.tag_name}>")


from io import StringIO
el = Element()
el.append("Some content.")
el.append("Some more content.")
el.render(file_out)
