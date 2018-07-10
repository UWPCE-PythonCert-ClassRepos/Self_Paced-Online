#!/usr/bin/env python


class Element:
    tags = ["<html>", "</html>"]
    indents = "    "
    appends_called = 0

    def __init__(self, content=None):
        self.content = content
        if not self.content:
            self.content = "{}\n{}".format(*self.tags)

    def newline_insert(self, old_string, new_string, insertion_point=1):
        old_list = old_string.split('\n')
        position = insertion_point
        if position > 0:
            for i, elem in enumerate(old_list):
                if elem == self.tags[1]:
                    position = i
        new_list = new_string.split('\n')
        for i, elem in enumerate(new_list):
            new_elem = list(elem)
            new_elem.insert(0, self.indents)
            new_elem = ''.join(new_elem)
            old_list.insert(position + i, new_elem)
        self.content = '\n'.join(old_list)

    def append(self, string):
        self.appends_called += 1
        if string:
            self.newline_insert(self.content, string, self.appends_called)

    def render(self, file_out, cur_ind=""):  # The assignment calls for cur_ind, but I haven't found a use for it.
        file_out.write(self.content)

    def write():  # the assignment calls for a write() function, but aside from having render call write and moving the one line of code from render() to write(), I haven't found a use for it
        pass


class Html(Element):
    tags = ["<html>", "</html>"]

    def append(self, obj):
        self.appends_called += 1
        if obj:
            self.newline_insert(self.content, obj.content, self.appends_called)


class Body(Html):
    tags = ["<body>", "</body>"]

    def append(self, obj):
        self.appends_called += 1
        if type(obj) == str:
            self.no_line_insert(self.content, obj)
        elif type(obj) == "__main__.A":
            self.no_line_insert(self.content, obj.content)
        else:
            super().append(obj)

    def no_line_insert(self, old_string, new_string):
        old_list = old_string.split(self.tags[1])
        old_list.append(f"{self.indents}{new_string}\n{self.tags[1]}")
        self.content = ''.join(old_list)


class P(Element):
    tags = ["<p>", "</p>"]

    def __init__(self, content=None, style=None):
        if content:
            self.content = f"{self.tags[0]}\n    {content}\n{self.tags[1]}"
        else:
            self.content = "{}\n{}".format(*self.tags)

        if style:
            self.style = style
            self.style_insert(self.content, self.style, (len(self.tags[0]) - 1))

    def style_insert(self, old_string, new_string, insertion_point):
        old_list = list(old_string)
        position = insertion_point
        old_list.insert(position, f" style=\"{new_string}\"")
        self.content = ''.join(old_list)


class Li(P, Body):
    tags = ["<li>", "</li>"]

    def append(self, obj, style=None):
        if style:
            self.style = style
            self.style_insert(self.content, self.style, (len(self.tags[0]) - 1))
        super().append(obj)


class Ul(P, Body):
    tags = ["<ul>", "</ul>"]

    def __init__(self, id=None, style=None):
        self.content = "{}\n{}".format(*self.tags)
        if id:
            self.id = id
            self.id_insert(self.content, self.id, 3)

        if style:
            self.style = style
            self.style_insert(self.content, self.style, -7)

    def id_insert(self, old_string, new_string, insertion_point):
        old_list = list(old_string)
        position = insertion_point
        old_list.insert(position, f" id=\"{new_string}\"")
        self.content = ''.join(old_list)


class A(Element):
    tags = ["<a>", "</a>"]

    def __init__(self, link, text):
        self.content = f"<a href=\"{link}\">{text}</a>"


class H(Element):
    tags = ["<h>", "</h>"]

    def __init__(self, num, text):
        self.content = f"<h{num}>{text}</h{num}>"


class Head(Html):
    tags = ["<head>", "</head>"]


class Title(Body):
    tags = ["<title>", "</title>"]

    def __init__(self, content=None):
        if content:
            self.content = f"{self.tags[0]}{content}{self.tags[1]}"
        else:
            self.content = "{}\n{}".format(*self.tags)


class Meta(Element):
    tags = ["<meta />"]

    def __init__(self, charset=None, name=None, content=None):
        self.content = f"{self.tags[0]}"
        if charset:
            self.charset = charset
            self.meta_insert(self.content, self.charset, "charset", -3)

    def meta_insert(self, old_string, new_string, element, insertion_point):
        old_list = list(old_string)
        position = insertion_point
        old_list.insert(position, f" {element}=\"{new_string}\"")
        self.content = ''.join(old_list)


class Hr(Element):
    tags = ["<hr />"]

    def __init__(self):
        self.content = "{}".format(*self.tags)


