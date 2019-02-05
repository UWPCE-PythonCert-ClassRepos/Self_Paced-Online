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
        file_out.write(cur_ind+'<'+self.tag)
        if self.kwargs != {}:
            for style, name in self.kwargs.items():
                file_out.write(' '+style+'="'+name+'"')
        file_out.write('>\n')
        for text in self.content:
            if isinstance(text,str):
                file_out.write(cur_ind+self.indent+text+'\n')
            else:
                new_ind=cur_ind+'    '
                text.render(file_out,new_ind)
        file_out.write(cur_ind+'</'+self.tag+'>\n')

class Html(Element):
    tag='html'
    def render(self,file_out,cur_ind=''):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self,file_out,cur_ind='')

class Body(Element):
    tag='body'

class P(Element):
    tag='p'

class OneLineTag(Element):
    def render(self,file_out,cur_ind=''):
        file_out.write(cur_ind+'<'+self.tag)
        if self.kwargs != {}:
            for style, name in self.kwargs.items():
                file_out.write(' '+style+'="'+name+'"')
        file_out.write('>')
        for text in self.content:
            if isinstance(text,str):
                file_out.write(text)
            else:
                text.render(file_out)
        file_out.write('</'+self.tag+'>\n')

class Head(Element):
    tag='head'

class Title(OneLineTag):
    tag='title'

class SelfClosingTag(Element):
    def render(self,file_out,cur_ind=''):
        file_out.write(cur_ind+'<'+self.tag)
        if self.kwargs != {}:
            for style, name in self.kwargs.items():
                file_out.write(' '+style+'="'+name+'"')
        file_out.write(' />\n')

class Hr(SelfClosingTag):
    tag='hr'

class Br(SelfClosingTag):
    tag='br'

class A(OneLineTag):
    tag='a'
    def __init__(self, link, content):
        OneLineTag.__init__(self,content,href=link)

class Ul(Element):
    tag='ul'

class Li(Element):
    tag='li'

class H(OneLineTag):
    def __init__(self, size, content):
        OneLineTag.__init__(self,content)
        self.tag = 'h'+str(size)

class Meta(SelfClosingTag):
    tag='meta'
        
    