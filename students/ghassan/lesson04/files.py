#!/usr/bin/env python3

import os

for files in os.listdir('.'):
    print(os.path.abspath(files))
