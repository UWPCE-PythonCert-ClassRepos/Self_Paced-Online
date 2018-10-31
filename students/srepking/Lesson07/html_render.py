class Element:
    """Creates html code for given inputs"""
    tag = 'html'
    indent = '   '  # three spaces for indent attribute

    def __init__(self,
                 content=None,
                 **kwargs):
        self.html_format = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, some_string):
        self.contents.append(some_string)

    def _opentag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.html_format.items():
            open_tag.append(" {key}=\"{value}\"".format(key=key, value=value))
        return "".join(open_tag)

    def _closetag(self):
        close_tag = "</{self.tag}>\n".format(self=self)
        return close_tag

    def render(self, file_out, cur_ind=""):
            file_out.write(cur_ind)
            file_out.write(self._opentag())
            file_out.write(">\n")
            for content in self.contents:
                try:
                    content.render(file_out, str(cur_ind+self.indent))
                except AttributeError:
                    file_out.write(cur_ind + self.indent + content)
                    file_out.write('\n')
            file_out.write(cur_ind)
            file_out.write(self._closetag())


class Html(Element):
    """Creates html code for given inputs"""
    tag = 'html'

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + '<!DOCTYPE html>\n')
        Element.render(self, file_out, cur_ind)


class Body(Element):
    """Subclass of Element with 'body' tag for body"""
    tag = 'body'


class P(Element):
    """Subclass of Element with 'p' tag for paragraph"""
    tag = 'p'


class Head(Element):
    """Subclass of Element with head tag for header"""
    tag = 'head'


class OneLineTag(Element):
    """Subclass of Element for one line tag."""
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind)
        file_out.write(self._opentag())
        file_out.write('>')
        file_out.write("".join(self.contents))
        file_out.write(self._closetag())


class Title(OneLineTag):
    """Subclass of OneLineTag used for page title"""
    tag = 'title'


class Br(Element):
    """Subclass of OneLineTag used for page title"""
    tag = 'br '

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind)
        file_out.write(self._opentag() + '/>\n')

    def append(self, some_string):
        raise TypeError('No appending to this object.')

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError('No string object expected')
        else:
            super().__init__(content, **kwargs)


class Hr(Element):
    """Subclass of OneLineTag used for page title"""
    tag = 'hr '

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind)
        file_out.write(self._opentag() + '/>\n')

    def append(self, some_string):
        raise TypeError('No appending to this object.')

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError('No appending to this object')
        else:
            super().__init__(content, **kwargs)


class A(OneLineTag):
    """Take a link and a description of the line and wrap is
    with html anchor constructor."""
    tag = 'a'

    def __init__(self,
                 link, content, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    """Create a header class to create this tag:
        <h2>PythonClass - Class 6 example</h2>"""
    def __init__(self,
                 level, content, **kwargs):
        self.tag = 'h' + str(level)
        super().__init__(content, **kwargs)


class Meta(Br):
    """Add the meta element to the beginning of the head element"""
    tag = 'meta'
