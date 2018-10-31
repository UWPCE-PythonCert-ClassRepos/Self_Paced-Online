class Element:
    #attributes
    tag_name = ""
    one_indent = " "

    #init method
    def __init__(self, content=None):
        if content:
            self.content = [content]
        else:
            self.content = []