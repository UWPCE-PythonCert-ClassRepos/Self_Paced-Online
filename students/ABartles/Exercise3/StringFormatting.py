#------------------Task 1------------------
print("------------------Task 1------------------")
tpl = ( 2, 123.4567, 10000, 12345.67)

num1 = tpl[0]
num2 = tpl[1]
num3 = tpl[2]
num4 = tpl[3]

s = "file_{:03}: {:.2f}, {:.2e}, {:.2e}".format(num1,num2,num3,num4)
print(s)

#------------------Task 2------------------
print("\n------------------Task 2------------------")
s2 = f"file_{num1:03}: {num2:.2f}, {num3:.2e}, {num4:.2e}"
print(s)

#------------------Task 3------------------
print("\n------------------Task 3------------------")

def formatter(tpl):
    count = len(tpl)
    lst = []
    for i in tpl:
        lst.append(str(i))
    s3 = ", ".join(lst)
    return f"The {count} items are: {s3}"

arbtpl = "Milk", 5, "Run", 32.5674

print(formatter(arbtpl))

#------------------Task 4------------------
print("\n------------------Task 4------------------")
tpl = ( 4, 30, 2017, 2, 27)
s4 = f'{tpl[3]:02} {tpl[4]:02} {tpl[2]} {tpl[0]:02} {tpl[1]:02}'
print(s4)

#------------------Task 5------------------
print("\n------------------Task 5------------------")
lst = ['oranges', 1.3, 'lemons', 1.1]
s = f'The weight of {lst[0].upper()} is {lst[1]*1.2}, and the weight of {lst[2].upper()} is {lst[3]*1.2}.'
print(s)

#------------------Task 6------------------
print("\n------------------Task 6------------------")
frst = "first"
fcost = 99.08
scnd = "second"
scost = 77.02

s = f'{frst:<10}{fcost:>10}   {scnd:<10}{scost:>10}'
print(s)

input()
