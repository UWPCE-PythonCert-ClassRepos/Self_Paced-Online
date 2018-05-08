class Element:
    """Create an Element class for rendering an html element"""
    tag_name = "html"
    indentation = '    '

    def __init__(self, content=None, **attrs):
        self.content = [content] if content else []
        self.attributes = attrs
        # if isinstance(self, SelfClosingTag):
        #     if self.content:
        #         raise TypeError("Self closing tag cannot have content")

    def append(self, content_to_add):
        # if isinstance(content_to_add, str):
        #     self.content.append(TextWrapper(content_to_add))
        # else:
            self.content.append(content_to_add)
#
#     def attr_render(self, file_out, cur_ind=0):
#         if self.attributes:
#             file_out.write( (cur_ind * self.indentation) + "<"+self.tag_name)
#             for key, value in self.attributes.items():
#                 file_out.write(f" {key}=\"{value}\"")
#             file_out.write(">\n")
#         else:
#             file_out.write( (cur_ind * self.indentation) + "<"+self.tag_name+">\n")
#
    def render(self, file_out, cur_ind=0):
#         Element.attr_render(self, file_out, cur_ind)
#         for elem in self.content:
#             cur_ind += 1
#             if isinstance(elem, str):
#                 elem = TextWrapper(elem)
#             elem.render(file_out, cur_ind)
#             cur_ind -= 1
        file_out.write( (cur_ind * self.indentation) + "</"+self.tag_name+">\n")
#
#
# class Html(Element):
#     tag_name = 'html'
#     indentation = ''
#     def render(self, file_out, cur_ind=0):
#         file_out.write("<!DOCTYPE html>\n")
#         Element.render(self, file_out, cur_ind)
#
#
# class Head(Element):
#     tag_name = 'head'
#
#
# class Body(Element):
#     tag_name = 'body'
#
#
# class P(Element):
#     tag_name = 'p'
#
#
# class A(Element):
#     tag_name = "a"
#     def __init__(self, link, content):
#         Element.__init__(self, content, href=link)
#
#
# class Ul(Element):
#     tag_name = 'ul'
#
#
# class Li(Element):
#     tag_name = 'li'
#
#
# class OneLineTag(Element):
#     def render(self, file_out, cur_ind=0):
#         open_tag = (cur_ind * self.indentation) + "<"+self.tag_name+">"
#         close_tag = "</"+self.tag_name+">\n"
#         file_out.write(open_tag + self.content[0] + close_tag)
#
#
# class Title(OneLineTag):
#     tag_name = 'title'
#
#
# class H(OneLineTag):
#     tag_name = 'h'
#     def __init__(self, level, content):
#         self.tag_name += str(level)
#         Element.__init__(self, content)
#
#
# class SelfClosingTag(Element):
#     def render(self, file_out, cur_ind=0):
#         Element.attr_render(self, file_out, cur_ind)
#
#
# class Hr(SelfClosingTag):
#     tag_name = 'hr'
#
#
# class Br(SelfClosingTag):
#     tag_name = 'br'
#
#
# class Meta(SelfClosingTag):
#     tag_name = 'meta'
#
#
# class TextWrapper:
#     """
#     A simple wrapper that creates a class with a render method
#     for simple text
#     """
#     indentation = '    '
#
#     def __init__(self, text):
#         self.text = text
#
#     def render(self, file_out, cur_ind=0):
#         file_out.write(cur_ind * self.indentation)
#         file_out.write(self.text + "\n")
