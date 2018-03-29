#!/usr/bin/env python3

import react as r
import unittest.mock

def test_react_correct():
    # mock.patch('builtins.input', side_effect=[...]) as mock_input:
    # with mock.patch.object(__builtin__, 'input', lambda: 'some_input'):
    # with mock.patch.object(__builtin__, 'input', lambda: 'yes'):
    with unittest.mock.patch('builtins.input') as mock_input:
        # assert module.function() == 'expected_output'
        # mock_input.return_value = 'yes'       # OK
        # assert r.react_correct() == 'JAAA'    # OK
        # assert r.react_correct() == None

        mock_input.return_value = 'no'
        assert r.react_correct() == 'NOOO'
