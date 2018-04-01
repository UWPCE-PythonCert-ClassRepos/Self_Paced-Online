#!/usr/bin/env python3

import io

class Element():
	tag = ""
	def __init__(self, content=None):
		self.contents = []
		if content and (isinstance(content, str)
			         or isinstance(content, Element)):
			self.append(content)
		else:
			print("Content not added - must specify a string or an element.")
	def append(self, in_str):
		try:  # Remove leading/trailing whitespace & multi-whitespaces
			self.clean_str = ' '.join(in_str.split())
		except AttributeError:
			print(f"{in_str} is not a string - not added to element.")
		else:
			self.contents.append(self.clean_str)
	def render(self, file_out, cur_ind=""):
		self.indent, result = 0, False
		self.indent = len(cur_ind)
		if file_out:
			try:
				file_out.write('<{0}>\n'.format(self.tag))
			except AttributeError:
				print(f"\n\tWritable file-like object not given - aborting.\n")
			else:
				file_out.write(' ' * self.indent)
				for i in self.contents:
					if isinstance(i, str):
						file_out.write(i + ' ')
					elif isinstance(i, Element):
						i.render(file_out, cur_ind)
				file_out.write('\n</{0}>\n'.format(self.tag))
				result = True
		return result
