#Problem 1:Object Types(Weight 2).Consider the number 17.
# Construct multiple variables (y1, y2, y3, and y4) in Python that represent
# thenumber17 in the various forms of objects (integer, float, string, and Boolean,
#  respectively).Hint: For creation of the Boolean,
# set a valuefor 17 to be compared against another number.
# Print the value of y1, y2, y3, and y4 and their types
# (Hint:you can use function type()to get a type of an
# object or variable).

#PROBLEM 1#
X=17
print('The value of X is ',X)

#integer#
x=17
y1= x
print('y1 is a' ,type(y1))
print('The value of y1 is' ,(y1))

#float#
x = 17
y2 = float(x)
print('y2 is a' ,type(y2))
print('The value of y2 is' ,(y2))

#string#
x=17
y3= str(x)
print('y3 is a' ,type(y3))
print('The value of y3 is' ,(y3))

#boolean, '17<18'
y4 = bool(x>18)
print('y4 is a' ,type(y4))
print('When put to the test whether 17 is greater than 18, y4 is' ,(y4))

#done
