# marks=float(input("Enter your marks="))
# if(marks>=90):
#     print("Grade A+")
# elif(marks>=75):
#     print("Grade B+")
# elif(marks>=55):
#     print("Grade C")
# elif(marks>=35):
#     print("Grade D")
# elif(marks>=0):
#     print("Grade Fail")
# else:
#     print("!!!!Wrong Input")

try:
    marks = float(input("Enter your marks = "))

    if marks >= 90:
        print("Grade A+")
    elif marks >= 75:
        print("Grade B+")
    elif marks >= 55:
        print("Grade C")
    elif marks >= 35:
        print("Grade D")
    elif marks >= 0:
        print("Grade Fail")
    else:
        print("Sorry! Wrong Input")

except ValueError:
    print("Sorry! Wrong Input. Please enter numbers only.")