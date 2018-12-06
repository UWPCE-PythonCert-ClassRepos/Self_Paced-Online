import html_render as hr
from io import StringIO

page = hr.Html()
body = hr.Body()
p1 = hr.P()
p1.append("Here is a paragraph of text")
p1.append("And here is another piece of text")
body.append(p1)
page.append(body)
f = StringIO()
page.render(f)
res_string = "<html>\n" \
             "   <body>\n" \
             "      <p>\n" \
             "         Here is a paragraph of text\n" \
             "      </p>\n" \
             "      <p>\n" \
             "         And here is another piece of text\n" \
             "      </p>\n" \
             "   </body>\n" \
             "</html>\n"
print(f.getvalue())
print(res_string)
#assert f.getvalue() == res_string