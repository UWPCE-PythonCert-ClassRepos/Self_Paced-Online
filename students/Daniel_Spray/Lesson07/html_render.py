class Element:
    tag='html'
    indent='    '
	
    def __init__(self, content=None, **kwargs):
        self.content = [content] if content else []
        self.kwargs = kwargs
		
    def append(self,new_content):
        '''Add content to list'''
        self.content.append(new_content)

    def render(self,file_out,cur_ind=''):
        file_out.write(cur_ind+'<'+self.tag+'>\n')
        for text in self.content:
            if isinstance(text,str):
                file_out.write(text+'.\n')
            else:
                text.render(file_out)
        file_out.write(cur_ind+'</'+self.tag+'>\n')

class Html(Element):
    tag='html'

class Body(Element):
    tag='body'

class P(Element):
    tag='p'


