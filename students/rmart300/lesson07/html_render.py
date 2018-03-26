class Element:
   
    _tag = ''
    _cur_ind = ''    

    def __init__(self, content=None, **attrs):
        self.content_list = []
        if content is not None:
            self.append(content)
        #self.tag = Element.tag
        self.attrs = attrs

    @property
    def tag(self):
        return self._tag
    @property
    def cur_ind(self):
        return self._cur_ind

    @property
    def attr_str(self):
        attr_str = ''
        if hasattr(self, 'attrs'):
            for k,v in self.attrs.items():
                attr_str += f" {k}=\"{v}\"" if len(attr_str) > 0 else f"{k}=\"{v}\"" 
        return attr_str

    @property
    def opening_tag(self):
        opening_tag = ''
        if len(self.tag) > 0:
            if self.tag == 'html': opening_tag = '<!DOCTYPE html>\n'

            if len(self.attr_str) > 0: 
                opening_tag += f"{self.cur_ind}<{self.tag} {self.attr_str}>\n"
            else:
                opening_tag += f"{self.cur_ind}<{self.tag}>\n"
        return opening_tag

    @property
    def closing_tag(self):
        closing_tag = ''
        if len(self.tag) > 0:
            closing_tag = f"{self.cur_ind}</{self.tag}>\n"
        return closing_tag

    def append(self, more_content):
        self.content_list.append(more_content)

    def render(self, file_out, cur_ind = ""):

        """
            file_out could be any open, writable file-like object ( i.e. have a write() method ). 
            This is what you get from the open() function – but there are other kinds of file-like objects. 
            The html will be rendered to this file

            cur_ind is a string with the current level of indentation in it: the amount that the entire tag 
            should be indented for pretty printing
        """
        
        file_out.write(self.opening_tag)

        for element in self.content_list:
            if isinstance(element,str):
                file_out.write(self.cur_ind + ' '*4 + element + '\n')
            else:
                element.render(file_out,self.cur_ind)

        file_out.write(self.closing_tag)

class Html(Element):
    
    _tag = 'html'
    _cur_ind = ''

class Body(Element):

    _tag = 'body'
    _cur_ind = ' '*4

class P(Element):

    _tag = 'p'
    _cur_ind = ' '*8

class Head(Element):

    _tag = 'head'
    _cur_ind = ' '*4

class OneLineTag(Element):

    _tag = ''
    _cur_ind = ''

    @property
    def one_line_tag(self):
        return f"{self.cur_ind}<{self.tag}>" + ' '.join(self.content_list) + f"</{self.tag}>\n"

    def render(self, file_out, cur_ind = ""):
        file_out.write(one_line_tag)

class Title(OneLineTag):

    _tag = 'title'
    _cur_ind = ' '*8

class SelfClosingTag(Element):

    _tag=''
    _cur_ind=''
    
    @property
    def closed_tag(self):
        return f"{self.cur_ind}<{self.tag} {self.attr_str} />\n"


    def render(self, file_out, cur_ind = ""):

        if len(self.content_list) > 0:
            raise TypeError
        file_out.write(closed_tag)
        

class Hr(SelfClosingTag):

    _tag = 'hr'
    _cur_ind = ' '*8

class Br(SelfClosingTag):
    _tag = 'br'
    _cur_ind = ' '*8

class A(Element):

    _tag = 'a'
    _cur_ind = ' '*16

    def __init__(self, link, content):
        self.content_list = []
        if content is not None:
            self.append(content)
        self.attrs = { 'href':link } 

class Ul(Element):

    _tag = 'ul'
    _cur_ind = ' '*8

class Li(Element):

    _tag = 'li'
    _cur_ind = ' '*12

class H(OneLineTag):

    _tag = 'h'
    _cur_ind = ' '*8

    def __init__(self,number,content):

        self._tag = f"h{number}"
       
        self.content_list = []
        if content is not None:
            self.append(content)
        super()

class Meta(SelfClosingTag):

    _tag = 'meta'
    _cur_ind = ' '*8

    def __init__(self, charset='UTF-8'):
        self.content_list = []
        self.attrs =  { 'charset': charset } 
