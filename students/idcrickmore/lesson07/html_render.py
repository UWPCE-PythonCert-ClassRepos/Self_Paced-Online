"""renders some simple HTML code"""

class Element():

    tag_name = ""
    indent = "    "
    
    #content=None is supposed to be the 'initializer signature' ???
    
    def __init__(self):
        self.content = list()

    def append(self, some_string):
        self.content.append(some_string)
		
    def render():
        pass
