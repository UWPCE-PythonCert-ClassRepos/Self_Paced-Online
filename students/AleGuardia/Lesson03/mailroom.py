#!/usr/bin/env python3

donations = [[['William Gates, III'], [1000000, 585000, 5750000]],
             [['Mark Zuckerberg'], [15000, 5000]],
             [['Jeff Bezos'], [3000000]],
             [['Paul Allen'], [25000,1000]],
             [['Elon Musk'], [30000,3499]]]


def return_average(seq):
    return sum(seq)/len(seq)


def return_count(seq):
    return len(seq)


def return_label():
    label ="{:18} | {:>12} | {:>9} | {:>12}\n".format('Donor Name','Total Given','Num Gifts','Average Gift')
    label += "-"*len(label)
    return label


def return_report(data):
    report = f"{return_label()}\n"
    for item in data:
        row = f"{item[0][0]:18} $ {'{sum(item[0]){:.2f}:>12}'}  {'{:>9d}'} $ {'{{:.2f}:>12}'}\n".format(*item[1])
        print(sum(item[1]))
        report += row
    return report

if __name__ == '__main__':
    print(len(donations))
    print(return_report(donations))


