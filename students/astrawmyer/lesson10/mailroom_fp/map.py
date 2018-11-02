

ddonors = {"Manny Machado": [12.2,2.51,3.20],
            "Adam Jones": [1024.14,22.21,323.45],
            "Chris Davis": [3.2,5.55,4.20]}

def challenge(factor):
    """Function to multiply the donations by all donors by a factor"""
    donors_2 = {}
    for k,v in ddonors.items():
        donors_2[k] = list(map(lambda x:x*factor,v))
    return donors_2

def filter_donations(**kwargs):
    """
    Function creates a donor dict of only sonations above or below a specified value.

    Args:
        above: Use to get donations above parameter.
        below: Use to get donations below parameter.
    """

    donors_2 = {}
    if 'above' in kwargs:
        for k,v in ddonors.items():
            donors_2[k] = list(filter(lambda x: x>kwargs.get('above'),v))
    
    if 'below' in kwargs:
        for k,v in ddonors.items():
            donors_2[k] = list(filter(lambda x: x<kwargs.get('below'),v))
    return donors_2


#print(filter_donations(above=10))
#print(filter_donations(below=10))
#print(challenge(2))

#function output: total total dollar amount
#function input: amount to multiply by
#               selection to which donations
#will need to first filter to criteria
#then apply mapping
#then sum all donations remaining
#then return the total