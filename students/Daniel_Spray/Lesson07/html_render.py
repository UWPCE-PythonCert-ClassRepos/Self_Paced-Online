class Element:
    tag='html'
    indent='    '
	
    def __init__(self, content=None, **kwargs):
        self.content = [].append(content) if content else []
        self.kwargs = kwargs
		
    def append(self,new_content):
        '''Add content to list'''
        self.content.append(new_content)

    def render(self,file_out,cur_ind=''):
        with open('html_render.html','w') as f:
            f.write(cur_ind+"<"+self.tag+">\n"+cur_ind+'.\n'.join(self.content)+"\n"+cur_ind+"<"+self.tag+">")