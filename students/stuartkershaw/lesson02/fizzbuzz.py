counter = 1
limit = 100

while counter <= limit:
    if counter % 3 == 0 and counter % 5 == 0:
        print('fizzbuzz')
    elif counter % 3 == 0:
        print('fizz')
    elif counter % 5 == 0:
        print('buzz')
    else:
        print('{}'.format(counter))
    counter += 1
