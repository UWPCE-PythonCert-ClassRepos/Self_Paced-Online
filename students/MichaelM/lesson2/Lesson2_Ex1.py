# cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# git status
# git add Lesson2_Ex1.py
# git commit
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students
# click Pull request > new pull request
# import name_main
# run Lesson2_Ex1.py

def horizontalLine(boxCnt):
    print((('+' + '- - - - -') * boxCnt ), end='+' + '\n')
def vertLine(boxCnt):
    cols = boxCnt + 1
    print(((('|' + '         ') * cols)+ '\n') * 4, end='') 
    
def box(boxCnt):
    for _ in range(boxCnt):
        horizontalLine(boxCnt)
        vertLine(boxCnt)
    horizontalLine(boxCnt)
  

if __name__ == "__main__":
    box(10)
    print("done...")
