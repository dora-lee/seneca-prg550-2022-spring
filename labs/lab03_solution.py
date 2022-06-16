# program: L3_solution.py
# author:  Danny Abesdris
# date:    06-Jun-2022
# purpose: python functions for online submission for PRG550 summer 2022 Lab #3

def loadDictionary(myDict, seq1, letter='X') :
   myDict[letter] = seq1
   return myDict

def dotProduct(myDictParam) :
   myKeys = list(myDictParam.keys( ))

   dotList = [ ]
   for i in range(len(myDictParam[myKeys[0]])) :
      tempVar = 1
      for key in myKeys :
         tempVar *= myDictParam[key][i]

      dotList.append(tempVar)


   final = reduce(lambda x, y : x + y, dotList)
   return final


def integerToRoman(n) :
   rvStr = ""
   romansDict = { 1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M" }
 
   if n < 1 or n > 3999 :
      rvStr = "Invalid"
   else :
      while n > 0 :
         if n >= 1000 :
            t = int(n / 1000)
            for i in range(t) :
               rvStr += "M"
            n -= (1000 * t)

         elif n >= 100 :
            h = int(n / 100)
            if h >= 9 :
               rvStr += (romansDict[100] + romansDict[1000]) # 900
               n -= 900
            elif h >= 5 :
               rvStr += romansDict[500]  # 500
               n -= 500
            elif h >= 4 :
               rvStr += (romansDict[100] + romansDict[500]) # 400
               n -= 400
            else :
               rvStr += romansDict[100]  # 100
               n -= 100

         elif n >= 10 :
            tens = int(n / 10)
            if tens >= 9 :
               rvStr += (romansDict[10] + romansDict[100]) # 90
               n -= 90
            elif tens >= 5 :
               rvStr += romansDict[50]  # 50
               n -= 50
            elif tens >= 4 :
               rvStr += (romansDict[10] + romansDict[50]) # 40
               n -= 40
            else :
               rvStr += romansDict[10]  # 10
               n -= 10

         elif n >= 9 :
            rvStr += (romansDict[1] + romansDict[10]) # 9
            n -= 9
         elif n >= 5 :
            rvStr += romansDict[5]  # 5
            n -= 5
         elif n >= 4 :
            rvStr += (romansDict[1] + romansDict[5]) # 4
            n -= 4
         else :
            rvStr += romansDict[1]  # 1
            n -= 1

   return rvStr
