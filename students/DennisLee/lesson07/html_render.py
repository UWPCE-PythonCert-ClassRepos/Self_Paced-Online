#!/usr/bin/env python3

import io

class Element():
	tag, indent = "", ""
	def __init__(self, content=None):
		self.contents = []
		self.append(content)
	def append(self, content):
		if content is not None:
			if isinstance(content, Element):
				self.contents.append(content)
			elif isinstance(content, str):
				if len(content.strip()) > 0:
					self.clean_str = ' '.join(content.split())
					self.contents.append(self.clean_str)
			elif isinstance(content, list) or isinstance(content, tuple):
				for i in content:
					self.append(i)
			else:
				raise TypeError(f"'{content}' not added, because "
						"the 'content' argument must be string, element, "
						"list, or tuple.")
	def render(self, file_out, cur_ind=""):
		result = False
		if not file_out:
			raise ValueError("Nothing specified in the 'file_out' argument.")
		elif not isinstance(cur_ind, str):
			raise TypeError("The 'cur_ind' argument must be a string.")
		elif cur_ind.strip(' '):
			raise ValueError(
					"The 'cur_ind' argument must contain spaces only.")
		else:
			if not self.indent:
				self.indent, cur_ind = cur_ind, self.indent
			child_ind = cur_ind + self.indent
			try:
				file_out.write(cur_ind + '<{0}>\n'.format(self.tag))
			except AttributeError:
				raise AttributeError("Writable file-like "
						"object not given in the 'file_out' argument.")
			else:  # REDO
				file_out.write(child_ind)
				for i in self.contents:
					if isinstance(i, str) and i.strip():
						file_out.write(i + ' ')
					elif isinstance(i, Element):
						i.indent = self.indent
						i.render(file_out, child_ind)
				file_out.write('\n' + cur_ind + '</{0}>\n'.format(self.tag))
				# i = 0
				# while i < len(self.contents):
				# 	start_index = i
				# 	while isinstance(i, str):
				# 		i += 1
				# 	if start_index < i:
				# 		file_out.write(child_ind + 
				# 				' '.join(self.contents[start_index:i]) + "\n")
				# 	if isinstance(i, Element):
				# 		i.indent = self.indent
				# 		i.render(file_out, child_ind)
				# 	i += 1
				# file_out.write(cur_ind + '</{0}>\n'.format(self.tag))
				result = True
		return result

class Html(Element):
	tag = "html"

class Body(Element):
	tag = "body"

class P(Element):
	tag = "p"