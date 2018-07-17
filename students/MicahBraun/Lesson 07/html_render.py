# ----------------------------------------------------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: Assignment 07 - html_render.py
# PURPOSE: html-page-creating module
# DATE: 07/16/2018
#
# DESCRIPTION: class Element and subclasses combine to form a module which can write out HTML-compatible page
# information (in the style of class example). Using <tag> conventions.
#
# NOTE: I had hoped to add a <style> and body{} element to add more CSS customization but ran out of time for now.
# ----------------------------------------------------------------------------------------------------------------------


class Element:
    """Element class for rendering an HTML element"""
    tag = ''
    indent = '    '

    def __init__(self, content=None, **attributes):
        """
        Class Initializer
        :param content: if parameter has value other than None (empty) content = list[content] else empty list
        :param attributes: variable len keyword argument(s) attributes for formatting tags
        """
        if content is not None:
            self.content = [content]
        else:
            self.content = []
        self.attributes = attributes

    def append(self, content):
        """
        Method: append()
        :param content: appends content to existing
        :return
        """
        self.content.append(content)

    def render(self, f_out, cur_ind=''):
        """
        Method: render()
        :param f_out: Element method for writing tags as file object to .html
        :param cur_ind: for obtaining correct indentation of tag element
        :return
        """
        f_out.write(f'{cur_ind}<{self.tag}{self.f_attributes()}>\n')

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(f_out, cur_ind + self.indent)
            else:
                f_out.write(cur_ind + self.indent + str(item) + '\n')

        f_out.write(cur_ind + f'</{self.tag}>\n')

    def f_attributes(self):
        """
        Method: f_attributes - formats attributes
        :return: formatted attributes
        """
        if self.attributes:
            attributes = ' ' + ' '.join(f'{k}="{v}"' for k, v in self.attributes.items())
        else:
            attributes = ''

        return attributes


class Html(Element):
    """
    HTML subclass of class Element
    """
    tag = 'html'

    def render(self, f_out, cur_ind=''):
        """
        Method: render() - Renders the tag and strings from the element content.
        ::param f_out - Sends writeable file object to receive rendered data.
        ::param cur_ind - With default of ''. Used for indentation of current element.
        ::return
        """
        f_out.write(f'{cur_ind}<!DOCTYPE html>\n')
        super().render(f_out, cur_ind)


class Body(Element):
    """
    Body element
    """
    tag = 'body'


class P(Element):
    """
    Paragraph element
    """
    tag = 'p'


class Head(Element):
    """
    Head element
    """
    tag = 'head'


class OneLineClass(Element):
    """
    Override existing Element.render()
    """
    def render(self, f_out, cur_ind=''):
        """
        Method: render() - Overrides Element.render() to print elements on one line.
        ::param f_out - Sends writeable file object to receive rendered data.
        ::param cur_ind - With default of ''. Used for indentation of current element.
        ::return dependent on content
        """
        f_out.write(f'{cur_ind}<{self.tag}{self.f_attributes()}>')

        for obj in self.content:                            # for each item/object in content
            if hasattr(obj, 'render'):                      # if it has an attribute(name, 'string')
                obj.render(f_out, cur_ind + self.indent)    # render obj(filename, indent(s))
            else:
                f_out.write(str(obj) + ' ')                 # else: write str(obj) empty space

            f_out.write(f'</{self.tag}>\n')                 # write closing tag


class Title(Element):
    """
    Title element
    """
    tag = 'title'


class SelfClosingTag(Element):
    """
    Subclass of Element for self-closing tags
    """
    def render(self, f_out, cur_ind=''):
        """
        Overwrites existing
        :param f_out: "
        :param cur_ind: "
        :return: "
        """
        f_out.write(f'{cur_ind}</{self.tag}{self.f_attributes()}>\n')


class Hr(Element):
    """
    Hr element
    """
    tag = 'hr'


class Br(Element):
    """
    Br element
    """
    tag = 'br'


class A(Element):
    """
    'A' == Anchor class for html anchoring of content (e.g. links)
    """
    tag = 'a'

    def __init__(self, link, content):
        super().__init__(content, href=link)


class Ul(Element):
    """
    Unordered List object (e.g. <ul>)
    """
    tag = 'ul'


class Li(Element):
    """
    List Item object (e.g. <li>
    """
    tag = 'li'


class H(OneLineClass):
    """
    Header object
    """
    def __init__(self, level, content):
        super().__init__(content)
        self.tag = f'h{level}'


class Meta(SelfClosingTag):
    """
    Meta charset="UTF-8" encoding tag
    """
    tag = 'meta'


class Img(Element):
    """
    Image tag subclasses from Element, override __init__() to accept img required values
    """
    tag = 'img'

    def __init__(self, source, alternate, ht=100, wd=100, hspace=100):
        super().__init__(src=source, alt=alternate, height=ht, width=wd, hspace=hspace)
