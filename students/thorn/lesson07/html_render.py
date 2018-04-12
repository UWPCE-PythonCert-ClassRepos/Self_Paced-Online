##!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    # Class attributes
    tag = ''  # tag name -> to be overridden
    indent = '  '  # indention level -> <html> is first so it starts at 4

    def __init__(self, content=None):
        ''' Init '''
        # Set content list if any exists
        if content:
            self.content = list(content)
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
        file_out.write(f"{cur_ind}<html>")
        for item in self.content:
            if hasattr(item, "render"):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(f"{cur_ind}{self.indent}{item}")
        file_out.write(f"{cur_ind}</html>")

