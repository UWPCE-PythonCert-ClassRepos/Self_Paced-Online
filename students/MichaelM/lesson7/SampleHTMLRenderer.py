#!/usr/bin/env python3

"""
# wk: cd C:\Users\
# v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson7
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson7
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson7
# git add mailroom_lesson06_module.py
# git add mailroom_lesson06.py
# git add test_mailroom_lesson06.py
# git commit mailroom_lesson06_module.py
# git commit mailroom_lesson06.py
# git commit test_mailroom_lesson06.py
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson6/
# click Pull request > new pull request

"""

from io import StringIO
import lesson7.html_render as hr


# writing the file out:
def render_page(HtmlPage, filename, indent=None):
    f = StringIO()
    if indent is None:
        HtmlPage.render(f)
    else:
        HtmlPage.render(f, indent)
    print(f.getvalue())
    with open(filename, 'w') as outfile:
        outfile.write(f.getvalue())


# Step 1
#########

page = hr.Element()
page.html("open", page.indent(0))
page.head("open", page.indent(1))
page.title("A classy html doc", page.indent(2))
page.head("close", page.indent(1))
page.body("open", page.indent(1))
page.p("open", page.indent(2))
page.append_to_list("Here is a paragraph of text -- there could be more of them, but this is enough to show that we can do some text.\n")
page.p("close", page.indent(2))
page.br(page.indent(2))
page.p("open", page.indent(2))
page.append_to_list("And here is another piece of text -- you should be able to add any number.\n")
page.p("close", page.indent(2))
page.body("close", page.indent(1))
page.html("close", page.indent(0))
render_page(page, "html_page.htm")


# ## Step 2
# ##########

# page = hr.Html()

# body = hr.Body()

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text"))

# body.append(hr.P("And here is another piece of text -- you should be able to add any number"))

# page.append(body)

# render_page(page, "test_html_output2.html")

# # Step 3
# ##########

# page = hr.Html()

# head = hr.Head()
# head.append(hr.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text"))
# body.append(hr.P("And here is another piece of text -- you should be able to add any number"))

# page.append(body)

# render_page(page, "test_html_output3.html")

# # Step 4
# ##########

# page = hr.Html()

# head = hr.Head()
# head.append(hr.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#               style="text-align: center; font-style: oblique;"))

# page.append(body)

# render_page(page, "test_html_output4.html")

# # Step 5
# #########

# page = hr.Html()

# head = hr.Head()
# head.append(hr.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#               style="text-align: center; font-style: oblique;"))

# body.append(hr.Hr())

# page.append(body)

# render_page(page, "test_html_output5.html")

# # Step 6
# #########

# page = hr.Html()

# head = hr.Head()
# head.append(hr.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#               style="text-align: center; font-style: oblique;"))

# body.append(hr.Hr())

# body.append("And this is a ")
# body.append( hr.A("http://google.com", "link") )
# body.append("to google")

# page.append(body)

# render_page(page, "test_html_output6.html")

# # Step 7
# #########

# page = hr.Html()

# head = hr.Head()
# head.append(hr.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append( hr.H(2, "PythonClass - Class 6 example") )

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#               style="text-align: center; font-style: oblique;"))

# body.append(hr.Hr())

# list = hr.Ul(id="TheList", style="line-height:200%")

# list.append( hr.Li("The first item in a list") )
# list.append( hr.Li("This is the second item", style="color: red") )

# item = hr.Li()
# item.append("And this is a ")
# item.append( hr.A("http://google.com", "link") )
# item.append("to google")

# list.append(item)

# body.append(list)

# page.append(body)

# render_page(page, "test_html_output7.html")

# # Step 8 and 9
# ##############

# page = hr.Html()


# head = hr.Head()
# head.append( hr.Meta(charset="UTF-8") )
# head.append(hr.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append( hr.H(2, "PythonClass - Example") )

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#                  style="text-align: center; font-style: oblique;"))

# body.append(hr.Hr())

# list = hr.Ul(id="TheList", style="line-height:200%")

# list.append( hr.Li("The first item in a list") )
# list.append( hr.Li("This is the second item", style="color: red") )

# item = hr.Li()
# item.append("And this is a ")
# item.append( hr.A("http://google.com", "link") )
# item.append("to google")

# list.append(item)

# body.append(list)

# page.append(body)

# render_page(page, "test_html_output8.html")