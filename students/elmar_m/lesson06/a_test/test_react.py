#!/usr/bin/env python3

import react as r
import unittest.mock


def test_react_correct():
    '''
    test if function reacts according to input 
    '''
    action_result= {'yes' : 'BUBU', 'no' : 'NOOO', 'wiwiwi' : 'BULLSHIT' }
    # action_result= {'yes' : 'HAHAHA', 'no' : 'NOOO', 'wiwiwi' : 'BULLSHIT' }
    for key in action_result:
        '''
        The following line simulates different user inputs by manipulating the
        builtins.input environment variable for the time of this test running:
        '''
        with unittest.mock.patch('builtins.input') as fake_input:
            fake_input.return_value = key
            if key == 'yes':
                '''
                The following line patches the r.secondfunc function (for the time of this
                test) to just return the specified return_value without really being executed.
                If a function is patched in that way here, it is NOT really executed when
                the test is run. 
                '''
                r.secondfunc = unittest.mock.MagicMock(return_value = 'BUBU')     # good one
                assert r.react_correct() == action_result[key]
            else:
                assert r.react_correct() == action_result[key]
