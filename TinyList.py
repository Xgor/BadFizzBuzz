fbCombo = ["Fizz Buzz","","","Fizz","","Buzz","Fizz","",""]

for i in range(1,101):
    v = 0
    if i % 15 < 8: v = i%15
    else: v = int(7.5-i % 7.5)
    if fbCombo[v] == "": print(i)
    else: print(fbCombo[v])

input() # END
