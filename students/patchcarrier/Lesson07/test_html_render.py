import html_render as hr
from io import StringIO

def check_render1(elt, render_indent):
    """Test the Element.render() function for step1.
    
    Inputs:
    elt - an Element instance to render
    render_indent - The number of indentation levels
    """
    
    #Render the html tag, writing everything to the string stream outf
    outf = StringIO()
    elt.render(outf, cur_ind=render_indent)
    #Return the position of the streem outf to the beginning
    outf.seek(0)
    
    #Remove empty lines at the beginning of the string stream
    line = outf.readline()
    start_ind = line.find('<')  
    #Check that the indent level is correct
    assert start_ind * ' ' == elt.indent * render_indent * ' '
    #Check that the first line is an html tag
    assert line[start_ind : start_ind + len('<html>')] == '<html>'
    
    #Check that each line in Element.contents was output
    for cur_content, outline in zip(elt.contents, outf):
        assert outline.lstrip().replace('\n','') == cur_content
        print(outline)
        
    line = outf.readline()
    start_ind = line.find('<')
    assert start_ind * ' ' == elt.indent * render_indent * ' '
    #Check that the last line is the close-out tag
    assert line[start_ind : start_ind + len('</html>')] == '</html>'

def test_step1():

    #Create an element instance, and one with content in it
    empty_elt = hr.Element()
    content_elt = hr.Element('starting string')
    
    #Ensure that the contents list instance variable got initialized correctly
    assert len(empty_elt.contents) == 0
    assert content_elt.contents[0] == 'starting string'
    
    #Add content to both elements to verify functionality of Element.append()
    empty_elt.append('my first string')
    content_elt.append('my second string')
    assert len(empty_elt.contents) == 1
    assert len(content_elt.contents) == 2
    
   
    check_render1(empty_elt,0)
    check_render1(content_elt,1)
    
def test_indentation():
    pass
    
def test_step2():
    
    # Create an element with no contents
    empty_page = hr.HTML()
    assert len(empty_page.contents) == 0
    
    # Create an element with a mix of strings and other element objects
    page = hr.HTML()
    body = hr.Body()
    p1 = hr.P("Here is a paragraph of text -- there could be more of them, "
                  "but this is enough  to show that we can do some text")
    assert len(p1.contents == 1)
    p2 = hr.P()
    p2.append("This is a second paragraph of text)
    body.append(p1)
    body.append(p2)
    assert len(body.contents) == 2
    page.append(body)
    assert len(page.contents) == 1
    
    
    
    
    
# page = hr.Html()

# body = hr.Body()

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text"))

# body.append(hr.P("And here is another piece of text -- you should be able to add any number"))

# page.append(body)

# render_page(page, "test_html_output2.html")
    
    
     
 