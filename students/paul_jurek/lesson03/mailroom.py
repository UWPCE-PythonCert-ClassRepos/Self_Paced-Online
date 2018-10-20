"""runs the command line app for the mailroom as part of lesson 3"""

# setup initial donor list
donors = {'Bill Gates': [100000, 5, 3000000],
          'Paul Allen': [10, 1000000],
          'Warren Buffet': [300000000],
          }

if __name__ == '__main__':
    user_input = input("Options:\n"
        '\tSend a Thank You\n'
        '\tCreate a Report\n'
        '\tquit\n'
        'Please input option: ')
