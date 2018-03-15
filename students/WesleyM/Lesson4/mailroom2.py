donors = [
  {'name': 'Alice Adams Ron', 'donation': [20]} ,
  {'name': 'Bob Be-Lake', 'donation': [100]},
  {'name': 'Charles Cruz', 'donation': [30, 50, 10]},
  {'name': 'Denise Dnice', 'donation': [10, 5]},
  {'name': 'Edward Eduardo', 'donation': [25, 20, 20, 20, 10]}
  ]
 

def send_ty():
  donor = input("Enter a donor name or input 'List' for a list of donors\n>")
  if donor.lower() == "list":
    for names in donors:
        print(names['name'])
    use_input()
  else:
    donation = float(input(("Enter a donation amount for {} \n>").format(donor)))
    for names in donors:
      if donor == names['name']:
        names['donation'].append(donation)
        break
    else:
      donors.append({'name': donor, 'donation': [donation]})
    print("Thank you {} for your donation of ${:.2f}".format(donor, donation))
  use_input()
  
def letters():
  for name in donors:
    print('Printing Letter to {a}'.format(a = name['name']))
    f = open('{a}.txt'.format(a = name['name']), 'w')
    f.write('Dear Ms./Mrs./Mr./Dr. {x}, \n We are thankful for your donation of ${y}. Your donation will be used for (insert harmful activity here). We hope you donate again soon!'.format(x = name['name'], y = sum(name['donation'])))
    f.close()
  use_input()

def report():
  print("Donor Name           | Total Given   | Num Gifts     | Average Gift  |\n" + "-"*70)
  for rep in donors:
    total = sum(rep['donation'])
    num = len(rep['donation'])
    print("|{:<20}|{:>15.2f}|{:>15}|{:>15.2f}|".format(rep['name'], total, num, total/num))
  use_input()

choices = {1: send_ty, 2: report, 3: letters}

def use_input():
  action = int(input("Choose one of four actions: \n 1. Send a Thank You \n 2. Create a Report \n 3. Send Letter to Everyone \n 4. Quit \n>"))
  while (action not in [1, 2, 3, 4]):
    action = input("Choose one of four actions: \n 1. Send a Thank You \n 2. Create a Report \n 3. Send Letter to Everyone 4. Quit \n>")
  if action in [1, 2, 3]:
    choices[action]()
  elif action == 4:
    return

if __name__ == '__main__':
    use_input()
