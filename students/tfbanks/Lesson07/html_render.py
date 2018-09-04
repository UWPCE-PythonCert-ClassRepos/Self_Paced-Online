# html_render.py by Tfbanks
#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


class Element(object):
    tag = 'html' 
    indent = '  '
    
    def __init__(self, content=None, **kwargs): 
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.kwargs = kwargs
        
    def append(self, new_content):
        self.contents.append(new_content)
    
    def render(self, out_file, cur_ind='', **kwargs):
        out_file.write(cur_ind + f'<{self.tag}')
        for k, v in self.kwargs.items():
             out_file.write(' {}="{}"'.format(k, v))
        out_file.write('>\n')

        for content in self.contents:
            if hasattr(content, 'render'):
                content.render(out_file, cur_ind + self.indent)
            else:
                out_file.write(cur_ind + self.indent + str(content) + '\n')

        out_file.write(cur_ind + f'</{self.tag}>\n')

 
class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=''):
        out_file.write ('<!DOCTYPE html>\n')
        super().render(out_file, cur_ind)


class Body(Element):
    tag = 'body'
    
    
class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file, cur_ind = '', **kwargs):
        out_file.write('{}<{}'.format(cur_ind, self.tag))

        for k, v in self.kwargs.items():
            out_file.write(' {}="{}"'.format(k, v))
        out_file.write('>')       
        
        for content in self.contents:
            if hasattr(content, 'render'):
                content.render(out_file, cur_ind + self.indent)
            else:
                out_file.write(content)

        out_file.write('</{}>\n'.format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")
 
    def render(self, out_file, cur_ind='', **kwargs):
        out_file.write(cur_ind + f'<{self.tag}')
        for k, v in self.kwargs.items():
            out_file.write(' {}="{}"'.format(k, v))
        out_file.write(' />\n')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, level, content=None):
        super().__init__(content)
        self.tag = f'h{level}'


class Meta(SelfClosingTag):
    tag = 'meta'
