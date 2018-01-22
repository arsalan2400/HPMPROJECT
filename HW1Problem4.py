#Print ours1 and ours2. Describe how ours1and ours2differfrom each other.#
yours = ['Yale','MIT','Berkeley']
mine= ['University of Connecticut','Lousiana State University','Florida State University']
ours1 = yours + mine
print(ours1)

ours2=[]
yours = ['Yale','James Bond College','Berkeley']
ours2.append(yours)
ours2.append(mine)
print(ours2)

yours[1] = 'James Bond College'
print(yours)
#this is just to show it begins at zero, not 1

print(ours1) #still uses MIT#
print(ours2) #Ours2 is dependent on 'Yours' list, so it will change to James Bond College#

print('Ours1 is a stored list that is not affected by the updated. Ours2 is dependent on Yours list, so it will change to James Bond College but Ours1 will not. '
      'The change from Yale to J.B.C. comes later in the code and does not affect the Ours1 component lists')
#done
