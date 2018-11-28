# fizzbuzz - loop through 1 to 100, if # dvisible by 3 print fizz, if divisible by 5 print buzz if both, print fizzbuzz

# iterate from 1 - 100
for x in range(1, 101):
	# test if value is divisible by 3 and 5 with no remainder
	if x % 3 == 0 and x % 5 == 0:
		print("fizzbuzz")
	# else if value is divisible by 3
	elif x % 3 == 0:
		print("fizz")
	# else if value is divisible by 5
	elif x % 5 == 0:
		print("buzz")
	# else print value
	else:
		print(x)
# end

	