class Element:
    tag = 'html'
    indent = '    '

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, added_content):
        self.content.append(added_content)

    def render(self, file_out, cur_ind=''):
        file_out.write(cur_ind + '<{}>\n'.format(self.tag))
        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(str(item)+'\n')
        file_out.write('</{}>\n'.format(self.tag))

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    def render(self, file_out, cur_ind=''):
        file_out.write(cur_ind + '<{}>'.format(self.tag))
        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(str(item))
        file_out.write('</{}>\n'.format(self.tag))

class Title(OneLineTag):
    tag = 'title'