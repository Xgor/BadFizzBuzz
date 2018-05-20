fbCombo = ["Fizz Buzz","","","Fizz","","Buzz","Fizz","","","Fizz","Buzz","","Fizz","",""]
for i in range(1,101):
    if fbCombo[i%15] == "": print(i)
    else: print(fbCombo[i%15])

input() # END
