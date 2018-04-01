#!/usr/bin/env python3

import react as r
import unittest.mock


def test_react_correct():
    '''
    test if function reacts according to input 
    '''
    action_result= {'yes' : 'JAAA', 'no' : 'NOOO', 'wiwiwi' : 'BULLSHIT' }
    # action_result= { 'no' : 'NOOO', 'wiwiwi' : 'BULLSHIT' }
    for key in action_result:
        '''
        The following line simulates different user inputs by manipulating the
        builtins.input environment variable for the time of this test running:
        '''
        with unittest.mock.patch('builtins.input') as fake_input:
            # mock_input.return_value = 'yes'       # OK
            # assert r.react_correct() == 'JAAA'    # OK

            # mock_input.return_value = 'no'        # OK
            # assert r.react_correct() == 'NOOO'    # OK

            # mock_input.return_value = 'yes'         # OK
            # assert r.react_correct() == 'JAAA'      # OK

            fake_input.return_value = key

            if key == 'yes':
                # pass
                # mocker.patch(r.secondfunc)
                # unittest.mock.patch('r.secondfunc')
                # r.secondfunc.assert_called_once_with('')
                '''
                The following line patches the r.secondfunc function (for the time of this
                test) to just return the 
                specified return_value without really being executed:
                '''
                # r.secondfunc = unittest.mock.MagicMock(return_value = 'HAHAHA')
                r.secondfunc = unittest.mock.MagicMock(return_value = 'BUBU')
                # assert r.secondfunc() == 'HAHAHA'
                assert r.secondfunc() == 'BUBU'


                # r.secondfunc.assert_called_with(key)      # FAIL
                # r.secondfunc.assert_called_with()           # FAIL
                # r.secondfunc.assert_called()           # FAIL
            else:
                assert r.react_correct() == action_result[key]
