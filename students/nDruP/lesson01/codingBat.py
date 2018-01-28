#For any of the exercises that I'm having trouble w/

def last2(str):
  if len(str)<3:
    return 0
  findStr = str[len(str)-2:len(str)]
  print("findStr: "+findStr)
  count=0
  for x in range(-1,len(str)-2):
    print(str[x:x+2])
    if str[x:x+2] == findStr:
      count+=1
  return count


def string_match(a, b):
  count = 0
  for x in range(min(len(a)-1, len(b)-1)):
    if a[x:x+2]==b[x:x+2]:
        count+=1
  return count

def make_bricks(small, big, goal):
  goalM5 = goal%5
  if goalM5 > small:
    return False
  small -= goalM5
  goal-=goalM5
  if goal-(big*5)<=0:
    return True
  return (goal-(big*5)-small)<=0
  

print(make_bricks(7,1,8))
print(make_bricks(41,2,47))
