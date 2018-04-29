"""renders some simple HTML code"""

#content=None is supposed to be the 'initializer signature'
class Element():

	def __init__(self):
		self.content = list()
	
	def append(self, some_string):
		self.content.append(some_string)
		
	def render():
		pass
