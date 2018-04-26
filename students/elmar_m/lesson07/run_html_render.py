#!/usr/bin/env python3

# file: run_html_render.py -- DO NOT CHANGE !

"""
a simple script can run and test your html rendering classes.

Uncomment the steps as you add to your rendering.

"""

from io import StringIO

# importing the html_rendering code with a short name for easy typing.
import html_render as hr




# Step 1
#########

# page = hr.Element()     
#     # erzeuge ein Objekt der Klasse hr.Element und nenne es page
# 
# page.append("Here is a paragraph of text -- there could be more of them, "
#             "but this is enough  to show that we can do some text")     
#     # fuehre die Methode 'append' des Objektes
#     # page aus und uebergib ihm als Argument 
#     # zwei Strings
# 
# page.append("And here is another piece of text -- you should be able to add any number")
#     # fuehre die Methode 'append' des Objektes page noch einmal aus und
#     # uebergib ihm einen anderen String als Argument
# 
# render_page(page, "output1.html")
    # fuehre die Funktion 'render_page' aus und uebergib ihr zwei Argumente: das Objekt 
    # namens page und einen String fuer den Namen des zu erzeugenden Files

# The rest of the steps have been commented out.
#  Uncomment them as you move along with the assignment.

# writing the file out:
def render_page(page, filename):
    """
    render the tree of elements

    This uses StringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = StringIO()      # erzeuge ein StringIO Objekt namens f
    # page.render(f, "----")      # fuehre die Methode 'render' des Objekts 'page' aus 
    page.render(f, "    ")      # fuehre die Methode 'render' des Objekts 'page' aus 
                                # und uebergib ihr zwei Argumente: 
                                # 1. das ein StringIO Objekt
                                # 2. einen leeren String bzw. einen String mit 4 Leerzeichen

    print(f.getvalue())         # gib den Inhalt des StringIO Objektes auf dem Bildschirm aus

    with open(filename, 'w') as outfile:    # erzeuge das Fileobjekt outfile und oeffne es im Schreibmodus
        outfile.write(f.getvalue())         # fuehre die Methode 'write' des Fileobjekts aus und uebergib 
                                            # ihr den Inhalt des StringIO Objektes 'f' als Argument

# ## Step 2
# ##########

#page = hr.Html()    # erzeuge ein Objekt der Klasse hr.Html und nenne es page
#
#body = hr.Body()    # erzeuge ein Objekt der Klasse hr.Body und nenne es body
#
#body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                 "but this is enough  to show that we can do some text"))
#                    # fuehre die append Methode des Objekts body aus und uebergib ihr ein
#                    # Objekt der Klasse hr.P als Argument, dieses Objekt wiederum bekommt
#                    # zwei Strings als Argument uebergeben
#
#body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
#
#page.append(body)
#
#render_page(page, "output2.html")




# # Step 3
# ##########

page = hr.Html()
 
head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))
 
page.append(head)
 
body = hr.Body()

body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                "but this is enough  to show that we can do some text"))
body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
 
page.append(body)
 
render_page(page, "output3.html")

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

# # Step 8
# ########

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
