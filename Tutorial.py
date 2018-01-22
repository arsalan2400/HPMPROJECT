X=23
print('Setting x=',X)

#integer#
x=23
y1= x
print('y1 is a' ,type(y1))

#float#
x = 23
y2 = float(x)
print('y2 is a' ,type(y2))

#string#
x=23
y3= str(x)
print('y3 is a' ,type(y3))

#boolean, '23>18'
y4 = bool(x>18)
print('y4 is a' ,type(y4))
print(y4)

#how do we split up stuff? you could add a space after
#the ones you want
text = "python" + "is" + "fun" + "!"
text= 'python ' + 'is ' + 'fun ' + '!'

#Question2
#how do we split up stuff? you could add a space after#
#the ones you want#
print('python' + 'is' + 'fun' + '!')
print('python ' + 'is ' + 'fun ' + '!')

#Question3 was done in actuality

#Question4

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

#Question5
dayNumbers= {'Sunday':1, 'Monday':2, 'Tuesday':3, 'Wednesday':4, 'Thursday':5, 'Friday':6, 'Saturday':7,
             1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}
print(dayNumbers[2])

print('The second day of the week is ', dayNumbers[2])
print('Friday is day ', dayNumbers['Friday'])
