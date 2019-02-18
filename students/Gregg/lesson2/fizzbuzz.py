def FizzBuzz(int_in):
    """Determine the FizzBuzziness of an input int and return the appropriate string"""
    #I already did the straightforward version on the programing test for this course
    #so I thought I would try something new, see if I could get only 1 if statement
    string = 'Fizz'*(not(int_in%3))+'Buzz'*(not(int_in%5))
    if not(string):
        string = str(int_in)
    return string


def FizzBuzz_iterate(end_int_in = 100):
    """Print the FizzBuzziness for positive numbers up to the input"""
    for i in range(end_int_in):
        print(FizzBuzz(i+1))


########
#Extra messing around with fizzbuzz#
########

def Fizzbuzz(int_in):
    """Determine the Fizzbuzziness of an input int and return the appropriate string
    I believe the original version required a lowercase b if both conditions were met
    which makes it a bit harder to do without multiple if statements
    Maybe its not the original but some modification I read about to make it more relevant"""
    b = 'B'*(bool(int_in%3))+'b'*(not(int_in%3))
    string = 'Fizz'*(not(int_in%3))+(b+'uzz')*(not(int_in%5))
    return(string+(not(string))*str(int_in))

def Fizzbuzz100_OneLine(end_int_in = 100):
    """Print the fizzbuzziness of 1-100 with one line of code
    including the loop in the single line? not sure about this
    I know this is terrible practice but wanted to see if I could do it"""
    for line in [(('Fizz'*(not(num%3))+(('B'*(bool(num%3))+'b'*(not(num%3)))+'uzz')*(not(num%5))) or str(num)) for num in range(1,end_int_in+1)]: print(line)
    #Found more elegant way to do it on Micheal Gililands blog
    #using join that eliminates the second for loop
    #Still would need the modification for the lowercase b
    #Also, this use of or is nice, I didn't know it could return the non boolean input
    #print '\n'.join("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i) for i in range(1,101))
    return True

#Irrelevant change to test git commit, again

if __name__ == "__main__":
    print('Lesson 2: FizzBuzz exercise')
    FizzBuzz_iterate()
