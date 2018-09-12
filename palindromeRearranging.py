def palindromeRearranging(inputString):

  if len(inputString) % 2 == 0:
    for char in inputString:

      if inputString.count(char) % 2 != 0:
        return False
    return True

  if len(inputString) % 2 != 0:
    oddCharCount = 0
    checkedChars = []
    for char in inputString:
      if char not in checkedChars:
        if inputString.count(char) % 2 != 0:
          oddCharCount +=1
        checkedChars.append(char)
        if oddCharCount > 1:
          return False
      return True
