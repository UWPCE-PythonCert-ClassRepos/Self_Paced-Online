#!/usr/bin/env python3


class Element():
    tag_name = 'html'
    indentation = 2

    def __init__(self, content):
        self.content = [] if content is None else [content]

    def append(self, new_content):
        self.content.append(new_content)
