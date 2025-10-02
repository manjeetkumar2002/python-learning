# when a function calls itself it is called recursion

#1. infinite recursion
# RecursionError: maximum recursion depth exceeded
# def greet():
#     print("Hello")
#     greet()
# greet()

#problem1 : print "Anirudh" 4 times [head recursion]
# count = 0
# def func():
#     global count
#     if count == 4:
#         return
#     print("Anirudh")
#     count += 1
#     func()
#
# func()

#problem2 : print "Anirudh" 4 times [tail recursion/backtracking]
# count = 0
# def func():
#     global count
#     if count == 4:
#         return
#     count += 1
#     func()
#     print("Anirudh")
# func()

#problem3 : print x n times
# def func(x,n):
#     if n==0:
#         return
#     print(x)
#     func(x,n-1)
#
# func(20,4)

#problem4 : print 1 to N [head recursion]
# def func(i,n):
#     if i>n:
#         return
#     print(i)
#     func(i+1,n)
#
# func(1,5)

#problem5 : print 1 to N [Tail recursion]
# def func(n):
#     if n==0:
#         return
#     func(n-1)
#     print(n)
#
# func(4)

#problem6 : print N to 1 [head recursion]
# def func(n):
#     if n==0:
#         return
#     print(n)
#     func(n - 1)
#
# func(4)

#problem7 : print N to 1 [tail recursion]
# def func(i,n):
#     if i>n:
#         return
#     func(i+1,n)
#     print(i)
#
# func(1,4)


# Parameterised recursive function are those where we don't return a value in base condition
# function recursive function are those where we return a value in base condition

#problem8: sum of 1 to n [parameterised recursion]

# def func(sum,i,n):
#     if i>n:
#         print(sum)
#         return
#     func(sum+i,i+1,n)
#
# func(0,1,10)

#problem9: sum of 1 to n [functional recursion]


def func(n):
    if n==1:
        return 1
    return n + func(n-1)

answer = func(10)
print(answer)