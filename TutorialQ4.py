
lily = ['Wax apple','kiwi','strawberries']
reddy= ['mango','blueberries','watermelon']
both = lily + reddy
print(both)

both2=[]
both2.append(lily)
both2.append(reddy)
print(both2)

lily[1] = 'gala apples'
print(lily)
#this is just to show it begins at zero, not 1

print(both) #still uses kiwi#
print(both2) #booth 2 is dependent on lily list, so it will change to gala apples#
