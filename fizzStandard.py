for i in range(1,101):
  s = ""
  if i % 3 == 0: s += "fizz "
  if i % 5 == 0: s += "buzz "
  if s == "": s = str(i)
  print(s)


input() # END
