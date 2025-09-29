'''
#   *
#  ***
# *****
n = int (input("enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1),end="")   #end="" >>>>>does not gives by default new line
    print("")
for i in range(1,n+1):
    print("*" *i, end="")
    print("")
'''
'''
# * * *
# *   *
# * * *
for i in range(1,n+1):
    if(i==1 or i ==n ):
        print("*"*n)
    else:
        print("*", end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")  #new line
'''