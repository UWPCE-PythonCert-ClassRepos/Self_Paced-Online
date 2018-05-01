#!/usr/bin/env python3

import io

class Element():
	indent = ""
	def __init__(self, content=None, **kwargs):
		self.contents, self.attributes = [], {}
		self.append(content)
		for k, v in kwargs.items():
			if isinstance(v, str):
				self.attributes[k] = ' '.join(v.split())
			else:
				raise TypeError(
						f"Attribute {k} value is {v}, which is not a string.")
		self.attribute_string = self.convert_attrs_to_str()
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
		self.verify_render_args(file_out, cur_ind)
		if not self.indent:
			self.indent, cur_ind = cur_ind, ""
		child_ind = cur_ind + self.indent
		file_out.write(
				cur_ind + '<{0}{1}>\n'.format(self.tag, self.attribute_string))
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
		return True
	
	def verify_render_args(self, file_out, cur_ind):
		if not file_out:
			raise ValueError("Nothing specified in the 'file_out' argument.")
		elif not isinstance(cur_ind, str):
			raise TypeError("The 'cur_ind' argument must be a string.")
		elif cur_ind.strip(' '):
			raise ValueError(
					"The 'cur_ind' argument must contain spaces only.")
		elif file_out.write(''):
			raise AttributeError("Writable file-like "
					"object not given in the 'file_out' argument.")

	def convert_attrs_to_str(self):
		return ''.join(f' {k}="{v}"' for k, v in self.attributes.items())
		

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
		self.verify_render_args(file_out, cur_ind)
		if not self.indent:
			self.indent, cur_ind = cur_ind, ""
		for i in range(len(self.contents)):
			item = self.contents[i]
			if not isinstance(item, str):
				raise TypeError(
						f"Element content item #{i} '{item}' is a "
						f"{type(item)}; it must be a string "
						f"since {self.tag} is a one-line element.")
		file_out.write(cur_ind + '<{0}{1}>{2}</{0}>\n'.format(
				self.tag, self.attribute_string, ' '.join(self.contents)))
		return True

class Title(OneLineTag):
	tag = "title"

class SelfClosingTag(Element):
	def append(self, content):
		if content is not None:
			raise TypeError(f"Cannot add content '{content}' "
					f"of type '{type(content)}' to element '{self.tag}', "
					"because the element is a self-closing tag.")
	def render(self, file_out, cur_ind=""):
		self.verify_render_args(file_out, cur_ind)
		if not self.indent:
			self.indent, cur_ind = cur_ind, ""
		file_out.write(cur_ind + '<{0}{1} />\n'.format(
				self.tag, self.attribute_string))
		return True

class Hr(SelfClosingTag):
	tag = "hr"

class Br(SelfClosingTag):
	tag = "br"

class A(OneLineTag):
	def __init__(self, link, content):
		self.contents, self.attributes, self.tag = [], {}, "a"
		if not isinstance(link, str):
			raise TypeError(f"'{link}' is the wrong type - the 'link' "
					"argument must be a string.")
		self.attributes['href'] = link.strip()
		self.append(content)
		self.attribute_string = self.convert_attrs_to_str()