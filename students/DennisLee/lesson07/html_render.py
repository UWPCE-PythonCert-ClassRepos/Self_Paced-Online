#!/usr/bin/env python3

import io

class Element():
	"""The base class for HTML elements."""
	indent = ""  # A string of spaces indicating how much to indent
	             # between each indentation level
	def __init__(self, content=None, **kwargs):
		"""
		Define an element by specifying its child content & attributes.

		:content:  The child content (string text and/or child `Element`
		    	   objects).  The default value is `None`.  You may 
				   specify multiple child objects by using a list or a
				   tuple.

		:kwargs:  A dict containing attribute names and their values.

		:return:  The initialized `Element` object.
		"""
		self.contents, self.attributes = [], {}
		self.append(content)
		for k, v in kwargs.items():  # Process the element attributes
			if isinstance(v, str):
				self.attributes[k] = ' '.join(v.split())
			else:
				raise TypeError(
						f"Attribute {k} value is {v}, which is not a string.")
		
		# Convert the attributes to the proper HTML string form
		self.attribute_string = self.convert_attrs_to_str()
	def append(self, content):
		"""
		Append additional child content to the element.

		:content:  The child content (string or `Element` object) to be
		           added to the end of the `contents` member list.  You
				   may specify a list or tuple containing multiple child
				   objects.

		:return:  `None`.
		"""
		if content is not None:
			if isinstance(content, Element):  # Add `Element` object
				self.contents.append(content)
			elif isinstance(content, str):  # Add normalized string
				if len(content.strip()) > 0:
					clean_str = ' '.join(content.split())
					self.contents.append(clean_str)
			elif isinstance(content, list) or isinstance(content, tuple):
				for i in content:  # Recurse for 2+ child objects
					self.append(i)
			else:
				raise TypeError(f"'{content}' not added, because "
						"the 'content' argument must be string, element, "
						"list, or tuple.")
	def render(self, file_out, cur_ind=""):
		"""
		Create (render) the `Element` object onto an HTML text object.

		:file_out:  A StringIO or FileIO object representing the output
		            stream to save the rendered HTML text to.

		:cur_ind:  A string of spaces specifying how much to indent
		           for this particular `Element` object.  The default is
				   to not indent at all.

		:return:  `True` if the method succeeds; otherwise, `None`.
		"""
		# Make sure arguments are passed correctly
		self.verify_render_args(file_out, cur_ind)

		# If `indent` member not currently defined, set it to the passed
		# indentation argument, and change the current indent level to 0
		if not self.indent:
			self.indent, cur_ind = cur_ind, ""
		if not self.tag:
			self.tag = "html"  # Default setting for step 1 in the run file
		child_ind = cur_ind + self.indent
		file_out.write(  # Open tag
				cur_ind + '<{0}{1}>\n'.format(self.tag, self.attribute_string))
		i, items = 0, len(self.contents)
		while i < items:
			start_index = i

			# Combine consecutive child strings into 1 normalized string
			while isinstance(self.contents[i], str):
				i += 1
				if i >= items:
					break
			if start_index < i:
				file_out.write(child_ind + 
						' '.join(self.contents[start_index:i]) + "\n")

			# Recurse using increased indentation to process a child
			# `Element` object
			if i < items and isinstance(self.contents[i], Element):
				self.contents[i].indent = self.indent
				self.contents[i].render(file_out, child_ind)
			i += 1
		file_out.write(cur_ind + '</{0}>\n'.format(self.tag)) # Close tag
		return True
	def verify_render_args(self, file_out, cur_ind):
		"""
		Make sure the indentation level is specified correctly and that
		the output object can be written to.

		:file_out:  A StringIO or FileIO object representing the output
		            stream to save the rendered HTML text to.

		:cur_ind:  The current indentation level, specified as a string
		           of spaces.

		:return:  `None` (if the method succeeds); otherwise, an
		          exception is raised.
		"""
		if not file_out:
			raise ValueError("Nothing specified in the 'file_out' argument.")
		elif not isinstance(cur_ind, str):
			raise TypeError("The 'cur_ind' argument must be a string.")
		elif cur_ind.strip(' '):
			raise ValueError(
					"The 'cur_ind' argument must contain spaces only.")
		elif not hasattr(file_out, 'write'):
			raise AttributeError("Writable file-like "
					"object not given in the 'file_out' argument.")
	def convert_attrs_to_str(self):
		"""Return the full HTML attribute text, preceded by a space."""
		return ''.join(f' {k}="{v}"' for k, v in self.attributes.items())

class OneLineTag(Element):
	"""
	The base class for HTML elements that may have child text but does
	not contain child elements.  These elements are "leaves" in an HTML
	content tree, so they can be rendered on just one line.
	"""
	def render(self, file_out, cur_ind=""):
		"""
		Create (render) a one-line tag object onto an HTML text object.

		:file_out:  A StringIO or FileIO object representing the output
		            stream to save the rendered HTML text to.

		:cur_ind:  A string of spaces specifying how much to indent
		           for this particular `OneLineTag` object.  The default
				   is to not indent at all.

		:return:  `True` if the method succeeds; otherwise, `None`.
		"""
		# Make sure arguments are passed correctly
		self.verify_render_args(file_out, cur_ind)

		# If `indent` member not currently defined, set it to the passed
		# indentation argument, and change the current indent level to 0
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
		
class SelfClosingTag(Element):
	"""
	The base class for HTML elements that contain neither child text nor
	child elements.  These elements do not need a separate closing tag,
	as you can just add a slash ("/") in the initial tag to indicate
	that it is self-contained.
	"""
	def append(self, content):
		"""
		Override the `append` method to make sure nothing can be added
		as child text or child elements.

		:content:  The child content (text, `Element` objects, or a list
		           or tuple containing text and/or `Element` objects)
				   that is proposed for addition.

		:return:  `None` if nothing was specified for addition;
		          otherwise, a `TypeError` exception is raised.
		"""
		if content is not None:
			raise TypeError(f"Cannot add content '{content}' "
					f"of type '{type(content)}' to element '{self.tag}', "
					"because the element is a self-closing tag.")
	def render(self, file_out, cur_ind=""):
		"""
		Create (render) a self-closing tag object onto an HTML text
		object.

		:file_out:  A StringIO or FileIO object representing the output
		            stream to save the rendered HTML text to.

		:cur_ind:  A string of spaces specifying how much to indent
		           for this particular `SelfClosingTag` object.  The
				   default is to not indent at all.

		:return:  `True` if the method succeeds; otherwise, `None`.
		"""
		# Make sure arguments are passed correctly
		self.verify_render_args(file_out, cur_ind)

		# If `indent` member not currently defined, set it to the passed
		# indentation argument, and change the current indent level to 0
		if not self.indent:
			self.indent, cur_ind = cur_ind, ""
		file_out.write(cur_ind + '<{0}{1} />\n'.format(
				self.tag, self.attribute_string))
		return True

class Html(Element):
	"""An `html` document element class."""
	tag = "html"
	def render(self, file_out, cur_ind=""):
		"""
		Create (render) the `Html` object onto an <html> text object,
		including its preceding DOCTYPE declaration.

		:file_out:  A StringIO or FileIO object representing the output
		            stream to save the rendered HTML text to.

		:cur_ind:  A string of spaces specifying how much to indent
		           for this particular `Element` object.  The default is
				   to not indent at all.

		:return:  `True` if the method succeeds; otherwise, `None`.
		"""
		# Make sure arguments are passed correctly
		self.verify_render_args(file_out, cur_ind)
		file_out.write("<!DOCTYPE html>\n")
		return Element.render(self, file_out, cur_ind)

class Head(Element):
	"""A `head` element class (child element of `html`)."""
	tag = "head"

class Meta(SelfClosingTag):
	"""
	A metadata (`meta`) self-closing element class (child of `head`).
	"""
	tag = "meta"

class Title(OneLineTag):
	"""A `title` one-line element class (child element of `head`)."""
	tag = "title"

class Body(Element):
	"""A `body` element class (child element of `html`)."""
	tag = "body"

class H(OneLineTag):
	"""A class for one-line heading elements (`h1`-`h6`) """
	def __init__(self, header_level, header_text, **kwargs):
		"""
		Define a header element by specifying its heading level, child 
		content, & attributes.

		:header_level:  The element's heading level (from 1 through 6).
		
		:header_text:  The heading text's content string.

		:kwargs:  A dict containing attribute names and their values.

		:return:  The initialized heading element object.
		"""
		if not isinstance(header_text, str):
			raise TypeError(f"The 'header_text' argument is '{header_text}' "
					f"(type '{type(header_text)}') - a string is required "
					"for this argument.")
		elif not isinstance(header_level, int):
			raise TypeError(f"Header level '{header_level}' is not valid - "
					"must specify an int.")
		elif header_level not in range(1, 7):
			raise ValueError(f"Header level '{header_level}' is out of range "
					"- must be between 1 and 6.")
		else:
			self.tag = "h" + str(header_level)
			OneLineTag.__init__(self, header_text, **kwargs)

class P(Element):
	"""A paragraph (`p`) element class."""
	tag = "p"

class Hr(SelfClosingTag):
	"""A horizontal rule/line (`hr`) self-closing element class."""
	tag = "hr"

class Br(SelfClosingTag):
	"""A line break (`br`) self-closing element class."""
	tag = "br"

class A(OneLineTag):
	"""An `a` one-line element class, representing hyperlinked text."""
	def __init__(self, link, content):
		"""
		Define the `a` element by specifying its hyperlinked text and
		the hyperlink target.

		:link:  The hyperlink target's URL.

		:content:  The child content (string text and/or child `Element`
		    	   objects).  The default value is `None`.  You may 
				   specify multiple child objects by using a list or a
				   tuple.

		:return:  The initialized `a` object.
		"""
		self.contents, self.attributes, self.tag = [], {}, "a"
		if not isinstance(link, str):
			raise TypeError(f"'{link}' is the wrong type - the 'link' "
					"argument must be a string.")
		self.attributes['href'] = link.strip()
		self.append(content)
		self.attribute_string = self.convert_attrs_to_str()

class Ul(Element):
	"""An unordered list (`ul`) element class."""
	tag = "ul"

class Li(Element):
	"""A list item (`li`) element class (child of `ul`)."""
	tag = "li"
