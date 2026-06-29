a = input("enter your name: ")
b = int(input("enter your marks: "))
print("studen Name is: ",a)
if b>= 35:
    print("you have passed in this exaam")
    if b >= 90:
        print("you are good student in this school")
    elif b <=85:
        print("you will pay 500 rupees ")
else:
    print("you are fail")