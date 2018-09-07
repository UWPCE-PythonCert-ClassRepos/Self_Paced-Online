class Element():
    """Creates html code for given inputs"""


    def __init__(self, content = ''):
        self.content = content

    def append(self, some_string):
        self.content = self.content + some_string


#page = Element()
#page.append("some test text ")
#page.append("add some more")
#print(page.content)
