# 4.The nested if statement

def testNestedIf():
    num = float(input("Enter number "))
    if(num >= 0):
        if(num == 0):
            print(num, "is Zero number ")
        else:
            print(num, "is Positive number ")
    else:
        print(num, "is Negative number ")