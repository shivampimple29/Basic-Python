# Write a program to find out whether a student is pass or fail, if it requires total 40% and At least 33%, in each subject to pass. Assume 3 
# Subjects and take marks as an input from the user
sub1=int(input("Enter ur marks in percentage: "))
sub2=int(input("Enter ur marks in percentage: "))
sub3=int(input("Enter ur marks in percentage: "))
sum=sub1+sub2+sub3
avg=sum/3
if(avg>40 and sub1>=33 and sub2>33 and sub3>=33):
    print("PASS")
else:
    print("FAIL")
