#Python Ternary Operator
def testTenary():
    age = int(input('Enter your age : '))
    #if (age >= 18):
    #   ticket = 120
    #else:
    #   ticket = 60
    ticket = 120 if age>=18 else 60
    print(f"ticket price = {ticket}")