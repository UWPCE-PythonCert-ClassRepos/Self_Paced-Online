#!/usr/bin/env python3
# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson7
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson7
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson7
# git add SampleHTMLRenderer.py
# git add html_render.py
# git commit SampleHTMLRenderer.py
# git commit html_render.py
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson7/
# click Pull request > new pull request

import lesson7.html_render as hr



print('# ## Step 1')
print('# ##########')
page = hr.Element()
page.append(
    "Here is a paragraph of text -- there could be more of them, but this is enough to show that we can do some text.\n")
page.append("And here is another piece of text -- you should be able to add any number.\n")
hr.render_page(page, "test_html_output1.htm")


print()
print()
print('# ## Step 2')
print('# ##########')

page = hr.Html()
body = hr.Body()
body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                  "but this is enough to show that we can do some text"))
body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
page.append(body)
hr.render_page(page, "test_html_output2.html")


print()
print()
print('# ## Step 3')
print('# ##########')
page = hr.Html()
head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))
page.append(head)
body = hr.Body()
body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                  "but this is enough to show that we can do some text"))
body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
page.append(body)
hr.render_page(page, "test_html_output3.html")


print()
print()
print('# ## Step 4')
print('# ##########')
element_list = hr.Html()
head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))
element_list.append(head)
body = hr.Body()
body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough to show that we can do some text",
                  style="text-align: center; font-style: oblique;"))
element_list.append(body)
hr.render_page(element_list, "test_html_output4.html")


print()
print()
print('# ## Step 5')
print('# ##########')

element_list = hr.Html()
head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))
element_list.append(head)
body = hr.Body()
body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough to show that we can do some text",
              style="text-align: center; font-style: oblique;"))
body.append(hr.Hr())
element_list.append(body)
hr.render_page(element_list, "test_html_output5.html")


print()
print()
print('# ## Step 6')
print('# ##########')
element_list = hr.Html()
head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))
element_list.append(head)
body = hr.Body()
body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough to show that we can do some text",
              style="text-align: center; font-style: oblique;"))
body.append(hr.Hr())
body.append("And this is a ")
body.append(hr.A("http://google.com", "link"))
body.append("to google")
element_list.append(body)
hr.render_page(element_list, "test_html_output6.html")


print()
print()
print('# ## Step 7')
print('# ##########')
element_list = hr.Html()
head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))
element_list.append(head)
body = hr.Body()
body.append(hr.H(2, "PythonClass - Class 6 example") )
body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough to show that we can do some text",
              style="text-align: center; font-style: oblique;"))
body.append(hr.Hr())
list = hr.Ul(id="TheList", style="line-height:200%")
list.append(hr.Li("The first item in a list") )
list.append(hr.Li("This is the second item", style="color: red") )
item = hr.Li()
item.append("And this is a ")
item.append( hr.A("http://google.com", "link") )
item.append("to google")
list.append(item)
body.append(list)
element_list.append(body)
hr.render_page(element_list, "test_html_output7.html")



print()
print()
print('# ## Step(s) 8 & 9')
print('# #################')
element_list = hr.Html()
head = hr.Head()
head.append(hr.Meta(charset="UTF-8") )
head.append(hr.Title("PythonClass = Revision 1087:"))
element_list.append(head)
body = hr.Body()
body.append(hr.H(2, "PythonClass - Example") )
body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough to show that we can do some text",
                 style="text-align: center; font-style: oblique;"))

body.append(hr.Hr())
list = hr.Ul(id="TheList", style="line-height:200%")
list.append( hr.Li("The first item in a list") )
list.append( hr.Li("This is the second item", style="color: red") )
item = hr.Li()
item.append("And this is a ")
item.append(hr.A("http://google.com", "link") )
item.append("to google")
list.append(item)
body.append(list)
element_list.append(body)
hr.render_page(element_list, "test_html_output8.html")

