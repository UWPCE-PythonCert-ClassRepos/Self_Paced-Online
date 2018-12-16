"""helper functions to assist with mailroom program"""

def menu_selection(prompt, dispatch_dict, **kwargs):
    """generic function to create command line menu and route response
    Will continue to ask user for response until valie response is given or
    user quits by entering 0 or quit.
    args:
        prompt: str to be displayed to user
        dispatch_dict: dict which routes user inputs
        **kwargs: allows for inputs to be passed to dict fuction
    """
    while True:
        response = input(prompt)
        if (response == '0') or (response.lower().strip() == 'quit'):
            break
        try:
            dispatch_dict.get(response)(**kwargs)
        except TypeError:
            print('Please enter valid option from list')