#!/usr/bin/env python3

import os

for l in os.listdir():
    print("{}\{}".format(os.getcwd(),l))