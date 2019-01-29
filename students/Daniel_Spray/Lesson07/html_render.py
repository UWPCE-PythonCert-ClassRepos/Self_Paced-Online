class Element:
    tag='html'
    def __init__(self,content=None):
        self.indent='    '
        list(content)

    def append(self,new_content):
        self.content.append(new_content)

    def render(self,file_out,cur_ind=''):
        with open(file_out,'w') as f:
            f.write(cur_ind+"<"+tag+">/n"+cur_ind+self.content+"/n"+cur_ind+"<"+tag+">")