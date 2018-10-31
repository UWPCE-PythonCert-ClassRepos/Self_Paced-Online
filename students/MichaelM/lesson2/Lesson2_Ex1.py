# cd C:\Users\Administrator\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# import name_main
# run Lesson2_Ex1.py

def horizontalLine():
    print('+' + '-'*4 + '+' + '-'*4 + '+')
def vertSpacer(cols):
    print(('|' + '    ')*cols)
    print(('|' + '    ')*cols)
    print(('|' + '    ')*cols)
    print(('|' + '    ')*cols)

if __name__ == "__main__":
    horizontalLine()
    vertSpacer(3)
    horizontalLine()
    vertSpacer(3)
    horizontalLine()
