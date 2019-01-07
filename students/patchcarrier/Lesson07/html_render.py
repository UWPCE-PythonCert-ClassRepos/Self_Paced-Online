class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    indent = 4
    
    def __init__(self, text):
        self.text = text

    def render(self, outfile, cur_ind=0):
        outfile.write(self.text)
        

class Element:
    
    #Indent is the number of spaces for each indent
    indent = 4
    
    def __init__(self, content=None, **kwargs):
        """Initialize an Element instance.
        
        Inputs:
        content - A string or another Element object (or subclass of Element)
                  which is contained by this Element instance
        kwargs - A dictionary containing attribute names and values for this instance
        """
        
        #The instance variable attributes is a dictionary of attribute names
        #and their corresponding values
        self.attributes = kwargs
        #The instance variable contents is a list of strings or other html
        #elements. Objects should only be added to self.contents through the 
        #Element.append method to retain the invariant that all objects in 
        #self.contents have a render method. Assigning directly to self.contents
        #could violate this invariant.
        self.contents = []
        if content is not None:
            self.append(content)
           
    def append(self, content):
        """Add the object content to self.contents.
     
        This method retains the invariant that all objects in self.contents
        must have a render method.
        """
 
        #If content doesn't have a render method, create a TextWrapper 
        #instance for it so it can be rendered.
        if hasattr(content, 'render'):
            self.contents.append(content)
        else:
            self.contents.append(TextWrapper(str(content)))       

    def write_tag_attributes(self, outfile):
        """Write the tag opener and the attributes of the element to the current
        position in outfile.
        
        Inputs:
        outfile - an open file-like object
        """
        
        outfile.write("<{}".format(self.tag))
        for attribute, value in self.attributes.items():
            outfile.write(' {}="{}"'.format(attribute, value))
        
    def render(self, outfile, cur_ind=0):
        """Render the html tags in self.contents in the open file-like object outfile.
    
        Inputs:
        cur_ind - An integer specifying the number of indent levels, where each
                  indent level consists of self.indent number of spaces.
        """
                       
        #Write tag and attributes
        Element.write_tag_attributes(self,outfile)
        outfile.write(">\n")
        
        #Render all of the objects in self.contents.
        #All of the objects in content should have a render method
        #this is inforced by Element.append()
        indent_str = cur_ind * self.indent * ' '
        for content in self.contents:
            outfile.write(indent_str + self.indent * ' ')
            content.render(outfile, cur_ind + 1)
            outfile.write("\n")
        
        #Write the closing tag
        outfile.write("{}</{}>".format(indent_str, self.tag))
       
        
class Html(Element):
    """Element representing an html tag."""
    
    tag = "html"
     
    def render(self, outfile, cur_ind=0):
        """Write the document type to outfile and then render an html tag like 
        every other type of element.
        """
        outfile.write("<!DOCTYPE html>\n")
        Element.render(self, outfile, cur_ind=cur_ind)
   
    
class Body(Element):
    """Element representing a body tag. """
    tag = "body"
    
    
class P(Element):
    """Element representing a paragraph tag."""
    tag = "p"
    

class Head(Element):
    """Element representing a head tag."""
    tag = "head"
    

class OneLineTag(Element):
    """An element that renders all of it's contents on a single line.
    
    In order for all of the contents to be rendered on a single line, all objects
    in self.contents must be instances of either OneLineTag, a subclass of OneLineTag,
    or the TextWrapper class. This requirement is not checked or maintained by 
    the class.
    """
    
    def render(self, outfile, cur_ind=0):
        """Render the html tags in self.contents on a single line in the open 
        file-like object outfile.
    
        Inputs:
        cur_ind - An integer specifying the number of indent levels, where each
                  indent level consists of self.indent number of spaces.
        """
        #Render the tag and attributes
        Element.write_tag_attributes(self,outfile)
        outfile.write(">".format(self.tag))
        
        #Render the contents
        for content in self.contents:
            content.render(outfile, cur_ind=0)
        outfile.write("</{}>".format(self.tag))  
  
    
class Title(OneLineTag):
    """Element representing a title tag."""
    tag = "title"
    

class SelfClosingTag(Element):
    """A class for self closing tags. Self closing tags don't have a contents
    instance variable.
    """
    
    def __init__(self, **kwargs):
        """Initialize a SelfClosingTag instance. 
        
        Inputs:
        kwargs - A dictionary containing attribute names and values for this instance
        """
        self.attributes = kwargs
    
    def render(self, outfile, cur_ind=0):
        """Render the tag and attributes."""
        
        Element.write_tag_attributes(self,outfile)
        outfile.write(" />".format(self.tag))        
    
    def append(self, *args, **kwargs):
        """Raise an error if the user tries to add content. Self closing tags
        don't support the addition of content."""
        raise TypeError("append() method not supported for class SelfClosingTag")


class Hr(SelfClosingTag):
    """Element representing a hr tag."""
    tag = "hr"


class Br(SelfClosingTag):
    """Element representing a br tag."""
    tag = "br"
    
    
class A(OneLineTag):
    """Element representing an anchor tag."""
    tag = "a"
    
    def __init__(self, link, content, **kwargs):
        """Initialize an instance of an anchor element.
        
        Inputs:
        link - the web address of the link (string)
        content - the text that should be displayed for the link (string)
        kwargs - A dictionary containing attribute names and values for this instance.
                 The addribute href is automatically added with link set as its value.
        """
        Element.__init__(self, content, href=link, **kwargs)
   
     
class Ul(Element):
    """Element representing an unordered list tag."""
    tag = "ul"
    
    
class Li(Element):
    """Element representing a list tag."""
    tag = "li"
    

class H(OneLineTag):
    """Element representing a header tag."""
    
    def __init__(self, header_level, content=None, **kwargs):
        """Initialize an instance of a header element.
        
        Inputs:
        header_level - An integer representing the header level (e.g. 1,2,3)
        content - the text that should be displayed for the link (string)
        kwargs - A dictionary containing attribute names and values for this instance.
                 The addribute href is automatically added with link set as its value.
        """
        #Tag is an instance variable for the H class because of the different
        #header levels possible (e.g. h1, h2, h3)
        self.tag = "h{:d}".format(header_level)
        Element.__init__(self, content, **kwargs)
        
        
class Meta(SelfClosingTag):
    """Element representing a meta tag."""
    tag = "meta"