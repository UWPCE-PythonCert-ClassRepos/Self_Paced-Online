# fizzbuzz - loop through 1 to 100, if # dvisible by 3 print fizz, if divisible by 5 print buzz if both, print fizzbuzz

# iterate from 1 - 100
for x in range(1, 51):
	# test if value is divisible by 3 and 5 with no remainder
	if x % 3 == 0 or x % 5 == 0:
		print("fizzbuzz")
	# else if value is divisible by 3
	if x % 3 == "0":
		print("fizz")
	# else if value is divisible by 5
	if x % 5 == "0":
		print("buzz")
	# else print value
	else:
		print("falling through", x)
# end

	