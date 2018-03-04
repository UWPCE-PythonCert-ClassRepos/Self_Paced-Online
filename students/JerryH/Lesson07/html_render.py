#!/usr/bin/env python

class Element(object):

    tag = "html"
    indent = "  "


    def __init__(self, content=None):
        self.content = [content] if content else []

    def append(self, words):
        self.content.append(words)

'''
el = Element("First content here")
print(el.content)
el.append("second sentence")
print(el.content)
'''
