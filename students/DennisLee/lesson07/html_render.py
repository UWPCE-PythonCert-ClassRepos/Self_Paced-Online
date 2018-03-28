#!/usr/bin/env python3

import io

class Element():
	def __init__(self, content=None):
		self.contents = []
		if content:
			if isinstance(content, str):
				self.append(content)
			elif isinstance(content, list) or isinstance(content, tuple):
				for i in content:
					self.append(str(i))
	def append(self, in_str):
		# try:  # Remove leading/trailing whitespace & multi-whitespaces
			self.clean_str = ' '.join(in_str.split())
		# except AttributeError:
		# 	print(f"{in_str} is not a string - not added to element.")
		# else:
			self.contents.append(self.clean_str)
	def render(self, file_out, cur_ind=""):
		self.indent, f, result = 0, None, False
		if cur_ind:
			try:
				self.indent = int(cur_ind)
			except ValueError:
				print(
				  f"'{cur_ind}' is not a number - indent defaults to 2.")
		if self.indent <= 0:
			print(f"'{cur_ind}' is not a valid indent value - "
			      "indent defaults to 2.")
			self.indent = 2
		try:
			f = open(file_out, 'w')
		except FileNotFoundError:
			print(f"'{file_out}' cannot be accessed ... skipping.")
		except OSError:
			print(f"'{file_out}' is an invalid handle ... skipping.")
		else:
			f.write('<html>\n')
			f.write(' ' * self.indent)
			for i in self.contents:
				f.write(i + ' ')
			f.write('\n</html>\n')
		finally:
			if f:
				f.close()
				result = True
			return result


def render_page(element, file_name):
	pass
	