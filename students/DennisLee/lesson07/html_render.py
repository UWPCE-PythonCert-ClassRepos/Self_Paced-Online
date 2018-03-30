#!/usr/bin/env python3

import io

class Element():
	tag = ""
	def __init__(self, content=None):
		self.contents = []
		if content and isinstance(content, str):
			self.append(content)
		else:
			print("Content not added - must specify a string.")
	def append(self, in_str):
		try:  # Remove leading/trailing whitespace & multi-whitespaces
			self.clean_str = ' '.join(in_str.split())
		except AttributeError:
			print(f"{in_str} is not a string - not added to element.")
		else:
			self.contents.append(self.clean_str)
	def render(self, file_out, cur_ind=""):
		self.indent, result = 0, False
		if cur_ind:
			try:
				self.indent = int(cur_ind)
			except ValueError:
				print(
				  f"\n\t'{cur_ind}' is not a number - indent defaults to 2.\n")
		if self.indent <= 0:
			print(f"\n\t'{cur_ind}' is not a valid indent value - "
			      "indent defaults to 2.\n")
			self.indent = 2
		if file_out:
			try:
				file_out.write('<{0}>\n'.format(self.tag))
			except AttributeError:
				print(f"\n\tWritable file-like object not given - aborting.\n")
			else:
				file_out.write(' ' * self.indent)
				for i in self.contents:
					file_out.write(i + ' ')
				file_out.write('\n</{0}>\n'.format(self.tag))
				file_out.close()
				result = True
		return result


def render_page(element, file_name):
	pass
	