c=int(input())
if (c<60):
    print(c*0,c)
elif (c>=60):
    print(c//60% c%60)
