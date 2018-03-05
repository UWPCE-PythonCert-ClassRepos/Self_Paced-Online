class Element:

    # Class Attributes
    tag = ""
    indent = "  "


    def __init__(self, content=None, **style):
        self.content = [content] if content else []
        self.styles = style


    def append(self, words):
        self.content.append(words)


    def render(self, fileout, cur_ind=""):
        #print(self, "-cur_ind:{}end".format(cur_ind))

        fileout.write(cur_ind + "<{}".format(self.tag))
        for key, value in self.styles.items():
            fileout.write(' {}="{}"'.format(key,value))
        fileout.write(">\n")
        for item in self.content:
            if isinstance(item, Element):
                item.render(fileout, cur_ind + self.indent)
            else: # output the content
                fileout.write(cur_ind + self.indent + item)
                fileout.write("\n")

           #print(fileout.getvalue())
        fileout.write(cur_ind + "</{}>\n".format(self.tag))


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class Title(Element):
    tag = 'title'

    def render(self, fileout, cur_ind=""):
        fileout.write(cur_ind + "<{}>".format(self.tag))

        for item in self.content:
            if isinstance(item, Element):
                item.render(fileout)
            else:
                fileout.write(item)
        fileout.write("</{}>\n".format(self.tag))


    '''
    el = Element("First content here")
    print(el.content)
    el.append("second sentence")
    print(el.content)
    '''
