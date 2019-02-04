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
        str_only=[]
        for text in self.content:
            if isinstance(text,str):
                str_only.append(str(text))
            else:
                text.render(file_out)
        content_string = ('.\n'+cur_ind+self.indent).join(str_only)
        file_out.write(cur_ind+self.indent+content_string+'\n'+cur_ind+'</'+self.tag+'>\n')

class Html(Element):
    tag='html'
    def render(self,file_out,cur_ind=''):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self,file_out,cur_ind='')

class Body(Element):
    tag='body'

class P(Element):
    tag='p'
