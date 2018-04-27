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
				self.indent, cur_ind = cur_ind, ""
			child_ind = cur_ind + self.indent
			try:
				file_out.write(cur_ind + '<{0}>\n'.format(self.tag))
			except AttributeError:
				raise AttributeError("Writable file-like "
						"object not given in the 'file_out' argument.")
			else:
				i, items = 0, len(self.contents)
				while i < items:
					start_index = i
					while isinstance(self.contents[i], str):
						i += 1
						if i >= items:
							break
					if start_index < i:
						file_out.write(child_ind + 
								' '.join(self.contents[start_index:i]) + "\n")
					if i < items and isinstance(self.contents[i], Element):
						self.contents[i].indent = self.indent
						self.contents[i].render(file_out, child_ind)
					i += 1
				file_out.write(cur_ind + '</{0}>\n'.format(self.tag))
				
				result = True
		return result

class Html(Element):
	tag = "html"

class Body(Element):
	tag = "body"

class P(Element):
	tag = "p"

class Head(Element):
	tag = "head"

class OneLineTag(Element):
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
			for i in range(len(self.contents)):
				item = self.contents[i]
				if not isinstance(item, str):
					raise TypeError(
							f"Element content item #{i} '{item}' is a "
							f"{type(item)}; it must be a string "
							f"since {self.tag} is a one-line element.")
			try:
				file_out.write(cur_ind + '<{0}>{1}</{0}>\n'.format(
						self.tag, ' '.join(self.contents)))
			except AttributeError:
				raise AttributeError("Writable file-like "
						"object not given in the 'file_out' argument.")
			else:
				result = True
		return result

class Title(OneLineTag):
	tag = "title"