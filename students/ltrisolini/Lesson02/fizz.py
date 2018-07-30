{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf400
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
###Lesson 2 Fizz Buzz###\
for i in range(1, 101):\
    if (i % 3 == 0) and (i % 5 == 0):\
        print("FizzBuzz")\
    elif (i % 5 == 0):\
        print("Buzz")\
    elif (i % 3 == 0):\
        print("Fizz")\
    else:\
        print(i)}