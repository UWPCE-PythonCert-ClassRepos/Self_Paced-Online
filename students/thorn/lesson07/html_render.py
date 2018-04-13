##!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element:
    # Class attributes
    tag = ''  # tag name -> to be overridden
    indent = '    '  # indention level -> <html> is first so it starts at 4

    def __init__(self, content=None, **kwargs):
        ''' Init '''
        # Set content list if any exists
        if content:
            self.content = [content]
        else:
            self.content = []
        # Various attributes
        self.attributes = kwargs  # dict
        
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

        # Attribute kwargs dictionary rendering
        # format: <tag key="value">\n
        file_out.write(f"{cur_ind}<{self.tag}")

        for key, value in self.attributes.items():
            file_out.write(f' {key}="{value}"')
        file_out.write(">\n")  # Close tag and newline outside of loop

        for contents in self.content:
            # if hasattr(contents, 'render'):
            if isinstance(contents, Element):
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
        # Doctype
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, cur_ind='')


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


class SelfClosingTag(Element):
    ''' Renders self closing tags e.g. <hr /> <br />
    
    Overrides render to only render one tag and any attributes.
    Raises TypeError if content attempted.

    Refactor of render coming when the entire thing works.
    '''
    def render(self, file_out, cur_ind=''):
        file_out.write(f"{cur_ind}<{self.tag}")
        # Attributes
        for key, value in self.attributes.items():
            file_out.write(f' {key}="{value}"')
        # Close SINGLE LINE tag
        # format: /> + newline
        file_out.write(' />\n')
        if self.content:
            print("No content allowed")
            raise TypeError

class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Ul(Element):
    ''' unordered list '''
    tag = 'ul'


class Li(Element):
    ''' list element ''' 
    tag = 'li'


class H(OneLineTag):
    ''' Header element.  Overrides onelinetag by taking one int arg for the header
    level.
    '''
    def __init__(self, level, content, **kwargs):
        super().__init__(content, **kwargs)
        self.level = level
        self.tag = f'h{level}'


class Meta(SelfClosingTag):
    ''' Meta Tag - self closing '''
    tag = "meta"



''' Not working quite right. '''

class A(Element):
    ''' Link element.  Overrides Element __init__ call. '''
    tag = 'a'

    def __init__(self, link, content):
        # Call superclass init -> no self necessary
        super().__init__(content, href=link)

        
