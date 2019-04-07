"""
Name: Muhammad Khan
Date: 03/25/2019
Assignment07

Purpose: A class-based system for rendering html.
"""
#######
#Step 1
#######

class Element(object):
    #Class attributes.
    tag = "html"
    indent="    "
    def __init__(self, content=None, **kwargs):
        """An initializer method.that sets the initial state of the object"""
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.kwargs = kwargs


    def append(self, new_content):
        """
        Return a list with appended new_content
        :parm: new_content   a required positional argument of type string OR
                             instance of the Elment
        """
        return self.contents.append(new_content)


    def render(self, out_file, cur_ind=""):
        """Render the html and write the output to a file"""
        out_file.write(cur_ind + '<{}'.format(self.tag))
        for name, value in self.kwargs.items():
            out_file.write(' {}="{}"'.format(name,value))
        out_file.write(">\n")
        for content in self.contents:
            if isinstance(content , str):
                out_file.write(cur_ind + self.indent + content )
                out_file.write("\n")
            else:
                content.render(out_file,cur_ind + self.indent)
        out_file.write(cur_ind + '</{}>\n'.format(self.tag))

#######
#Step 2
#######

class Body(Element):
    """Body class inherits from the parent Element class"""
    # Attribute overriding.
    tag = "body"


class P(Element):
    """Class for paragraph tag."""
    tag = "p"


class Html(Element):
    """Class for HTML tag."""
    tag = "html"
    def render(self, out_file, cur_ind=""):
        out_file.write('<!DOCTYPE html>\n')
        Element.render(self,out_file, cur_ind="")


#######
#Step 3
#######


class Head(Element):
    """Class for head tag."""
    tag = "head"


class OneLineTag(Element):
    """This class inherits from the element base class"""

    def render(self,out_file,cur_ind = ""):
        """Render the html in a single line and write the output to a file"""
        out_file.write(cur_ind + '<{}'.format(self.tag))
        for name, value in self.kwargs.items():
                out_file.write(' {}="{}"'.format(name,value))
        out_file.write('>')
        for content in self.contents:
            if isinstance(content, str):
                out_file.write(content)
            else:
                content.render(out_file, cur_ind + self.indent)
        out_file.write('</{}>\n'.format(self.tag))


class Title(OneLineTag):
    """Class for Title tag inherits from the OneLineTag base class."""
    tag = "title"


########
# Step 4  Allow constructor of the Element class to accept kwarg argument Done!
########


########
#Step 5.
########


class SelfClosingTag(Element):
    """
    This class inherits from the parent class Element and it provides
    functionality for the self closing html tags.
    """
    #initializer(constructor) overriding
    def __init__(self, content=None, **kwargs):
        """Raise the TypeError exception if the user feeds content"""
        if content:
            raise TypeError("Self closing tags don't take content")
        self.kwargs = kwargs


    # override the render method for self closing tags.
    def render(self, out_file, cur_ind=""):
        """Override the render method in the parent class Element"""
        out_file.write(cur_ind +'<{} '.format(self.tag))
        for name, value in self.kwargs.items():
            out_file.write('{}="{}"'.format(name, value))
        out_file.write('/> \n')


class Hr(SelfClosingTag):
    # Attribute Overriding of the Element class.
    tag = "hr"

class Br(SelfClosingTag):

    tag = "br"


#########
# Step 6
#########


class A(OneLineTag):
    """class attribute"""
    tag = "a"
    """Constructor overriding."""
    def __init__(self, link, content=None, **kwargs):

        kwargs['href'] = link
        super().__init__(content,**kwargs)


###########
# Step 7
###########

class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):
    tag = "h"

    #Constructor overriding to account for level parameter.
    def __init__(self, level,content=None, **kwargs):

        self.tag = self.tag+str(level)
        super().__init__(content, **kwargs)

#########
# step 8
########

# <!DOCTYPE html> is rendered in the html class.

# Add the meta data class.

class Meta(SelfClosingTag):

    tag = "meta"

#########
# Step 9
########

# Indentiation functionality was added.
