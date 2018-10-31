# cd C:\Users\Administrator\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# git status
# git add Lesson2_Ex1.py
# git commit
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students
# click Pull request > new pull request
# import name_main
# run Lesson2_Ex1.py

def horizontalLine(rows):
    print('+' + '-' * rows + '+' + '-' * rows + '+')
def vertSpacer(cols, rows):
    print((('|' + (' ' * rows)) * cols + '\n') * rows, end='')
def box(cols, rows):
    horizontalLine(rows)
    vertSpacer(cols, rows)
    horizontalLine(rows)
  

if __name__ == "__main__":
    box(3, 10)

  
