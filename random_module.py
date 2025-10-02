import random

# In this lecture we will discuss:
# -What is Randomization
# -What is Random Module in Python
# -randint() function
# -randrange() function
# -random() function
# -choice() function
# -uniform() function
# -shuffle() function

print(random.randint(1,2)) # btw 1 to 2 both include
print(random.randrange(1,3)) # 3 is not include it give 1 or 2 not 3
print(random.random()) # Give a random  floating value between 0.0 to 1.0
print(random.uniform(1,4)) # it gave a floating value

arr = [1,2,3,4,5,6,7]
print(random.choice(arr))
random.shuffle(arr)
print(arr)