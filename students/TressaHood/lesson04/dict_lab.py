#!/usr/bin/env python3

# Activity 1 Dictionary and Set lab


def main():

    # Dictionaries 1
    # create a dictionary
    d = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    print(d)

    # remove last item
    d.pop("cake")
    print(d)

    # add new item
    d["fruit"] = "Mango"
    print(d)

    # display the keys
    print(d.keys())

    # display the values
    print(d.values())

    #
    if "cake" in d:
        print("There is cake, not deleted")
    else:
        print("There is no cake")

        #
    if "Mango" in d.values():
        print("There is a Mango, not deleted")
    else:
        print("There is no Mango")

    # Dictionaries 2
    d = {"name": None, "city": None, "cake": None}
    for item in d:
        d[item] = item.lower().count("t")

    print(d)

    # Sets 1
    # make sets
    s2 = set(range(0, 21, 2))
    s3 = set(range(0, 21, 3))
    s4 = set(range(0, 21, 4))
    print(s2)
    print(s3)
    print(s4)

    # subset?
    print(s3.issubset(s2))
    print(s4.issubset(s2))

    # Sets 2
    s = set()
    for i in "Python":
        s.update(i)

    # add 'i'
    s.update('i')
    print(s)

    # create a frozen set
    fs = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))
    print(s.union(fs))
    print(s.intersection(fs))


if __name__ == '__main__':
    main()
