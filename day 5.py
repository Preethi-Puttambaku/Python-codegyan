#iƒ elif else condition
#check wheather number is positive  or zero or negative
'''num = int(input())
if num == 0:
    print("Zero")
elif num > 0:
    print("Postive")
elif num <0: 
    print("negative")
# else statement is optional it is not compulsary to mention it

#grade calculation marks read marks liedin between 92 to 100 grade A
# 80 to 89 grade b, 60 to 79 grade c,40 to 59 grade d , below 40 grade f

marks = int(input())
if 90 <=marks<=100:
    print("Grade is A")
elif 80<=marks<=89:
    print("Grade is B")
elif int(60<=marks<=79):
    print("Grade is C")
elif int(49<=marks<=59):
    print("Grade is D")
elif int(40 >= marks):
    print("Grade is F")
elif int(marks > 100):
    print("Invalid")

#check whaether a number is positive even or negative even or positive odd or negative odd
n = int(input())
if n <0 & n % 2==0:
    print("positive even")
elif n <0 & n %2==0:
    print("Negative even")
elif n >0 & n % 2== 1:
    print("positive odd")
else:
    print("negative odd")'''

#Nested loop
#positve even positive odd negative even negative odd
n = int(input())
if n  %2 ==0:
    if n>0:
        print("positive even")
    else:
        print("negative even")
elif n % 2 ==1:
    if n >0:
        print("positive odd")
    else:
        print("negative odd")

    

