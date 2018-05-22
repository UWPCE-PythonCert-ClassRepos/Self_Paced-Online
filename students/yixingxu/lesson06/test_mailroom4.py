#!/usr/bin/env python
import mailroom4
# from cigar_party import cigar_party2 as cigar_party
# from cigar_party import cigar_party3 as cigar_party
                 
def test_list_name():
    donation_history = [
                    {'name':'Anna','donations':[100,200,300]},
                    {'name':'Bob','donations':[1000,2000]},
                    {'name':'Chuck','donations':[10000]},
                    {'name':'David','donations':[1]},
                    {'name':'Ethan','donations':[10,20]}
                 ]
    expected = ['Anna', 'Bob', 'Chuck', 'David', 'Ethan']
    assert (expected == mailroom4.list_name()) is True
    
def test_create_a_report():
    donation_history = [
                    {'name':'Anna','donations':[100,200,300]},
                    {'name':'Bob','donations':[1000,2000]},
                    {'name':'Chuck','donations':[10000]},
                    {'name':'David','donations':[1]},
                    {'name':'Ethan','donations':[10,20]}
                 ]
    expected = [['Chuck', '$', 10000, 1, '$', 10000.0],
                ['Bob', '$', 3000, 2, '$', 1500.0],
                ['Anna', '$', 600, 3, '$', 200.0],
                ['Ethan', '$', 30, 2, '$', 15.0],
                ['David', '$', 1, 1, '$', 1.0]]
    assert (expected == mailroom4.create_a_report()) is True
    
def test_create_summary():
    donation_history = [
                    {'name':'Anna','donations':[100,200,300]},
                    {'name':'Bob','donations':[1000,2000]},
                    {'name':'Chuck','donations':[10000]},
                    {'name':'David','donations':[1]},
                    {'name':'Ethan','donations':[10,20]}  
                    ]
    expected = [
                 ['Anna', '$', 600, 3, '$', 200.0],
                 ['Bob', '$', 3000, 2, '$', 1500.0],
                 ['Chuck', '$', 10000, 1, '$', 10000.0],
                 ['David', '$', 1, 1, '$', 1.0],
                 ['Ethan', '$', 30, 2, '$', 15.0]]
    assert (expected == mailroom4.create_summary()) is True
