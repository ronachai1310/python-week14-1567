#python if-elseif else Statement

def testGrade():
    score = int(input("Enter score "))
    if (score>=80 and score<100):
        print(score,"is A")
    elif(score>=75 and score<80):
         print(score,"is B+")
    elif(score>=70 and score<75):
         print(score,"is B")
    elif(score>=65 and score<70):
         print(score,"is C+")
    elif(score>=60 and score<65):
         print(score,"is C")
    elif(score>=55 and score<60):
         print(score,"is D+")
    elif(score>=50 and score<55):
         print(score,"is D")
    elif(score>=0 and score<50):
         print(score,"is F")
    else:
         print(score,"ERROR SCORE")