def QuestionsMarks(strParam):
  """
    >>> QuestionsMarks("acc?7??sss?3rr1??????5")
    True
    >>> QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?5")
    False
    >>> QuestionsMarks("9???1???9??1???9")
    False
    >>> QuestionsMarks("aa6?9")
    False
    >>> QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?5")
    False
  """
  l, r = 0, 1
  cond = False
  while r < len(strParam):
    left = strParam[l]
    right = strParam[r]
    if left.isnumeric() and right.isnumeric() and int(left) + int(right) == 10:
      sub = strParam[l:r]
      cond = sub.count('?') == 3
      l = r
      if not cond:
        return cond
    elif right.isnumeric():
      l = r
    r += 1
  
  return cond

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)