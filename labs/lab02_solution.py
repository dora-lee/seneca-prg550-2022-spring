# program: L2_solution.py
# author:  Danny Abesdris
# date:    30-May-2022
# purpose: python functions for online submission for PRG550 summer 2022 Lab #2

def drawPascalsTriangle(nRows) :
  triangle = "1\n"
  row = "1"
  for i in range(nRows - 1) :
     nextRow = ""
     fn = 0
     for item in row.split(" ") :
        nextRow += str(fn + int(item)) + " "
        fn = int(item)

     row = nextRow + "1"
     triangle += row + "\n"

  print(triangle)


def alphaFrequency(userString) :
  print(userString)
  chars = [0] * 26
  for i in userString.lower( ) :
     if i in string.ascii_lowercase :
        chars[ord(i) - ord('a')] = userString.lower( ).count(i)
  for j in string.ascii_lowercase :
     if chars[ord(j) - ord('a')] > 0 :
        print(j, "=", chars[ord(j) - ord('a')], "*" * chars[ord(j) - ord('a')])

def encryptStr(text, n) :
  result = ""
  # transverse the plain text
  for i in text:
     # Encrypt uppercase characters in plain text
     if i.isalpha( ) :
        if i.isupper( ) :
           if ord(i) - ord('A') + n % 26 > 25 :
              cipher = chr(ord('A') + n % 26 - (ord('Z') - ord(i)))
           else :
              cipher = chr(ord(i) + n % 26)
        else :
           if ord(i) - ord('a') + n % 26 > 25 :
              #print("lowercase, with wrap, letter:", i, " value of subtraction:", ord(i) - ord('a'))
              cipher = chr(ord('a') + n % 26 - (ord('z') - ord(i)))
           else :
              #print("lowercase, with wrap, letter:", i, " value of subtraction:", ord(i) - ord('a'))
              cipher = chr(ord(i) + n % 26)
        result += cipher

     else :
        result += i

  print(result)
  return result
