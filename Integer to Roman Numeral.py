"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""



class Solution:
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    #Defining the value of Roman numerals and their value
    conversionChart = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
    #Convert the string to uppercase to match the values in the dictionary
    s = s.upper()

    #Initializing variables
    total = 0
    currentPosition = (len(s))
    lastPosition = 0

    #logic of converting roman numberals to integers
    while currentPosition-1 >= 0:
        if conversionChart[s[currentPosition-1]] >= conversionChart[s[lastPosition-1]]:
            total += conversionChart[s[currentPosition-1]]
        else:
            total -= conversionChart[s[currentPosition-1]]

        # move the pointers toward the front of the string    
        lastPosition = currentPosition
        currentPosition = currentPosition - 1
        
    return(total)





"""
Testing Solution
def romanToInt(s):
    #:type s: str
    #:rtype: int
    
    #Defining the value of Roman numerals and their value
    conversionChart = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
    #Convert the string to uppercase to match the values in the dictionary
    s = s.upper()
    print(s)

    #Initializing variables
    total = 0
    currentPosition = (len(s))
    lastPosition = 0

    #logic of converting roman numberals to integers
    while currentPosition-1 >= 0:
        if conversionChart[s[currentPosition-1]] >= conversionChart[s[lastPosition-1]]:
            total += conversionChart[s[currentPosition-1]]
            print(total, " added to Total")
        else:
            total -= conversionChart[s[currentPosition-1]]
            print(total, " subtracted from Total")

        # move the pointers toward the front of the string    
        lastPosition = currentPosition
        currentPosition = currentPosition - 1
        
    return(total)

print(romanToInt("xxx"))
print(romanToInt("xIx"))
print(romanToInt("C"))
print(romanToInt("CM"))
print(romanToInt("MDCCC"))

"""