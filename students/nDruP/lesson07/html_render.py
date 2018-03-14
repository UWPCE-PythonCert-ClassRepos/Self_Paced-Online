class Element:
    tag = "Element"

    
    def __init__(self):
        self.content = ()


    def render(self, memory, offset):
        for x in self.content:
            memory.write(offset+x+'\n')
        

    def append(self, text):
        mutable_content = list(self.content)
        mutable_content.append(text)
        self.content = tuple(mutable_content)
