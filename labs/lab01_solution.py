# program: L1_solution.py
# author:  Danny Abesdris
# date:    23-May-2022
# purpose: python functions for online submission for PRG550 summer 2022 Lab #1

def drawPyramid(rows) :
   digits = string.digits
   for i in range(rows) :
      line = " " * (rows - i - 1)
      line += (digits[0 : i + 1] + "".join(reversed(digits[0 : i])))
      print(line)

def threeLetterCombinations(letter) :
   for a in range(ord('a'), ord(letter)+1) :
      for b in range(ord('a'), ord(letter)+1) :
         for c in range(ord('a'), ord(letter)+1) :
            print(chr(a), chr(b), chr(c))


def allNarcissisticNumbers(limit) :
   for i in range(1, limit + 1) :
      sum = 0
      temp = i
      exp = len(str(temp))
      if exp > 1 :
         while temp > 0 :
            digit = temp % 10
            sum += digit ** exp
            temp //= 10

         if i == sum :
            print(i)
