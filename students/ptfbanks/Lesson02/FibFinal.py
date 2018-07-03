# Final developmental design to select Fibonacci or Lucas Series member
#_____________________Program Setup___________________________________
t=str(input("I will calculate for you the Fibonacci or Lucas series of numbers.  Which series woiuld you lke? (Enter F, or L): "))
   # Prepare user with intoduction to programs function."""
   # user identifes which series type (t) to run.  limit is clarified to avoid run-away process
   
c=int(input("Which member of that series (eg.9th) would you like? Enter a positive number (max 20): "))
if c>20: #user selects a desired member of the series by number
   c=20  # limit is enforced to avoid run-away process
      
   #user selects a desired member (c) of the series by number
if c<0:    #All negative requests will revert to the Series origin - position 0.
   print("Clever.... ", (c), ". Series do not have negative position members. The orign starts at position 0, which is...") 
   c=0
#_____________________Program body___________________________________
def sum_series(f, s, n):
   """Calculate fibonacci/Lucal series values for a given membernumber in the series."""
   if n==1:
      return (f)
   if n==2:
      return (s)
   else:
      return sum_series(f,s,n-2) + sum_series(f,s,n-1)
      """Apply asserts as verification tests."""
   assert sum_series(2, 1, 6) == 18 #Entry of "L", and 6
   assert sum_series(0, 1, 5) == 5  #Entry of "F", and 5
         
if t=="F" or t=="f":
   print ("The number", (c), "member of the the Fibonacci serues is...", (sum_series (0, 1, c+1)))
elif t=="L"or t=="l":
   print ("The number", (c), "member of the the Lucas serues is...", (sum_series (2, 1, c+1)))
else:
   print("Entry Error...  Series", (t), "?" )
        
#-----------test validaton reference--------------------

# assertion test for fibonacci - Not applicable in this program version.
#assert fib(0) == 0
#assert fib(1) == 1
#assert fib(2) == 1
#assert fib(3) == 2

# assertion test for lucas  - Not applicable in this program version.
#assert lucas(0) == 2
#assert lucas(1) == 1
#assert lucas(2) == 3
#assert lucas(3) == 4

# assertion test for sum_series - relocated mid function above.
#assert sum_series(0, 1, 3) == 2 #Entry of "F", and 3
#assert sum_series(2, 1, 0) == 2 #Entry of "L", and 0
#assert sum_series(0, 1, 5) == 5 #Entry of "F", and 5
#assert sum_series(2, 1, 6) == 18 #Entry of "L", and 6