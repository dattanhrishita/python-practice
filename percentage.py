'''wap to accept percentage from user and make a decision about
his grade .if percenatge greater than 70 mark as o grade otherwise if greater than 60
A grade and  40 B grade other wise failed'''


mark=int(input("Enter the marks"))
if mark>=70:
    print("The grade is O")
elif mark>=60:
    print("the grade is A")
elif mark>=40:
    print("the grade  is B")
else:
    print("fail")
