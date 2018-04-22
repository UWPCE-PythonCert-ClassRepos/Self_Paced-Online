#!/usr/bin/env python3


class Element():
    tag_name = 'html'
    indentation = 4

    def __init__(self, content=None):
        self.content = [] if content is None else [content]
        self.children = []

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, cur_ind=""):
        self.file_out = file_out
        self.cur_ind = cur_ind

        self.file_out.write(
            f"{self.cur_ind}<{self.tag_name}>\n"
            f"{self.cur_ind}{' ' * self.indentation}{' '.join(self.content)}\n"
            f"{self.cur_ind}</{self.tag_name}>"
        )
