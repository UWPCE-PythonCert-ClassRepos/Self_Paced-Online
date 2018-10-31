a = [2,3,4,5,6]
def mult(fact):
    return list(map(lambda x:x*fact,a))

print(mult(2))


ddonors = {"Manny Machado": [12.2,2.51,3.20],
            "Adam Jones": [1024.14,22.21,323.45],
            "Chris Davis": [3.2,5.55,4.20]}
fact = 2
donors2 = {}
for k,v in ddonors.items():
    donors2[k] = list(map(lambda x:x*fact,v))

print(donors2)