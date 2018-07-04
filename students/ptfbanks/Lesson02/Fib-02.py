# second developmental design to select Fibonacci and lucas Series

t=str(input("I will calculate for you the Fibonacci or Lucas series of numbers.  Which series woiuld you lke? (Enter F, or L): "))
   # Prepare user with intoduction to programs function."""
   # user identifes which series type to run.  limit is clarified to avoid run-away process
c=int(input("And Which member of that series (eg.9th) would you like? Please enter a positive number (max 20): "))
if c>20: #user selects a desired member of the series by number
   c=20  # limit is enforced to avoid run-away process
  
# but if null is entered... I Could not get this to work so commented it out
#if c=="": #A blank number requests will return the Series origin - position 0.
#   print("No number, I'll return the series orign, position 0, which is...")
#   c=0

if c<0:    #All negative requests will revert to the Series origin - position 0.
   print("Clever.... ", (c), ". Series do not have negative position members. The orign starts at position 0, which is...") 
   c=0   

   
def fib(n):
   if n<=1:
      return (n)
   else:
      return fib(n-2) + fib(n-1)
           
def lucas(n):
   if n==0:
      return 2
   elif n==1:
      return 1
   else:
      return lucas(n-2) + lucas(n-1)

if t=="F":
   print ("Fibonacci series number " , (c), "is the valeue ", fib(c))
elif t=="L":
   print ("Fibonacci series number " , (c), "is the valeue ", lucas(c))
else:
   print("Entry Error...  Series", (t), "?" )
        
#def sum_series(f, s, n):
   """This is the start of the third itteration."""
   