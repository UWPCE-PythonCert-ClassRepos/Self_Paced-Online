import html_render as hr
from io import StringIO

page = hr.Element()
f = StringIO()
page.render(f)
print(f.getvalue())