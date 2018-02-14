#!/usr/bin/env python3


def hz_line(size, cell=2):
	for j in range(0, cell):
		print('+', end=' ')
		for i in range (0, size):
			print (' '+'-'+' ', end='')
	print('+')

def vt_line(size, cell=2):
	for y in range(0, cell):
		print('|', end=' ')
		for x in range(0, size):
			print (' '* 3, end='')
	print('|')

def gridify(size):
	for z in range(0, 2):
		hz_line(size)
		for s in range(0, size):
			vt_line(size)
	hz_line(size)

def rectanglize(size, cell):
	for z in range(0, cell):
		hz_line(size, cell)
		for s in range(0, size):
			vt_line(size, cell)
	hz_line(size, cell)


gridify(3)
rectanglize(4, 4)

