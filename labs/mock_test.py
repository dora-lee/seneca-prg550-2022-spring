#########################################
# This file is used for local testing 
#########################################
#
# program: MOCKmain.py
# author:  Seneca Student
# date:    15-Jun-2022
# purpose: python main() program for PRG550 summer 2022 MOCK test
#



import math
import random
import string
import collections
import datetime
import re
import time
import copy


def displayNums(n):
    for idx in range(0,n):
        print(idx+1)


def displayInTriplicate(letter):
    print(letter*3)



def main() :
   displayNums(5)
   displayInTriplicate('c')
   displayNums(8)
   displayNums(2)
   displayInTriplicate('?')


if __name__ == "__main__" : 
   main()

    