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
        
        #print(type(self))
        if len(self.tag) > 0:
            attr_str = ''
            for k,v in self.attrs.items():
                attr_str += f"{k}=\"{v}\""
            attr_str = ' ' + attr_str if len(attr_str) > 0 else attr_str
            file_out.write(f"{self.cur_ind}<{self.tag}{attr_str}>\n")
        for element in self.content_list:
            if isinstance(element,str):
                file_out.write(self.cur_ind + element + '\n')
            else:
                element.render(file_out,element.cur_ind)
        if len(self.tag) > 0:
            file_out.write(f"{self.cur_ind}</{self.tag}>\n")

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
    _cur_ind = ''*4

class OneLineTag(Element):

    _tag = 'head'
    _cur_ind = ''*4

    def render(self, file_out, cur_ind = ""):
        file_out.write(f"{self.cur_ind}<{self.tag}>" + '\n'.join(self.content_list) + f"{self.cur_ind}</{self.tag}>\n")

class Title(OneLineTag):

    _tag = 'title'
    _cur_ind = ''*4
