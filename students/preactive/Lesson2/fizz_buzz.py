for i in range(1, 101):
    current_print = str(i)
    if i % 3 == 0:
        current_print = current_print.replace(str(i), "")
        current_print += "fizz"
    if i % 5 == 0:
        current_print = current_print.replace(str(i), "")
        current_print += "buzz"
    print(current_print)
