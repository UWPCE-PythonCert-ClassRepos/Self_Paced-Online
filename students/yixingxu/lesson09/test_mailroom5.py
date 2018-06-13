from mailroom4 import **

def test_donation_history_initialization():
    donors_collection = donation_history_initialization()
    a_list = ['Anna', 'Bob', 'Chuck', 'David', 'Ethan']
    assert ( donors_collection.get_donors_names()== a_list ) is True

#
# print(donors_collection.get_donors_names())
#     print('Ethan' in donors_collection.get_donors_names())
#
#     for donor in donors_collection.donors:
#         print(donor.name)
#         print(donor.donations)
#
#     donors_collection.add_donation_amount('David', 50)
#     for donor in donors_collection.donors:
#         print(donor.name)
#         print(donor.donations)
#
#     print(donors_collection.create_summary())
#     donors_collection.create_a_report()
#
#     new_donor = Donor('New')
#     donors_collection.add_new_donor(new_donor)
#     for donor in donors_collection.donors:
#         print(donor.name)
#         print(donor.donations)
#     donors_collection.add_donation_amount('New', 40)
#     for donor in donors_collection.donors:
#         print(donor.name)
#         print(donor.donations)
#     print(donors_collection.get_donors_names())
#
#     send_a_thank_you(donors_collection)
#     for donor in donors_collection.donors:
#         print(donor.name)
#         print(donor.donations)
#
#     send_letters_to_everyone(donors_collection.create_summary())