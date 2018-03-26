#!/usr/bin/env python3

class Element(object):
	indent, contents = None, []
	def __init__(self, content=None): pass
	def append(self, string): pass
	def render(self, file_out, cur_ind=""): pass

def render_page(element, file_name): pass
	