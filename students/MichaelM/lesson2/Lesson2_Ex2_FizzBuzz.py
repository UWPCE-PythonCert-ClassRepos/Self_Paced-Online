# cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# run Lesson2_Ex2_FizzBuzz.py
# git status
# git add Lesson2_Ex2_FizzBuzz.py
# git commit
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students
# click Pull request > new pull request
# import name_main
# run Lesson2_Ex1.py
# from Natasha: python uses snake_case convention for var names (and functions)> horizontal_line

def buzzles_and_fizzles(top_pot):
        for i in range(top_pot):
            if (i%3) == 0:
                print("Fizz")
            elif (i%5) == 0:
                print("Buzz")
            elif (i%5) == 0 & (i%3) == 0:
                print("FizzBuzz")
            else:
                print(i)

if __name__ == "__main__":
    buzzles_and_fizzles(101)
    print("Well, that was the last number...")



