#!/usr/bin/env python3

# series 1
l3_list = ('Apples', 'Pears', 'Oranges', 'Peaches')
print(l3_list)

response = input("give me a fruit to add to the end of the list> ")

l3_response = (response,)
l3_list = l3_list + l3_response
print(l3_list)

response_n = input("give me a number 1 through 5> ")
print(response_n, l3_list[int(response_n)-1])


l3_list = ('Mango',) + l3_list
print(l3_list)


l3_list = list(l3_list)
l3_list.insert(0, 'Lychee')
l3_list = tuple(l3_list)
print (l3_list)

for li in l3_list:
    if li.startswith('P'):
        print(li)

# series 2
print (l3_list)
# remove last fruit from list
l3_list = l3_list[:-1]
print(l3_list)

response2 = input("give me a fruit to delete from the list> ")

l3_list = list(l3_list)
# need error handling for this will throw valueError exception
l3_list.remove(response2)
# keep as list for next section
#l3_list = tuple(l3_list)

print(l3_list)

# series 3
for li2 in l3_list:
    li2_lower = li2.lower()
    response3 = input(f"do you like {li2_lower} ?>")
    while ((response3 != 'yes') and  (response3 != 'no')):
        response3 = input('you must answer yes or no>')
    if response3 == 'no':
        #print(li2)
        l3_list.remove(li2)

    elif response3 == 'yes':
        #do nothing
        continue

print(l3_list)

# series 4

l4_list = []
for li3 in l3_list:
    l4_list.append(li3[::-1])

l4_list = l4_list[:-1]
print(l3_list)
print(l4_list)



