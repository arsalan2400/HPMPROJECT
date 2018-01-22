1#Write an iterativefunction and a recursivefunction that computes
#the sum of all numbers from
#1 to n, where nis given as parameter.
#Test both functions for n = 100. Why is it 101 instead of 100? because -1

def sum_it(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
print(sum_it(100))

#recursive

def sum_rec(n):
    if n== 1:
        return 1
    else:
        return n + sum_rec(n-1)
print(sum_rec(100))
#whatever the function returns, we will add it.
# If n=44, we will add to sum(n=43)
print(sum_rec(100))

#done
