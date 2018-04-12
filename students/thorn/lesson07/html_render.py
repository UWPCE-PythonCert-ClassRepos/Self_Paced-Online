##!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    # Class attributes
    tag = ''  # tag name -> to be overridden
    indent = '    '  # indention level -> <html> is first so it starts at 4

    def __init__(self, content=None):
        ''' Init '''
        # Set content list if any exists
        if content:
            self.content = [content]
        else:
            self.content = []

    def append(self, new_content):
        ''' 
        Appends a string to content.
        '''
        self.content.append(new_content)

    def render(self, file_out, cur_ind=""):
        ''' 
        Renders the tag and the strings in the content.  
        Starts <html> ends </html>

        file_out: any open writeable file-like object

        cur_ind: string with the current level of indentation -> the amount the 
                 entire tag should be indented for printing
        '''
        # Start with html at our current ident --> add content 1 tab extra in
        file_out.write(f"{cur_ind}<{self.tag}>\n")
        
        for contents in self.content:
            if hasattr(contents, 'render'):
                contents.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(f"{cur_ind}{self.indent}{contents}\n")
        file_out.write(f"{cur_ind}</{self.tag}>\n")
            

class Html(Element):
    ''' <html> tag '''
    # HTML class attributes
    tag = 'html'

    # Pass render with indent.
    def render(self, file_out, cur_ind=""):
        Element.render(self, file_out, cur_ind="")


class Body(Element):
    ''' <body> tag '''
    tag = 'body'


class P(Element):
    ''' <p> tag '''
    tag = 'p'


class Head(Element):
    ''' <head> tag '''
    tag = 'head'


class OneLineTag(Element):
    ''' Overrides the render method to put everything on one line for certain tags. 
    
    Should be similar to how element acts but without new lines.
    '''
    def render(self, fileout, cur_ind=''):
        fileout.write(f"{cur_ind}<{self.tag}>")
        for contents in self.content:
            if hasattr(contents, 'render'):
                contents.render(fileout, cur_ind + self.indent)
            else:
                fileout.write(contents)
        fileout.write(f"</{self.tag}>\n")


class Title(OneLineTag):
    ''' <title> tag subclass of OneLineTag (puts it all on one line). '''
    tag = 'title'