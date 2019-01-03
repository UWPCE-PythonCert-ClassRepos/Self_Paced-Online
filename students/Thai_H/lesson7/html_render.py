
# Step 1
#########
#---------------------------------------------------------------------
class Element:
    tag = ''
    indent = '    '  # 4 spaces


    #-----------------------------------------------------------------
    def __init__(self, content = None, **attributes):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = attributes


    #-----------------------------------------------------------------
    def append(self, content):
        self.content.append(content)


    #-----------------------------------------------------------------
    def format_attributes(self):
        if self.attributes:
            attributes = ' ' + ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())
        else:
            attributes = ''

        return attributes


    #-----------------------------------------------------------------
    def render(self, file_out, cur_ind = ''):
        file_out.write(f'{cur_ind}<{self.tag}{self.format_attributes()}>\n')

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(cur_ind + self.indent + str(item) + '\n')

        file_out.write(cur_ind + f'</{self.tag}>\n')

#------------------------------------------------------------------------------



# ## Step 2
# ##########
#------------------------------------------------------------------------------
class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind = ''):

        file_out.write(f'{cur_ind}<!DOCTYPE html>\n')
        super().render(file_out, cur_ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'
#------------------------------------------------------------------------------


# ## Step 3
# ##########
#------------------------------------------------------------------------------
class Head(Element):
    tag = 'head'

class OneLineClass(Element):
    def render(self, file_out, cur_ind=''):
        file_out.write(f'{cur_ind}<{self.tag}{self.format_attributes()}>')

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(str(item) + ' ')

            file_out.write(f'</{self.tag}>\n')


class Title(Element):
    tag = 'title'
#-------------------------------------------------------------------------


# # Step 4
# ##########

class SelfClosingTag(Element):

    def render(self, file_out, cur_ind=''):
        file_out.write(f'{cur_ind}</{self.tag}{self.format_attributes()}>\n')


class Hr(Element):
    tag = 'hr'
#----------------------------------------------------------------------------



# # Step 5
# #########

class Br(Element):
    tag = 'br'
#----------------------------------------------------------------------


# # Step 6
# #########
class A(Element):
    tag = 'a'

    def __init__(self, link, content):
        super().__init__(content, href = link)

#------------------------------------------------------------------------



# # Step 7
# #########
class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineClass):

    def __init__(self, level, content):
        super().__init__(content)
        self.tag = f'h{level}'

#------------------------------------------------------------------------


# # Step 8 and 9
# ##############
class Meta(SelfClosingTag):
    tag = 'meta'

#-------------------------------------------------------------------------