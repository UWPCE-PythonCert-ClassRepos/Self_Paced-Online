#!/usr/bin/env python3

import react as r
import unittest.mock

def test_react_correct():
    '''
    test if function reacts according to input 
    '''
    action_result= {'yes' : 'JAAA', 'no' : 'NOOO', 'wiwiwi' : 'BULLSHIT' }
    for key in action_result:
        with unittest.mock.patch('builtins.input') as fake_input:
            # mock_input.return_value = 'yes'       # OK
            # assert r.react_correct() == 'JAAA'    # OK

            # mock_input.return_value = 'no'        # OK
            # assert r.react_correct() == 'NOOO'    # OK

            # mock_input.return_value = 'yes'         # OK
            # assert r.react_correct() == 'JAAA'      # OK

            fake_input.return_value = key
            assert r.react_correct() == action_result[key]
