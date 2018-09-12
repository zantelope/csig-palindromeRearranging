def palindromeRearranging(inputString):

  if len(inputString) % 2 == 0:
    for char in inputString:

      if inputString.count(char) % 2 != 0:
        return False
    return True

  if len(inputString) % 2 != 0:
    charInstances = []
    checkedChars = []
    for char in inputString:
      if char not in checkedChars:
        charInstances.append(inputString.count(char))
        checkedChars.append(char)
    oddChars = 0
    for element in charInstances:
      if element % 2 != 0:
        oddChars +=1
      if oddChars > 1:
        return False
    return True
