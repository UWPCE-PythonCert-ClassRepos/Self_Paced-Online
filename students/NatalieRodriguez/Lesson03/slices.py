#Lesson 03: Slices
#Natalie Rodriguez
#3/14/2018


#Test Sequences to Use
dog_list = ['Virgil', 'River', 'Kibson', 'Dexter', 'China', 'Lucy', 'Percy']
bird_list = ['Bluejay', 'Sparrow', 'House Finch', 'Cardinal', 'Nuthatch', 'Tufted Titmouse']
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#________________________________________________________________________
#Exchange the first item in the sequence with the last item in the sequence using slices.
def first_last_exchanged(dog_list):
    print("Original Sequence:",dog_list)
    dog_list[0], dog_list[-1] = dog_list[-1], dog_list[0]
    return dog_list

print(first_last_exchanged(dog_list))


#_______________________________________________________________________
#Print the sequence with every other item removed

def every_other_removed(dog_list):
    print("Original Sequence:", dog_list)
    del dog_list[1::2]
    return dog_list

print(every_other_removed(dog_list))

#________________________________________________________________________
#Remove the first 4 elements.
#Then remove the last 4 elements.
#Then remove every other item in between.

def part_three(number_list):
    print("Original Sequence:", number_list)
    return number_list[4:-4:2]

print(part_three(number_list))

#________________________________________________________________________
#Reverse the list.

def reverse_list(number_list):
    print("Original Sequence:", number_list)
    return number_list[::-1]

print(reverse_list(number_list))

#________________________________________________________________________
#middle third, last third, first third.

def thirds(bird_list):
    print("Original Sequence:", bird_list)
    bird_list[:2], bird_list[2:4], bird_list[4:] = bird_list[2:4], bird_list[4:], bird_list[:2]
    return bird_list

print(thirds(bird_list))

#________________________________________________________________________
#tests

#sequences
dog_list = ['Virgil', 'River', 'Kibson', 'Dexter', 'China', 'Lucy', 'Percy']
bird_list = ['Bluejay', 'Sparrow', 'House Finch', 'Cardinal', 'Nuthatch', 'Tufted Titmouse']
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


assert first_last_exchanged(dog_list) == ['Percy', 'River', 'Kibson', 'Dexter', 'China', 'Lucy', 'Virgil']
assert every_other_removed(dog_list) == ['Percy', 'Kibson', 'China', 'Virgil']
assert part_three(number_list) == [4, 6, 8, 10]
assert reverse_list(number_list) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
assert thirds(bird_list) == ['House Finch', 'Cardinal', 'Nuthatch', 'Tufted Titmouse', 'Bluejay', 'Sparrow']
