#!/usr/bin/env python

# Step 1:
# 
class Element() :

    # It should have class attributes for the tag name (“html” first) and the indentation (spaces to indent for pretty printing)
    tag = "html"
    indent = 4
    content = ""

    # An Element object has to collect a bunch of sub-elements, in order,
    # and you need to be able to append new ones to it – sounds like a like a list? So should it subclass from list?
    # Ask yourself – does this make sense? an “Element is a list” – no.
    # But “An Element uses a list” makes perfect sense.
    # If the is phrase makes sense, then subclassing would makes sense. If the uses phrase makes sense, then you would not want to subclass.
    # So no – you don’t want Element to subclass from list.
    sub_elements=[]

    # The initializer signature should look like Element(content=None)
    # where content is expected to be a string – and defaults to Nothing.
    def __init__(self, content=None):
        self.content = ""
        if self.content:
            self.content = content
        

    # It should have an append method that can add another string to the content.
    # So your class will need a way to store the content in a way that you can keep adding more to it.
    def append(self, content):
        self.sub_elements.append(content)
        #print ("call Element.append")
        #print (self.sub_elements)


    # It should have a render(file_out, cur_ind = "") method that renders the tag and the strings in the content.
    # file_out could be any open, writable file-like object ( i.e. have a write() method ).
    # This is what you get from the open() function – but there are other kinds of file-like objects.
    # The html will be rendered to this file.
    #  cur_ind is a string with the current level of indentation in it: 
    #   the amount that the entire tag should be indented for pretty printing.
    # This is a little tricky: cur_ind will be the amount that this element should be indented already.
    # It will be from zero (an empty string) to a lot of spaces, depending on how deep it is in the tree. 
    # You could use an integer for the number of spaces to indent – 
    # or keep it simple and just use a string with 2, or 4 or ?? spaces in it.
    # The amount of each level of indentation should be set by the class attribute: indent
    # ex: soo this render() method takes a file-like object, and calls its write() method,
    #   writing the html for a tag. Something like:
    # 
    # <html>
    #     Some content. Some more content.
    # <\html>

    def render(self, file_out, cur_ind = ""):
        file_out.write('<'+self.tag+'>')
        for idx_elm in self.sub_elements: file_out.write(idx_elm)
        file_out.write('<\\'+self.tag+ '>')
        #print (file_out)


# Step 2:
# 
# Create a couple subclasses of Element, for each of <html>, <body>, and <p> tags. All you should have to do is override the tag class attribute (you may need to add a tag class attribute to the Element class first, if you haven’t already).
# 
# Now you can render a few different types of element.
# 
# Note: So why are we subclassing here? Because: “a body element is an Element” makes perfect sense – that’s when you want to subclass. Another way to think about it is that you want to subclass to make a specialized version of something.
# 
# You may note not that the Element class really doesn’t do anything by itself – it needs a tag (at least) to be a proper element. This is what’s called a “Base Class”. It contains functionality required by various subclasses, but may not do anything on its own.
# 
# Extend the Element.render() method so that it can render other elements inside the tag in addition to strings. A recursion-like approach should do it. i.e. it can call the render() method of the elements it contains. You’ll need to be smart about setting the cur_ind optional parameter – so that the nested elements get indented correctly (again, this is a secondary concern…get correct html first).
# 
# Figure out a way to deal with the fact that the contained elements could be either simple strings or Element s with render methods (there are a few ways to handle that…). Think about “Duck Typing” and EAFP. See the section Notes on handling “duck typing” and the end of the Exercise for more.
# 
# You should now be able to render a basic web page with an <html> tag around the whole thing, a <body> tag inside, and multiple <p> tags inside that, with text inside that. And all indented nicely.
# 
# See: test_html_output2.htm
# 
# NOTE: when you run step 2 in run_html_render.py, you will want to comment out step 1 – that way you’ll only get one set of output.





class Html( Element):
    tag = "Html"
    def __init__():
        pass
class Body(Element):
    pass
class P(Element):
    pass



