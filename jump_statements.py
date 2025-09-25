# Jump Statements (break, continue, pass)
# 1.break: stop the loop immediately
# 2.continue: skip the current iteration and go to the next one
# 3.pass: do nothing (used as a placeholder)

#************* BREAK*************
for i in range(100):
    if(i==33):
        break #exit the loop right now
    print(i)  

#*******CONTINUE********
for i in range(100):
    if(i==33):
        continue #skip this iteration
    print(i)  

#*****PASS****
for i in range(3):
    if i == 1:
        pass  # does nothing, avoids error for empty block
    print(i)

#generate a table of any number
n = int (input("enter the number: "))
for i in  range(1,11):
    print(f"{n} X {i} = {n * i}")