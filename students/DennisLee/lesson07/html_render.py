#!/usr/bin/env python3

import io

class Element():
	tag, indent = "", ""
	def __init__(self, content=None):
		self.contents = []
		if content is not None:
			self.append(content)
	def append(self, content):
		if isinstance(content, Element) and len(content.strip()):
			self.contents.append(content)
		elif isinstance(content, str):
			self.clean_str = ' '.join(content.split())
			self.contents.append(self.clean_str)
		elif isinstance(content, list) or isinstance(content, tuple):
			for i in content:
				self.append(i)
		else:
			print(f"{content} not added - must be string, element, "
			      "list, or tuple.")
	def render(self, file_out, cur_ind=""):
		result = False
		if file_out:
			try:
				file_out.write('<{0}>\n'.format(self.tag))
			except AttributeError:
				print(f"\n\tWritable file-like object not given - aborting.\n")
			else:
				child_ind = cur_ind + self.indent
				if not self.indent:
					self.indent = cur_ind
				for i in self.contents:
					if isinstance(i, str):
						file_out.write(child_ind + i + ' ')
					elif isinstance(i, Element):
						i.indent = self.indent
						i.render(file_out, child_ind)
				file_out.write(cur_ind + '\n</{0}>\n'.format(self.tag))
				result = True
		return result

class Html(Element):
	tag = "html"

class Body(Element):
	tag = "body"

class P(Element):
	tag = "p"