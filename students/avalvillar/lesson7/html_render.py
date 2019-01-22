"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    January 16th 2019
"""

'''
This is the Element class that is subclassed from 'object' and will have many
subclasses from itselt. The overall goal is to be able to render HTML
documentation as functions are called for particular tags, attributes, and
indentations/levels.
'''

#Top level class of project.
class Element(object):

    #Class level attributes for an empty tag, default indentations
    tag = ''
    indentation = 4
    attrs = {'':''}

    #If attributes are given - put them in self.attrs and if contens is None
    #create an empty content list to append to later.
    def __init__(self, content=None, **kwargs):
        self.attrs = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    #Append function to add contents as needed to a list for later use.
    def append(self, content):
        self.contents.append(content)

    #Render method that will write to the file object passed in.
    def render(self, file_out, cur_ind=''):
        '''if cur_ind != '':
            file_out.write(' ' * cur_ind)'''
        if self.attrs.keys():
            file_out.write('<' + self.tag)
            for k, v in self.attrs.items():
                file_out.write(' {}=\"{}\"'.format(k,v))
            file_out.write('>')
        else:
            file_out.write('<' + self.tag + '>\n')
        for item in self.contents:
            try:
                item.render(file_out, self.indentation * 2)
            except AttributeError:
                file_out.write(item)
        '''if cur_ind != '':
            file_out.write(' ' * cur_ind)'''
        file_out.write('\n</' + self.tag + '>')

#Subclass of Element - will add "Doctype" to all new HTML files.
class Html(Element):
    tag = 'html'
    def render(self, file_out, cur_ind=""):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out)

#Subclass of Element
class Body(Element):
    tag = 'body'
    def render(self, file_out, cur_ind=""):
        Element.render(self, file_out)

#Subclass of Element
class P(Element):
    tag = 'p'
    def render(self, file_out, cur_ind=""):
        Element.render(self, file_out)

#Subclass of Element
class Head(Element):
    tag = 'head'
    def render(self, file_out, cur_ind=""):
        Element.render(self, file_out, self.indentation)

#Overwrites the Element render function to create a single line tag.
class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        '''if cur_ind != '':
            file_out.write(' ' * cur_ind)'''
        file_out.write('<' + self.tag + '>')
        [file_out.write(item) for item in self.contents]
        file_out.write('</' + self.tag + '>')

#Subclass of OneLineTag to a the tag on a single line
class Title(OneLineTag):
    tag = 'title'
    def render(self, file_out, cur_ind=""):
        OneLineTag.render(self, file_out, self.indentation * 2)

#Overwrites Element render function to create a self closing tag
class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=''):
        '''if cur_ind != '':
            file_out.write(' ' * cur_ind)'''
        file_out.write('<' + self.tag)
        if self.attrs.keys():
            for k, v in self.attrs.items():
                file_out.write(' {}=\"{}\"'.format(k,v))
        try:
            self.contents is None
        except:
            print('Contents not empty')
        file_out.write(' />\n')

#Subclass of SelfClosingTag
class Hr(SelfClosingTag):
    tag = 'hr'

#Subclass of SelfClosingTag
class Br(SelfClosingTag):
    tag = 'br'

#Subclass of SelfClosingTag
class Meta(SelfClosingTag):
    tag = 'meta'
    def render(self, file_out, cur_ind=""):
        SelfClosingTag.render(self, file_out, self.indentation * 2)

#Subclass of Element
class Ul(Element):
    tag = 'ul'
#Subclass Element
class Li(Element):
    tag = 'li'

#Subclass of OneLineTag - Extends the Element initializer.
class H(OneLineTag):
    tag = 'h'
    def __init__(self, level, content):
        self.tag = (self.tag + str(level))
        Element.__init__(self, content)

#Subclass of Element - Extends the Element initializer.
class A(Element):
    tag = 'a'
    def __init__(self, link, content):
        Element.__init__(self, content, href=link)

