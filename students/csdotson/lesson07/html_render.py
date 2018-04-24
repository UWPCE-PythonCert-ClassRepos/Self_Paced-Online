class Element:
    """Create an Element class for rendering an html element"""
    tag_name = ''
    indentation = ""

    def __init__(self, content=None):
        self.content = [content] if content else []

    def append(self, content_to_add):
        self.content.append(content_to_add)

    def render(self, file_out, cur_ind=""):
        opening_tag = "<"+self.tag_name+">\n"
        closing_tag = "</"+self.tag_name+">"
        output = opening_tag
        for elem in self.content:
            output += (elem + "\n")
        output += closing_tag
        file_out.write(output)


class Html(Element):
    tag_name = 'html'



class Body(Element):
    tag_name = 'body'



class P(Element):
    tag_name = 'p'


# class TextWrapper:
#     """
#     A simple wrapper that creates a class with a render method
#     for simple text
#     """
#     def __init__(self,text):
#         self.text = text
#
#      def render(self, file_out, current_ind=""):
#         file_out.write(current_ind)
#         file_out.write(self.text)
