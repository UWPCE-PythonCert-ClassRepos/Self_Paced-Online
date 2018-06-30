def print_grid_basic():
	for j in range(2):	
		print('+' + ' - '*4 + '+' +  ' - '*4 + '+')
		for i in range(4):	
			print('|' + '   '*4 + '|' +  '   '*4 + '|')	
	print('+' + ' - '*4 + '+' +  ' - '*4 + '+')
	

def print_grid_one(x):
	y = int(x/2)
	for j in range(2):	
		print('+' + ' - '*y + '+' +  ' - '*y + '+')
		for i in range(y):	
			print('|' + '   '*y + '|' +  '   '*y + '|')	
	print('+' + ' - '*y + '+' +  ' - '*y + '+')

	
	
def print_grid_multi(x,y):
	for j in range(x):	
		for k in range(x):
			print('+' + ' - '*y , end=' ')
		print('+')
		for i in range(x):	
				print('|' + '   '*y , end=' ')
		print('|')
	for k in range(x):
		print('+' + ' - '*y , end=' ')
	print('+')