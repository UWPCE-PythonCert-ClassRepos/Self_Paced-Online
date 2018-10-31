'''
Shin Tran
Python 210
Assignment 8
'''

#!/usr/bin/env python3
# Implementing a sparse array class


# Takes in a list as an initializer
class sparse_array(list):

    def __init__(self, list_contents = None):
        if list_contents != None:
            self.content_list = list_contents
        else:
            self.content_list = []


    # Prints the array
    def print_list(self):
        print(self.content_list)


    # Returns the length of the array, including the zeros
    def get_length(self):
        return len(self.content_list)


    # Sets the element based on the index
    # Raises an index error if it's greater than the length
    def set_index(self, index, value):
        try:
            if value != 0:
                self.content_list[index] = value
            else:
                print("Can't store a 0 as a value.")
        except IndexError:
            print("Index out of bounds error, index can't be set.")


    # Gets the element based on the index
    # Returns a 0 if the index doesn't exist
    def get_index(self, index):
        try:
            return self.content_list[index]
        except IndexError:
            print("Index out of bounds error, index can't be retrieved.")
            return 0


    # Deletes the element by index
    # Returns the value of the deleted index
    def delete_index(self, index):
        try:
            ret_value = self.content_list[index]
            new_list1 = self.content_list[0:index]
            new_list2 = self.content_list[index+1:]
            self.content_list = new_list1 + new_list2
            return ret_value
        except IndexError:
            print("Index out of bounds error, index can't be deleted.")


    # Adds an element to the end of the array
    def append_value(self, value):
        self.content_list.append(value)


    # Slices the array based on the parameters passed in
    # includes the zeros
    def full_slice_array(self, start, end, step=1):
        new_list = self.content_list[:]
        new_list = new_list[start:end:step]
        return new_list


    # Slices the array based on the parameters passed in
    # excludes the zeros
    def core_slice_array(self, start, end, step=1):
        new_list = []
        for i in self.content_list:
            if i != 0:
                new_list.append(i)
        new_list = new_list[start:end:step]
        return new_list


if __name__ == '__main__':
    
    my_list1 = sparse_array([1,0,0,0,2,0,0,0,5])
    print("Print the list:")
    my_list1.print_list()
    print("Length is: {}".format(my_list1.get_length()))
    print()
    
    print("Get the indexes of the array")
    print(my_list1.get_index(0))
    print(my_list1.get_index(4))
    print(my_list1.get_index(8))
    print(my_list1.get_index(12))
    print()

    print("Set the indexes of the array")
    my_list1.set_index(3, 2)
    my_list1.set_index(5, 4)
    my_list1.set_index(8, 0)
    my_list1.set_index(15, 6)
    my_list1.print_list()
    print()

    print("Added a 9 at the end")
    my_list1.append_value(9)
    my_list1.print_list()
    print()

    print("Slices only non zero values of the array")
    print(my_list1.core_slice_array(0,6))
    print(my_list1.core_slice_array(0,6,2))
    print()
    
    print("New list")
    my_list2 = sparse_array([0,1,2,3,4,5,6,7,8,9])
    my_list2.print_list()
    print("Delete an this value from the list {}".format(my_list2.delete_index(4)))
    print(my_list2.delete_index(14))
    my_list2.print_list()
    print()

    print("New list")
    my_list3 = sparse_array([0,1,2,3,4,5,6,7,8,9])
    my_list3.print_list()
    list_length = my_list3.get_length()
    print("Testing slicing the sparse array")
    print(my_list3.full_slice_array(0, int(list_length/2)))
    print(my_list3.full_slice_array(int(list_length/2), list_length))
    print(my_list3.full_slice_array(0, list_length, 2))
