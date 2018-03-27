donors = {
  'Alice Adams Ron': [20] ,
  'Bob Be-Lake': [100],
  'Charles Cruz': [30, 50, 10],
  'Denise Dnice': [10, 5],
  'Edward Eduardo': [25, 20, 20, 20, 10]
  }
 

def send_ty():
  donor = input("Enter a donor name or input 'List' for a list of donors\n>")
  repeat = 0
  if donor.lower() == "list":
    for names in donors:
        print(names)
    use_input()
  else:
    while repeat == 0:
      donation = float(input("Enter a donation amount for {} \n>".format(donor)))
      for names, donations in donors.items():
        if donor == names:
          donors[names].append(donation)
          break
      else:
        donors[donor] = [donation]
      print("Thank you {} for your donation of ${:.2f}".format(donor, donation))
      repeat = input("Would you like to add another donation for {}? Type 'yes' or 'no' \n>".format(donor))
      if repeat.lower() == "no":
        repeat = 1
      elif repeat.lower() == "yes":
        repeat = 0
      else:
        repeat = input("Would you like to add another donation for {}? Type 'yes' or 'no' \n>".format(donor))
  use_input()
  
def letters():
  for name, donations in donors.items():
    print('Printing Letter to {a}'.format(a = name))
    f = open('{a}.txt'.format(a = name), 'w')
    f.write("""Dear Ms./Mrs./Mr./Dr. {x}, \n
              We are thankful for your donation of ${y}.
              Your donation will be used for (insert harmful activity here).
              We hope you donate again soon!""".format(x = name,
              y = sum(donations)))
    f.close()
  use_input()

def report():
  print("Donor Name           | Total Given   | Num Gifts     | Average Gift  |\n" + "-"*70)
  for name, donations in donors.items():
    total = sum(donations)
    num = len(donations)
    print("|{:<20}|{:>15.2f}|{:>15}|{:>15.2f}|".format(name, total, num, total/num))
  use_input()

def close_program():
  print('Closing Program')

choices = {1: send_ty, 2: report, 3: letters, 4: close_program}

def use_input():
  action = int(input("Choose one of four actions: \n 1. Send a Thank You \n 2. Create a Report \n 3. Send Letter to Everyone \n 4. Quit \n>"))
  while action not in choices:
    action = input("Choose one of four actions: \n 1. Send a Thank You \n 2. Create a Report \n 3. Send Letter to Everyone 4. Quit \n>")
  choices[action]()


if __name__ == '__main__':
    use_input()
