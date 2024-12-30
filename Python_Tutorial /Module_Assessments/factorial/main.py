input_user=int (input("enter your number ")) 

fact=1
count=1
while count <=input_user:
    fact=fact*count
    count=count+1

print("the factorial is : ",fact)