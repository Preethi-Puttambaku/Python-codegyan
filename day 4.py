#data types
#input reading from user 
name = input()
print(type(name),name)

#reading integers from user
num = int(input())
print(type(num),num)

# reading float from user
num = float(input())
print(type(num),num)

#reading complex numbers
x= int(input())
y = int(input())
c = complex(x,y)
print(type(c),c)

# reading boolean values
n = bool((input()))#in boolean first it will read as string then it should convert into'int' and then it will convert it into'bool'
print(type(n),n)

#to print boolean not converting it into int we can write
n = bool(input())
print(type(n),n)

#one egg price is 5 rps and what is the price of N eggs
one_egg = int(5)
N = int(input("Enter the value:"))
total = int(one_egg * N)
print("Cost of N eggs is:",total)

#If box cotains N pencils and total price is M,then waht price of each
#pencil price
N = int(input("Enter how many pencils contained in a box:"))
M = int(input("Enter total pprice of box:"))
each_pencil = int(N/M)
print("The cost of each pencil is:",each_pencil)

#red ball price is 25 green ball price is 30 if i buy N red balls and M green balls then what is the total cost 
red = int(25)
green = int(30)
n = int(input())
m = int(input())
n_red = int(n * red)
m_green = int(m * green)
total = print(int(n_red + m_green))

# If condition
a = 20
b = 25
print(a,b)
c = a+b
if c == 45:# if the condition is true the block code wont execute 
    print(c)
print("programe done") # if false it will execute

# if else condition
stock = 10
if stock > 0:
    print("stock availiable")
else:
    print("stock unavailiable")
print("not")


#practice questions
#check if a number is zero or non zero
num  = int(input())
if num == 0:
    print('Yes')
print('No')

#check number is positive or not
num = int(input())
if num >0:
    print("Positive")
print("Negative")

#Or
num = int(input())
if num <=0:
    print("Negative")
print("Positive")

#checking if a number is even or odd
num = int(input())
if num % 2 ==0:
    print("even")
else:
    print("odd")

#check whether a person is eligible for vote or not
num = int(input())
if num >= 18 :
    print("eligigble")
else:
    print("Not eligible")

#checking wheather number is divisible by 3 or not
num = int(input())
if num % 3 ==0 :
    print("yes")
else:
    print("No")

#checking if a number is divisible by both 3 and 5 or not
num = int(input())
if num % 3 ==0 & num % 5 ==0 :
    print("yes")
else:
    print("no")

#find bigger number among two numbers
num1 =int(input())
num2 =int(input())
if num1 > num2 :
    print(num1,"is greater")
else:
    print(num2,"is bigger")
    


    
    
    
    


          
   
    
        


