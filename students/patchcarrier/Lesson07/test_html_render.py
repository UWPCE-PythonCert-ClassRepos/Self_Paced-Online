import html_render as hr
from io import StringIO
import sys
import pytest as pt
  
    
def get_start_tag(line):
    """Return the start tag (if one exists) on a line of input from an html file.
    If a starting tag doesn't exist on the line, an empty string is returned."""
    
    # Look for a closing tag on the current line
    close_start = line.find("</")
    
    # If a closing tag is present, look for the start of the opening tag before
    # the closing tag
    if close_start >= 0:
        start_i = line.find("<", 0, close_start)
    else:
        start_i = line.find("<")
        
    if start_i >= 0 :
        end1 = line.find(">", start_i + 1)
        end2 = line.find(" ", start_i + 1)
        if end2 >= 0:
            end_i = min([end1, end2])
        else:
            end_i = end1
        return line[start_i + 1 : end_i].replace(" ","")
    else:
        return ""
    
    
def get_end_tag(line):
    """Return the end tag (if one exists) on a line of input from an html file.
    If a starting tag doesn't exist on the line, an empty string is returned."""
    
    start_i = line.find("</")
    
    if start_i >= 0:
        # start looking for the character ">" starting after the string "</"
        end_i = line.find(">", start_i + 2)
        return line[start_i + 2 : end_i].replace(" ","")
    else:
        return ""
    
    
def check_rendering(outf, start_tags, end_tags):
    """Ensure that the html tags in outf are rendered properly.
    
    Inputs:
    outf - file like object containing the rendered output
    start_tags - list of strings with length equal to the number of lines in
                 outf. Each string indicates the starting tag that should be present
                 in the corresponding line in outf. An empty string in start_tags
                 indicates that no starting tag should be present on the corresponding line
                 in outf
    end_tags - like start_tags, but each string corresponds to the end tag
               that should be present on each line in outf.
    
    """
    
    for line, start_t, end_t in zip(outf, start_tags, end_tags):
        # Get the start and end tags that were actually rendered:
        r_start = get_start_tag(line)
        r_end = get_end_tag(line)
        
        # Verify that the expected tags match what is rendered
        assert r_start == start_t
        assert r_end == end_t
        

def test_step2():
    """Test the render method for Html, body, and p tags as well as for
    the TextWrapper class."""
    
    # Create an element with no contents
    empty_page = hr.Html()
    assert len(empty_page.contents) == 0
    
    # Create an element with a mix of strings and other element objects
    page = hr.Html()
    body = hr.Body()
    
    # Initialize an instance of the P class with content
    p1 = hr.P("Here is a paragraph of text -- there could be more of them, "
                  "but this is enough  to show that we can do some text")
    assert len(p1.contents) == 1
    assert isinstance(p1.contents[0], hr.TextWrapper)
    
    # Create an instance of the P class with no content and add it
    p2 = hr.P()
    assert len(p2.contents) == 0
    p2.append("This is a second paragraph of text")
    assert len(p1.contents) == 1
    
    body.append(p1)
    body.append(p2)
    assert len(body.contents) == 2
    page.append(body)
    assert len(page.contents) == 1
    
    # Check that start and end tags are rendered properly:
    outf = StringIO()
    page.render(outf)
    outf.seek(0)
    start_t = ["!DOCTYPE","html","body","p","","","p","","","",""]
    end_t = ["","","","","","p","","","p","body","html"]
    check_rendering(outf, start_t, end_t)
    
    # Check that text is rendered properly using TextWrapper.render()
    outf = StringIO()
    p2.render(outf)
    outf.seek(0)
    # remove <p> tag line
    outf.readline()
    # content that was rendered
    r_text = outf.readline().lstrip().replace("\n","")
    assert r_text == "This is a second paragraph of text"
    
    
def test_step3():
    """Check that one line tag elements are rendered correctly."""
    
    page = hr.Html()    
    # Check that Title is an instance of OneLineTag
    head = hr.Head(hr.Title("Title Test"))
    assert isinstance(head.contents[0], hr.OneLineTag)
    
    page.append(head)
    body = hr.Body()
    body.append(hr.P("One paragraph."))
    body.append(hr.P("Antoerh paragraph."))
    page.append(body)
 
    
    outf = StringIO()
    page.render(outf)
    outf.seek(0)
    # One line tags should have an opening and closing tag on the same line
    start_t = ["!DOCTYPE","html","head","title","","body","p","","","p","","","",""]
    end_t = ["","","","title","head","","","","p","","","p","body","html"]
    check_rendering(outf, start_t, end_t)
     

def test_step4():
    """Check that the Element and OneLineTag constructors accept attributes and
    that they are rendered properly."""
    
    # Check that the attributes are printed in the p tag opener
    p1 = hr.P(first="Jimmy", last="John")
    outf = StringIO()
    p1.render(outf)
    outf.seek(0)
    p_line = outf.readline()
    start_i = p_line.find('<')
    end_i = p_line.find('>')
    # String with the p tag attributes and no spaces:
    attributes = p_line[start_i + 2 : end_i].replace(" ","")
    assert attributes == 'first="Jimmy"last="John"'
    
    # Check that attributes are printed properly in the Title (one line tag subclass)
    # tag opener
    head = hr.Head(hr.Title("This is a Title", best_title="yes", worst_title="no"))
    outf = StringIO()
    head.render(outf)
    outf.seek(0)
    outf.readline() 
    title_line = outf.readline()
    start_i = title_line.find('<')
    end_i = title_line.find('>')
    attributes = title_line[start_i + len('<title') : end_i].replace(" ","")
    assert attributes == 'best_title="yes"worst_title="no"'
    
    
def test_step5():
    """Check that self closing tags are rendered properly and that content
    can't be added to them without raising an exception."""
    
    with pt.raises(TypeError):
        myhr = hr.Hr("some content")
        
    with pt.raises(TypeError):
        br = hr.Br()
        br.append("some content")
        
    myhr = hr.Hr()
    outf = StringIO()
    myhr.render(outf)
    outf.seek(0)
    line = outf.readline().replace(" ","")
    assert line == "<hr/>"
    
    
def test_step6():
    """Check that anchor tags are rendered properly and that they can
    accept attributes."""
    
    
    # Check that the anchor tag is rendered correctly
    link = hr.A("https://tenor.com/search/baby-goat-gifs","GOATS!!", 
                style="color: yellow")
    
    outf = StringIO()
    link.render(outf)
    outf.seek(0)
    
    # Get the rendered output, attributes are stored in a dictionary so there is
    # no guarante which oder they are printed in, check the two possibilities:
    render_out = outf.readline().replace(" ","")
    out1 = '<ahref="https://tenor.com/search/baby-goat-gifs"' \
            'style="color:yellow">GOATS!!</a>'
    out2 = '<astyle="color:yellow"' \
            'href="https://tenor.com/search/baby-goat-gifs">GOATS!!</a>'
    assert render_out == out1 or render_out == out2
    
    # Create an output file to see if the link text is displayed properly
# =============================================================================
#     with open('yellow_link.html','w') as outf:
#         
#         html = hr.Html(hr.Head(hr.Title("Yellow Link Page")))
#         body = hr.Body()
#         p1 = hr.P("Here is a link to some")
#         body.append(p1)
#         p1.append(link)
#         html.append(body)
#         html.render(outf)
# =============================================================================
        
        
def test_step7():
    """Check that lists are rendered properly and that header elements of 
    different levels can be created."""
    
    # Verify the rendering of lists
    my_list = hr.Ul()
    l1 = hr.Li("item 1")
    l2 = hr.Li("item 2")
    l3 = hr.Li("item 3")
    my_list.append(l1)
    my_list.append(l2)
    my_list.append(l3)
    
    outf = StringIO()
    my_list.render(outf)
    outf.seek(0)
    # check that the tags are in the correct location
    start_t = ["ul","li","","","li","","","li","","",""]
    end_t = ["","","","li","","","li","","","li","ul"]
    check_rendering(outf, start_t, end_t)
    
    # Verify that header tags can be different levels
    h1 = hr.H(1,"Level1")
    h2 = hr.H(2,"Level2",style="color: blue")
    h3 = hr.H(3,"Level3",style="color: yellow")
    assert h1.tag == "h1"
    assert h2.tag == "h2"
    assert h3.tag == "h3"
    
    outf = StringIO()
    h3.render(outf)
    outf.seek(0)
    line = outf.readline().replace(" ","")
    assert line == '<h3style="color:yellow">Level3</h3>'
    
    # Generate some output to look at
    html = hr.Html(hr.Head(hr.Title("Header Practice")))
    body = hr.Body()
    body.append(h1)
    body.append(hr.P("This is a long paragraph"))
    body.append(h2)
    body.append(hr.P("Omg this paragraph is so long"))
    body.append(h3)
    body.append(hr.P("This paragraph is super long and has a list!"))
    body.append(my_list)
    html.append(body)
    
# =============================================================================
#     with open('Headers.html','w') as outf:
#         html.render(outf)
# =============================================================================
        
        
def test_step8():
    """Verify that html tag render include <!DOCTYPE html> and that meta tags are 
    rendered correctly."""
    
    # Check that the DOCTYPE html string is rendered for HTML tags
    html = hr.Html()
    outf = StringIO()
    html.render(outf)
    outf.seek(0)
    # Get the first line and remove trailing white space
    doc_line = outf.readline()
    doc_line = doc_line[::-1].lstrip()
    doc_line = doc_line[::-1]
    assert doc_line == "<!DOCTYPE html>"
    
    # Check that meta tags are rendered correctly
    head = hr.Head(hr.Meta(charset="UTF-8"))
    outf = StringIO()
    head.render(outf)
    outf.seek(0)
    outf.readline()
    meta_line = outf.readline().replace(" ","").replace("\n","")
    assert meta_line == '<metacharset="UTF-8"/>'
