#!/usr/bin/env python3
def taskone():
    tuple = ( 2, 123.4567, 10000, 12345.67)
    print("file_{:05d}: {:0.2f} {:0.2E} {:0.2E}".format(tuple[0], tuple[1], tuple[2], tuple[3]))

def tasktwo():
    tuple = ( 2, 123.4567, 10000, 12345.67)
    print(f"file_{tuple[0]:05d}: {tuple[1]:0.2f} {tuple[3]:0.2E} {tuple[3]:0.2E}")

def taskthree():
    tuple = ( 2, 123.4567, 10000, 12345.67)
    print("The {:d} numbers are ".format(len(tuple)) + ", ".join(["{}"] * len(tuple)).format(*tuple))

def taskfour():
    tuple = ( 4, 30, 2017, 2, 27)
    tuple2 = (tuple[3],tuple[4],tuple[2],tuple[0],tuple[1])
    print(" ".join(["{:02d}"] * len(tuple2)).format(*tuple2))

def taskfive():
    muhList = ['oranges', 1.3, 'lemons', 1.1]
    print(f"The weight of an {muhList[0]} is {muhList[1]} and the weight of a {muhList[2]} is {muhList[3]}")
    print(f"The weight of an {muhList[0].upper()} is {muhList[1]*1.2} and the weight of a {muhList[2].upper()} is {muhList[3]*1.2}")

def tasksix():
    dataGrid = [["bob",20,1000],["donald",103,30],["greg",38,800],["Constantine",78,90000]]
    nameLen, ageLen, priceLen = [], [], []
    for row in dataGrid:
        nameLen.append(len(row[0]))
        ageLen.append(len(str(row[1])))
        priceLen.append(len(str(row[2])))
    print(len(dataGrid))
    for i in range(len(dataGrid)):
        print("| {:<{}} | {:<{}} | {:<{}} |".format(dataGrid[i][0], max(nameLen), dataGrid[i][1], max(ageLen), dataGrid[i][2], max(priceLen)))

if __name__ == "__main__":
    tasksix()
