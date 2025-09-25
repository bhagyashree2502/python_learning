# loops >> loops are used to run same code for multiple times in a program. 
# 1. for loop : used to repeat code a fixed number of times
# 2. while loop : used when you don’t know in advance how many times to repeat.

for i in range(5):  
    print("Iteration:", i)

# output: 
# Iteration: 0
# Iteration: 1
# Iteration: 2
# Iteration: 3
# Iteration: 4

count = 0

while count < 3:
    print("Count is:", count)
    count += 1

# output: 
# Count is: 0
# Count is: 1
# Count is: 2

#find the numbers of characters in a user name
user_name = input("Enter your name: ")
if(len(user_name)<10):
    print("Your name contain less than 10 letters")
else:
    print("All is well!!")    

t = (6, 3231, 75, 122)
for i in t:
    print(i)

s = "Bhagyashree"
for j in s:
    print(j)    

l = [1,7,8]
for i in  l:
    print(i)
else:
    print("done")