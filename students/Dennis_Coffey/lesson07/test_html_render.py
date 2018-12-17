# -*- coding: utf-8 -*-
"""
Test suite for HTML render lesson 07 exercise
"""

import pytest

from io import StringIO

# importing the html_rendering code with a short name for easy typing.
import html_render as hr

from run_html_render import *

f = StringIO()
page.render(f)


# Test for Step 1 of run_html_render
#def test_Element():
#    assert f.getvalue() == 'Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some textAnd here is another piece of text -- you should be able to add any number'

# Funtion to compare desired vs generated result for each step
def compare_files(desired_file, generated_file):
    desired_file = open(desired_file)
    desired_result = desired_file.read()
    generated_file = open(generated_file)
    generated_result = generated_file.read()
    assert desired_result == generated_result
    desired_file.close()
    generated_file.close()

# Test for Step 2 of run_html_render
def test_step2():
    compare_files('test_html_output2.htm', 'test_html_output2.html')        
    
# Test for Step 3 of run_html_render
def test_step3():
    compare_files('test_html_output3.htm', 'test_html_output3.html')        

# Test for Step 4 of run_html_render
def test_step4():
    compare_files('test_html_output4.htm', 'test_html_output4.html')        

# Test for Step 5 of run_html_render
def test_step5():
    compare_files('test_html_output5.htm', 'test_html_output5.html')        


# Test for Step 6 of run_html_render
def test_step6():
    compare_files('test_html_output6.htm', 'test_html_output6.html')        

# Test for Step 7 of run_html_render
def test_step7():
    compare_files('test_html_output7.htm', 'test_html_output7.html')        

# Test for Step 8 of run_html_render
#def test_step8():
#    compare_files('test_html_output8.htm', 'test_html_output8.html')        
