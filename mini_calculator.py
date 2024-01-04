a = int(input(" enter the 1st number "))
b= int(input(" enter the 2nd number "))
user = str(input("I chose to"))
print(user)
if user=="add":
    print(a+b)
elif user == "mul":
    print(a*b)
elif user == "sub":
    print(a-b)
elif user == "div":
    print(a/b)
else:
    print("Choose the valid operation you want to calculate")
