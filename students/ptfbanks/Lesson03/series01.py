print ("This curious little routine plays games with strings and tuples, by parsing and splicing them in alernate ways.")
print ("A string refers to an ordered sequence of characters; like a sentence.")
print ("A tupple is an ordered sequence of entries (script limits 20 entries) delimited by commas.")
print ("Words and variables may also be included as tupple elements when appropriate.")
Sequence = []  #iniitalise sequence "Entry" Print ()
print ()
print ("Please enter a text string, or a series of tuple entry elements.")
for i in range (20):
    Add_entry = input("Enter string text or entry for tuple element Number.  (Enter END to stop) ")
    if Add_entry == "END":
        break
    Sequence.append(Add_entry)
print ("Thank you.  The sequence entered is recorded as:")

if i ==1:
    Sequence = f"{Sequence}"
    Sequence = Sequence [2:-2]
    print(Sequence)
    print(" this will be handled as a String.")
else:
    print(Sequence)
    print(" this will be handled as a Tuple.")
print()

def swap_fl(content):
    return content[-1:] + content[1:-1] + content[:1]


def alternate(content):
    return content[::2]


def fst4_lst4swap_alt_rest(content):
    if len(content)<11:
        print("This will look strange, a minimum of 11 entries is required for it to work properly")
        print("Try again if you like.")
    return content[-4:] + content[4:-4:2] + content[:4]


def revrs_by_slice(content):
    return content[::-1]


def mid_lst_fst_3rd(content):
    n=len(content)
    trd=n//3
    return content[(trd):] + content[:trd]

print("Play step one: Exchange first and last entry..... ")
print("result: ", swap_fl(Sequence))
print ()
print("Play step two: Return very other entry..... ")
print("result: ", alternate(Sequence))
print ()
print("Play step three: Exchange first four and last four entries,and alternate the center..... ")
print("result: ", fst4_lst4swap_alt_rest(Sequence))
print ()
print("Play step one: Reverse the whole series of entries..... ")
print("result: ", revrs_by_slice(Sequence))
print ()
print("Play step one: Divide into thirds, return middle, last, first third set of entries..... ")
print("result: ", mid_lst_fst_3rd(Sequence))


# assertion tests--------------------------------------
assert swap_fl(1, 2, 3, 4) == [4, 2, 3, 1]
assert swap_fl(abcdefg) == gbcdefa
assert alternate(1, 2, 3, 4) == [2, 4]
assert alternate(abcdefg) == aceg
assert fst4_lst4swap_alt_rest(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) == [9, 10, 11, 12, 5, 6, 7, 8, 1, 2, 3, 4]
assert fst4_lst4swap_alt_rest(abcdefghijkl) == ijklefghabcd
assert revrs_by_slice(1, 2, 3, 4) == [4, 3, 2, 1]
assert revrs_by_slice(abcdefg) == gfedcba
assert mid_lst_fst_3rd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) == [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]
assert mid_lst_fst_3rd(abcdefghijkl) == efghijklabcde
