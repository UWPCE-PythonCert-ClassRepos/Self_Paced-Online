donors = [
  ["Alice", 20],
  ["Bob", 100],
  ["Charles", 30, 50, 10],
  ["Denise", 10, 5],
  ["Edward", 25, 20, 20, 20, 10],
  ]

def usein():
  action = input("Choose one of three actions: \n 1. Send a Thank You \n 2. Create a Report \n 3. Quit \n>")
  while (action.lower() not in ["1", "2", "3", "send a thank you", "create a report", "quit"]):
    action = input("Choose one of three actions: \n 1. Send a Thank You \n 2. Create a Report \n 3. Quit \n")
  if action.lower() in ['1', 'send a thank you']:
    sendty()
    usein()
  if action.lower() in ['2', 'create a report']:
    report()
    usein()
  if action.lower() in ['3', 'quit']:
    return
 

def sendty():
  donor = input("Enter a donor name or input 'List' for a list of donors\n>")
  if donor.lower() == "list":
    for names in donors:
        print(names[0])
  else:
    donation = input(("Enter a donation amount for {} \n>").format(donor))
    for names in donors:
      if donor == names[0]:
        names.append(int(donation))
        break
    else:
      donors.append([donor, int(donation)])
    print(("Thank you {} for your donation of ${:.2f}").format(donor, int(donation)))
  

def report():
  print("Donor Name           | Total Given   | Num Gifts     | Average Gift  |\n" + "-"*70)
  for rep in donors[0:]:
    total = sum(rep[1:])
    num = len(rep[1:])
    print("|{:<20}|{:>15.2f}|{:>15}|{:>15.2f}|".format(rep[0], total, num, total/num))

if __name__ == '__main__':
  usein()
