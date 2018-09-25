#!/usr/bin/env python3

class Element(object):
    tag = "html"
    indent = "    "
    def __init__(self,content=None):
        self.content = []
    
    def append(self, new_content):
        self.content.append(new_content)


