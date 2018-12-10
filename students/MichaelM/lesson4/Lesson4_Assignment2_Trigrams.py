"""
wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson4
git add Lesson4_Assignment2_Trigrams.py
git add trigrams.py
git commit Lesson4_Assignment2_Trigrams.py
git commit trigrams.py
git push
goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson4/
click Pull request > new pull request
"""


from Lesson04 import trigrams
import importlib
importlib.reload(trigrams)

if __name__ == "__main__":
    #trigrams.create_trigram(r"C:\Users\geekw\Dropbox\UW_Python\Assignments\Lesson04\tmp\trigram_text.txt")
    trigrams.create_trigram(r"https://uwpce-pythoncert.github.io/PythonCertDevel/_downloads/sherlock_small.txt")

