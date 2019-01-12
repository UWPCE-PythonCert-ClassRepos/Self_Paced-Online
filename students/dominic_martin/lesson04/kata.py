#!/usr/bin/env Python 3
import string

def txtRead():
	f = open('58639.txt')
	txt_data = f.read()
	f.close()
	# print(txt_data)
	new_Txt = txt_data.translate(string.punctuation)
	# new_trigrams = []
	# c = 2
	# while c < len(txt_data) - 2:
	# 	new_trigrams.append((txt_data[c], txt_data[c+1], txt_data[c+2]))
	# 	c += 2
	print(new_Txt)

def main():
	txtRead()

main()