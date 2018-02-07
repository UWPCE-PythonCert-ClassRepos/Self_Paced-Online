def grid_printer():
	for i in range(2):
		print("+", end = " ")
		print("- " * 4, end = "")
		print("+", end = " ")
		print("- " * 4, end = "")
		print("+")
		for i in range(4):
			for  i in range(2):
				print("|", end = " " * 9)
			print("|")
	print("+", end = " ")
	print("- " * 4, end = "")
	print("+", end = " ")
	print("- " * 4, end = "")
	print("+")