"""
HTML Render Assignment

Create an Element class for rendering an html element (xml element).
There is a skeleton for one in html_render.py – it has just enough so that the first few tests in test_html_render.py can run – though that won’t pass!
Do run those tests first – then add the code to make them pass.
The Element class should have a class attribute for the tag name (“html” first).
The initializer signature should look like:
"""

# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None, **kwargs):
        self.contents = [content]
        self.attributes = {**kwargs}
        
    def append(self, new_content):
        if self.contents[0] is None:
            self.contents = [new_content]
        else:
            self.contents.append(new_content)

    def render(self, out_file):
        #loop through list of contents
        open_tag = ["<{}".format(self.tag)]
        for key in self.attributes:
            open_tag.append(" " + key + "=\"" + self.attributes[key] + "\"")
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        #out_file.write("<{}>\n".format(self.tag))            
        for content in self.contents: 
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>".format(self.tag))

class Html(Element):
    """class for HTML text"""
    tag = "html"

class Body(Element):
    """class for body text - all other content is the same"""
    tag = "body"

class P(Element):
    """class of Paragraph text - all ohter content is the same"""
    tag = "p"


# Step 3
# Create header class
class Header(Element):
    tag = "head"

#create:
#1. OneLineTag class with new render method
#2. first subclass for OneLineTag for titles
class OneLineTag(Element):

    def append(self, content):
        raise NotImplementedError

    def render(self, out_file):
        #write one line text from contents
        out_file.write("<{tag}>{content}</{tag}>\n".format(tag=self.tag, content=self.contents))
        
class Title(OneLineTag):
    tag = "title"

# Step 4
# Update Element Class to accept a set of attributes as keywords to 
# the constructor
# (see Element Class lines 26 to 40)

# Step 5
# Create a SelfClosingTag subclass of Element to render tags like:
# <hr /> and <br />

class SelfClosingTag(Element):
    """class to create horizontal rule and line break"""
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag should not have content")
        Element.__init__(self, content=None, **kwargs)
        
    def append(self, *args):
        raise TypeError("cannot add content")

    def render(self, out_file):
        open_tag = ["<{tag}".format(tag=self.tag)]
        for key in self.attributes:
            open_tag.append(" " + key + "=\"" + self.attributes[key] + "\"")
        open_tag.append(" />\n")
        out_file.write("".join(open_tag))     

       
class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

#Step 6
# Create an 'A' class for anchor (link) element
# anchor tag should look like <a href="http://google.com">link to google</a>


class A(OneLineTag):
    """anchor tag similar to href, one liner with link"""
    tag = "a"
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

    def render(self, out_file):
        open_tag = ["<{tag}".format(tag=self.tag)]
        for key in self.attributes:
            open_tag.append(" " + key + "=\"" + self.attributes[key] + "\">")
        out_file.write("".join(open_tag))
        print(self.contents)
        for content in self.contents: 
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write("</{tag}>".format(tag=self.tag))

#Step 7
#Header elements: '<h2> Python Class - Html rendering example </h2>'
#the tag should be an instance attribute so I can change it from h1 to h2, etc
#most like the OneLineTag class (exactly like the title)

class H(OneLineTag):
    """tag will be instance attribute"""
    def __init__(self, tag, content=None):
        self.tag=tag
        self.contents = content







        
        

        






