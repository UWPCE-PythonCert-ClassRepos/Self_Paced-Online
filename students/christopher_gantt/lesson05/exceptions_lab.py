#!/usr/bin/env python3

def safe_input():
    try:
        input("type something")
    except (EOFError, KeyboardInterrupt):
        return None

safe_input()