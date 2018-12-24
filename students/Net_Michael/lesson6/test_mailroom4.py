#!/usr/bin/env python
# coding: utf-8

import unittest
import os
import io
import pathlib
import shutil
import re
import pytest
import string
from collections import defaultdict
from mailroom4 import list_dir_path

class list_dir_path_test( unittest.TestCase):
    # list_dir_path lists files in directory_1, that is, given
    # ~/directory_1/directory_2 will list all files and directories in directory_1
    # and directory_2 is the folder containing the current working directory

    def list_dir_path(self):
        test_values = os.path.dirname( os.getcwd())
        actual =  test_values in list(list_dir_path())[1][1]
        expected = True
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
