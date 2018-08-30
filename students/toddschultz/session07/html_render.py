class Element:
    tag = "html"
    indent = "    "
    verbiage = []

    def __init__(self, verbiage=None):
        if verbiage is True:
            self.verbiage = [verbiage]
        else:
            self.verbiage = []
 
    def append(self, text):
        ''' Appends lines to the list of verbiage '''
        self.verbiage.append(text)
        

    def render(self, file_out, cur_ind = ""):
        ''' Writes verbiage and appropriate tags to the file '''
        file_out.write(f"{cur_ind}<{self.tag}>")
        for item in self.verbiage:
            file_out.write("\n")
            file_out.write(self.indent)
            file_out.write(item)
        file_out.write(f"\n{cur_ind}</{self.tag}>\n")