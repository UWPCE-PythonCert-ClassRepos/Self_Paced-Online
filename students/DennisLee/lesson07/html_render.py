#!/usr/bin/env python3

class Element():
	def __init__(self, content=None):
		self.contents = []
		if content:
			if isinstance(content, str):
				self.append(str)
			elif isinstance(content, list) or isinstance(content, tuple):
				for i in content:
					self.append(str(i))
	def append(self, string):
		try:  # Remove leading/trailing whitespace & multi-whitespaces
			clean_str = ' '.join(string.split())
		except AttributeError:
			print(f"{string} is not a string - not added to element.")
		else:
			self.contents.append(clean_str)
	def render(self, file_out, cur_ind=""):
		pass

def render_page(element, file_name):
	pass
	