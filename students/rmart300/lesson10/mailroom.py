from datetime import date
from donor_collection import DonorCollection
from donor import Donor

dc = {}

def validate_user_selection(action, action_dict):
    """ validate the user selection versus available actions """

    key_list = list(action_dict.keys())
    try:
        if int(action) not in key_list:
            return False
        else:
            return True
    except ValueError as e:
        return False

if __name__ == '__main__':

    example_list = [Donor('Fred Smith'), Donor('Terrie Ann'), Donor('Murray Martin'), Donor('Josh Jones'), Donor('Jane Doe')]
    dc = DonorCollection(example_list)
    # prompt user for action and then call function
    action = 0
    while not isinstance(action,int) or int(action) != 4:
        prompt_message = 'What would you like to do: '
        prompt_message += '1 - \“Send a Thank You\” or '
        prompt_message += '2 - \“Create a Report\” or '
        prompt_message += '3 - \"Send letters to everyone\" or '
        prompt_message += '4 - \"Donation Challenge\" or 5 - \“quit\”\n'
        action = input(prompt_message)
       
        action_dict = { 1: dc.send_thank_you, 2: dc.create_report, 3: dc.write_letters, 4: dc.donation_challenge, 5: exit }
 
        if not validate_user_selection(action, action_dict):
            key_list = list(action_dict.keys())
            print("please enter a number {0}-{1}".format(key_list[0],key_list[-1]))
        else:
            action_dict[int(action)]()
            
