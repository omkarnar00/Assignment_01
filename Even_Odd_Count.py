even,odd=0,0
n=int(input("Enter The Range :"))
for i in range(1,n):
    if i % 2 == 0:
        even=even+1
    else :   
        odd=odd+1 
print("Number Of Even Numbers : {} \nNumber Of Odd Numbers : {}".format(even ,odd))        

###  Enter The Range :10
###  Number Of Even Numbers : 4 
###  Number Of Odd Numbers : 5 