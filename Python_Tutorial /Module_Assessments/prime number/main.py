input_user=int (input("enter your number : "))

if input_user > 1:
    for i in range(2,input_user):
        if (input_user % i)==0 :
            print("number is not prime")

        else :
            print("number is prime")
else :
    print("number is prime")