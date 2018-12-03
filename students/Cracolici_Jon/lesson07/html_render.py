#
#!/usr/bin/env python3
#
#Jon Cracolici
#UW-Python Cert
#Lesson 07
#HTML Render Problem
"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    """Element class containing:
    Attributes:
        Content - A list of strings passed to Element
        Tag - tag for type of content
        Indent - indent spec'd for pretty printing
        Other attributes may be passed for use in SubClasses
    Methods:
        Append - appends Content
        Render - Renders Contents for file output"""

    tag = ''
    indent = '    ' #4 spaces

    def __init__(self, content=None, **kwargs):
        """Constructor.
        Inputs:
        Content - defaults to None. Otherwise is a passed string.
        **kwargs - passable attributes which may be relevent to subclasses."""
        if content:
            self.content = [content]
        else:
            self.content = []
        if kwargs:
            self.atts = kwargs
        else:
            self.atts = ''
        if self.tag:
            self.tag = self.tag
        else:
            self.tag = 'html'

    @staticmethod
    def format_atts(atts=None):
        """Method to format the passed **kwargs into a string ready for rendering.
        Takes the keyword-value pairs and builds a string from them.
        atts: attributes (key-values), defaults to None."""

        if atts:
            atts_string = ''.join(' {} = "{}"'.format(key, value) for key, value in atts.items())
        else:
            atts_string = ''
        return atts_string

    def append(self, new_content):
        """Append method adds additional strings to Content."""
        self.content.append(new_content)

    def render(self, file_out, cur_ind=0):
        """Method to render the input into pretty printing HTML."""
        #Prep whatever kwargs might need to printed
        atts_string = self.format_atts(self.atts)
        #Start Rendering!
        file_out.write('{}<{}{}>\n'.format(cur_ind*self.indent, self.tag, atts_string))
        for stuff in self.content:
            if hasattr(stuff, 'render'):
                stuff.render(file_out, cur_ind=cur_ind+1)
            else:
                line = '{}{}\n'.format((cur_ind+1)*self.indent, stuff)
                file_out.write(line)
        file_out.write('{}</{}>\n'.format(cur_ind*self.indent, self.tag))


class Html(Element):
    """Html tagged subclass of Element."""
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        Element.__init__(self, content=None, **kwargs)

    def render(self, file_out, cur_ind=0):
        file_out.write('<!DOCtype html>\n')
        Element.render(self, file_out, cur_ind=cur_ind)


class Body(Element):
    """Body tagged subclass of Element."""
    tag = 'body'


class P(Element):
    """P tagged subclass of Element."""
    tag = 'p'


class Head(Element):
    """Head tagged subclass of Element."""
    tag = 'head'


class OneLineTag(Element):
    """One Line Tag tagged subclass of Element.
    Over-rides render method to render everything on one line.
    Hence the name."""

    def render(self, file_out, cur_ind=0):
        #Prep whatever kwargs might need to printed
        atts_string = self.format_atts(self.atts)
        #Starts a new line, then writes the tag, all kwargs, and content on that line.
        file_out.write('{}<{}{}>'.format(cur_ind*self.indent, self.tag, atts_string))
        for content in self.content:
            file_out.write(content)
        file_out.write('</{}>\n'.format(self.tag))


class Title(OneLineTag):
    """Title tagged subclass of OneLineTag.
    Used in rendering titles."""
    tag = 'title'


class SelfClosingTag(Element):
    """Closes itself. Cannot contain content."""
    tag = ''

    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError('This element contains content, and is not supposed to. Self-Closing-Tag.')
        else:
            self.content = content
        if kwargs:
            self.atts = kwargs
        else:
            self.atts = ''

    def render(self, file_out, cur_ind=0):
        atts_string = self.format_atts(self.atts)
        file_out.write('{}<{}{} />\n'.format(cur_ind*self.indent, self.tag, atts_string))


class Hr(SelfClosingTag):
    """Subclass of SelfClosingTag. Used for <hr /> tags in html."""
    tag = 'hr'


class Br(SelfClosingTag):
    """Subclass of SelfClosingTag. Used for <br /> tags in html."""
    tag = 'br'


class A(OneLineTag):
    """Subclass of OneLineTag that allows the insertion of a link."""

    tag = 'a'

    def __init__(self, link, content=None):
        if link:
            self.href = str(link)
        else:
            raise TypeError('You are supposed to have a link. class A.')
        OneLineTag.__init__(self, content=content, href=self.href)


class Ul(Element):
    """Unordered list subclass of Element."""
    tag = 'ul'


class Li(Element):
    """List entry subclass of Element."""
    tag = 'li'


class H(OneLineTag):
    """Header subclass of OneLineTag.
    Can take an integer as an input denoting
    what level the header is on."""

    def __init__(self, level, content=None, **kwargs):
        """This initalization method also takes a level as an input.
        Level must be an int, and not too big. I chose 7 as being too big."""

        if ((isinstance(level, int)==True) and ((0 < level) == True) and ((level<7)==True)):
            self.tag = 'h{}'.format(level)
            if content:
                self.content = [content]
            else:
                self.content = []
            if kwargs:
                self.atts = kwargs
            else:
                self.atts = ''
            OneLineTag.__init__(self, content, **kwargs)

        else:
            raise AttributeError('Issue with Header class formatting.')


class Meta(SelfClosingTag):
    """Subclass of SelfClosingTag. Used to catch Meta."""
    tag = 'meta'


