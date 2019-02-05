class Element:
    '''Create a baseline class for creating HTML documents'''
    tag='html'
    indent='    '
	
    def __init__(self, content=None, **kwargs):
        '''Initialize objects'''
        self.content = [content] if content else []
        self.kwargs = kwargs
		
    def append(self,new_content):
        '''Add content to list'''
        self.content.append(new_content)

    def render(self,file_out,cur_ind=''):
        '''Create a method for rendering the content to an html file'''
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
    '''Create a class for making an html tag'''
    tag='html'
    def render(self,file_out,cur_ind=''):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self,file_out,cur_ind='')

class Body(Element):
    '''Create a class for making a body tag'''
    tag='body'

class P(Element):
    '''Create a class for making a paragraph tag'''
    tag='p'

class OneLineTag(Element):
    '''Create a class for making a single line tag'''
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
    '''Create a class for making a head tag'''
    tag='head'

class Title(OneLineTag):
    '''Create a class for making a title tag'''
    tag='title'

class SelfClosingTag(Element):
    '''Create a class for making a self-closing tag'''
    def render(self,file_out,cur_ind=''):
        file_out.write(cur_ind+'<'+self.tag)
        if self.kwargs != {}:
            for style, name in self.kwargs.items():
                file_out.write(' '+style+'="'+name+'"')
        file_out.write(' />\n')

class Hr(SelfClosingTag):
    '''Create a class for making a hr tag'''
    tag='hr'

class Br(SelfClosingTag):
    '''Create a class for making a br tag'''
    tag='br'

class A(OneLineTag):
    '''Create a class for making an 'a' tag'''
    tag='a'
    def __init__(self, link, content):
        OneLineTag.__init__(self,content,href=link)

class Ul(Element):
    '''Create a class for making an unordered list tag'''
    tag='ul'

class Li(Element):
    '''Create a class for making an ordered list tag'''
    tag='li'

class H(OneLineTag):
    '''Create a class for making an h tag'''
    def __init__(self, size, content):
        OneLineTag.__init__(self,content)
        self.tag = 'h'+str(size)

class Meta(SelfClosingTag):
    '''Create a class for making a meta tag'''
    tag='meta'
        
    